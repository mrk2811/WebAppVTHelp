from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from users.models import Comments
from .models import placesOfInterest, regular_user, admin, User
from actions.models import Action
from django.http import JsonResponse
import requests


# Create your views here.
def places_of_interest_list(request):

    places = placesOfInterest.objects.all()
    sorted_places = placesOfInterest.objects.order_by('id')

    return render(request,
                  "vt_help/places_of_interest/list.html",
                  {"places": places})

def places_of_interest_detail(request, place_id):
    places = placesOfInterest.objects.all().order_by('-date_posted');
    for place in places:
        if place.id == place_id:
            break
    comments = Comments.objects.all().filter(place=place).order_by('-date_posted');
    return render(request,
                  "vt_help/places_of_interest/detail.html",
                  {"place": place, "comments": comments})

def places_of_interest_home(request):

    actions = Action.objects.all();
    return render(request,
                  "vt_help/places_of_interest/home.html",
                  {"actions": actions})

def places_of_interest_login(request):
    return render(request,
                  "vt_help/places_of_interest/login.html")

def places_of_interest_add(request):
    return render(request,
                  "vt_help/places_of_interest/add.html")

def add(request):

    # redirect if not logged in
    if not request.session.get("username", False):
        return redirect('vt_help:views.places_of_interest_home')

    user = User.objects.get(username=request.session.get("username"))
    if request.method == 'POST':
        # process the form
        title = request.POST.get('add-a-title')
        location = request.POST.get('add-a-location')
        shortdescription = request.POST.get('add-a-brief-overview')
        pls = placesOfInterest(
            title=title,
            location=location,
            shortDescription=shortdescription,
            campus='Blacksburg',
            category='Entertainment',
            type='Sports & Games',
            url='#',
            author=request.session.get('username'),
            user=user,
        )
        pls.save()


        #log the action
        action = Action(
            user=user,
            verb="created a place",
            target=pls
        )
        action.save()

        messages.add_message(request, messages.SUCCESS, "You successfully submitted the place: %s" % pls.title)
        return redirect("vt_help:views.places_of_interest_detail", pls.id)
    else:
        # show the form
        return render(request, "vt_help/places_of_interest/add.html")

def edit(request, place_id):
    places = placesOfInterest.objects.all()
    for place in places:
        if place.id == place_id:
            place.title = request.POST.get('add-a-title')
            place.location = request.POST.get('add-a-location')
            place.shortDescription = request.POST.get('add-a-brief-overview')
            place.save()
            messages.add_message(request, messages.INFO, "You successfully edited the place: %s" % place.title)
            return redirect("vt_help:views.places_of_interest_detail", place.id)
            break
    else:
        # show the form
        return render(request,
                      "vt_help/places_of_interest/edit.html",
                      {"place": place})

def places_of_interest_edit(request, place_id):
    places = placesOfInterest.objects.all()
    for place in places:
        if place.id == place_id:
            break
    return render(request,
                  "vt_help/places_of_interest/edit.html",
                  {"place": place})

def delete(request, place_id):
    places = placesOfInterest.objects.all()
    for place in places:
        if place.id == place_id:
            place.delete()
            #place.save()
            #placesOfInterest.objects.get('place_id').delete()
            #placesOfInterest.objects.
            #places.update()
            messages.add_message(request, messages.WARNING, "You deleted the place: %s" % place.title)
            break
    return redirect("vt_help:views.places_of_interest_list")

def sort_recent(request):
    sorted_places = placesOfInterest.objects.order_by('id')
    return render(request,
                  "vt_help/places_of_interest/list.html",
                  {"places": sorted_places})

def sort_title(request):
    sorted_places = placesOfInterest.objects.order_by('title')
    return render(request,
                  "vt_help/places_of_interest/list.html",
                  {"places": sorted_places})

def author_and_date(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

    if(is_ajax and request.method == "GET"):
        place_id = request.GET.get('place_id')
        try:
            place = placesOfInterest.objects.get(pk=place_id)
            author = place.author
            date_posted = place.date_posted
            return JsonResponse({'success': 'success', 'author': author, 'date_posted': date_posted}, status=200)

        except placesOfInterest.DoesNotExist:
            return JsonResponse({'success': 'new place succesfully added'}, status=200)
    else:
        return JsonResponse({'error': 'bad ajax request'}, status=400)

def edit_location(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

    if (is_ajax and request.method == "POST"):
        place_id = request.POST.get('place_id')
        new_location = request.POST.get('new_location')
        try:
            place = placesOfInterest.objects.get(pk=place_id)
            place.location = new_location
            place.save()
            jsonlocation = place.location
            return JsonResponse({'success': 'success', 'new_location': jsonlocation}, status=200)

        except placesOfInterest.DoesNotExist:
            return JsonResponse({'success': 'new place succesfully added'}, status=200)
    else:
        return JsonResponse({'error': 'bad ajax request'}, status=400)

def comment_add(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        username = request.POST.get('username')
        comment_text = request.POST.get('comment_text')
        place = request.POST.get('place')
        comment = Comments(
            text=comment_text,
            user=get_object_or_404(User, username=username),
            place=place,
        )
        comment.save()
        return JsonResponse({'success': 'success'}, status=200)

    else:
        return JsonResponse({'error': 'bad ajax request'}, status=400)
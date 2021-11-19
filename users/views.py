from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model
# Create your views here.
from users.models import Details


def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, "users/user/profile.html",
                  {"user": user}
                  )

def profile_edit_page(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, "users/user/profile_edit.html",
                  {"user": user}
                  )

def profile_edit(request, username):
    user = get_object_or_404(User, username=username)
    first_name = request.POST.get("add-first-name")
    last_name = request.POST.get("add-last-name")
    email = request.POST.get("add-email")
    password = request.POST.get("add-password")
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.set_password(password)
    if user == "admin":
        role = request.POST.get("add-role")
        user.details.role = role
    user.save()
    return redirect("users:profile", username)

def profile_list(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, "users/user/user_list.html", {"users": users})


def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        campus = request.POST.get('campus')
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.details.campus = campus
        user.save()

        messages.add_message(request, messages.SUCCESS, "You successfully registered with the username: %s" % user.username)
        request.session['username'] = user.username
        request.session['role'] = user.details.role
        messages.add_message(request, messages.SUCCESS,
                             "You have logged in successfully!.")

        return redirect("vt_help:views.places_of_interest_home")
    else:
        return render(request, "users/user/register.html",
                  )

def login_user(request):
    username = request.POST.get("username")
    pw = request.POST.get("pw")

    user = authenticate(username=username, password=pw)

    if user is not None:
        request.session['username'] = user.username
        request.session['role'] = user.details.role
        messages.add_message(request, messages.SUCCESS,
                             "You have logged in successfully!.")
    else:
        messages.add_message(request, messages.ERROR,
                             "Invalid username or password.")

    return redirect(
        "vt_help:views.places_of_interest_list")

def logout_user(request):
    del request.session['username']
    del request.session['role']
    return redirect("vt_help:views.places_of_interest_list")
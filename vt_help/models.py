import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class placesOfInterest(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=400)
    shortDescription = models.TextField(blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    campus = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('vt_help:views.places_of_interest_detail', args=[self.id])


# class placesOfInterest:
#     def __init__(self, id, title, location, shortDescription, likes, dislikes, campus, category, type, url):
#         self.id = id
#         self.title = title
#         self.location = location
#         self.shortDescription = shortDescription
#         self.likes = likes
#         self.dislikes = dislikes
#         self.campus = campus
#         self.category = category
#         self.type = type
#         self.url = url
#
# breakZonePlace = placesOfInterest(
#     1,
#     "BreakZone at Squires",
#     "Location: 117 Squires Student Center 290 College Avenue Blacksburg, VA 24061",
#     "Breakzone is Virginia Tech’s home of billiards, bowling, and table tennis. Breakzone’s relaxing environment offers a way to spend some time with friends or family",
#     200,
#     80,
#     "Blacksburg",
#     "Entertainment",
#     "Sports & Games",
#     "DetailedView.html"
# )
#
# place2 = placesOfInterest(
#     2,
#     "It's Game Time At The Superbowl",
#     "Location: 375 Arbor Dr NE, Christiansburg, VA 24073",
#     "Family entertainment center in Christiansburg, VA - Bowling, LaserTag, Spin Bumper Cars, Arcade.",
#     50,
#     2,
#     "Blacksburg",
#     "Entertainment",
#     "Sports & Games",
#     "#"
#
# )
#
# place3 = placesOfInterest(
#     3,
#     "Table Tennis at Virginia Tech",
#     "Location: 117 Squires Student Center 290 College Avenue Blacksburg, VA 24061",
#     "The organization aims to promote the sport of Table Tennis at Virginia Tech. Members practice every Sunday in Room 116 of the breakzone in Squires Student Center from 2:30 pm to 6:30 pm.",
#     43,
#     0,
#     "Blacksburg",
#     "Entertainment",
#     "Sports & Games",
#     "#"
#
# )
#
# place4 = placesOfInterest(
#     4,
#     "McComas Hall Recreational Sports",
#     "Location: 895 Washington St SW, Blacksburg, VA 24060",
#     "McComas Hall, located in the traffic circle at the intersection of Washington Street and West Campus Drive, houses one of the gyms on campus as well as the main administrative and business offices for Recreational Sports.",
#     32,
#     5,
#     "Blacksburg",
#     "Entertainment",
#     "Sports & Games",
#     "#"
#
# )

#places = []
# places.append(breakZonePlace)
# places.append(place2)
# places.append(place3)
# places.append(place4)

regular_user = {"username": "rick", "password": "regular"}
admin = {"username": "admin", "password": "admin"}
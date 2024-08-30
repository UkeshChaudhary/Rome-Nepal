from django.db import models
from accounts.models import User

# Create your models here.

#Place Models
class Place(models.Model):

    PLACE_TYPE_CHOICES = [
        ('Mountain Ranges and Trekking', 'Mountain Ranges and Trekking'),
        ('Historical and Cultural Sites', 'Historical and Cultural Sites'),
        ('National Parks and Wildlife Sanctuaries', 'National Parks and Wildlife Sanctuaries'),
        ('Lakes and Scenic Spots', 'Lakes and Scenic Spots'),
        ('Religious and Spiritual Sites', 'Religious and Spiritual Sites'),
        ('Adventure and Outdoor Activities', 'Adventure and Outdoor Activities'),
        ('Remote and Off-the-Beaten-Path Destinations', 'Remote and Off-the-Beaten-Path Destinations'),
        ('Cultural Villages', 'Cultural Villages'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    place_type = models.CharField(max_length=255, choices=PLACE_TYPE_CHOICES)
    images = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
    

#Place Image Modles

# class PlaceImage(models.Model):
#     place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='places/images/')
#     description = models.TextField(blank=True, null=True)

    

#     def save(self, *args, **kwargs):
#         #Ensure the directory structure is created based on the place name

#         if self.place:
#             self.image.field.upload_to = f'images/{self.place.name}/'
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"Image for {self.place.name}"
    

# Resturant Model
class Resturant(models.Model):
    place = models.ForeignKey(Place, related_name='resturants', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    cuisine_type = models.CharField(max_length=100, blank=True, null=True)
    opening_hours = models.CharField(max_length=100, blank=True, null=True)
    contact_info = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)


    def __str__(self):
        return f"{self.name} - {self.place.name}"
    

#Activity Model
class Activity(models.Model):
    place = models.ForeignKey(Place, related_name='activities', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    activity_type = models.CharField(max_length=255)
    duration = models.CharField(max_length=255, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    

    def __str__(self):
        return f"{self.name} - {self.place.name}"
    


# Trip Model
class Trip(models.Model):
    user = models.ForeignKey(User, related_name='trips', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    place = models.ForeignKey(Place, related_name='trips', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} by {self.user}"

# Day Plan Model
class DayPlan(models.Model):
    trip = models.ForeignKey(Trip, related_name='day_plans', on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Day {self.date} of {self.trip.name}"

# Activity Plan Model
class ActivityPlan(models.Model):
    day_plan = models.ForeignKey(DayPlan, related_name='activity_plans', on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, related_name='activity_plans', on_delete=models.CASCADE)
    start_time = models.TimeField()
    duration = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.activity.name} on {self.day_plan.date}"

# Restaurant Visit Model
class RestaurantVisit(models.Model):
    day_plan = models.ForeignKey(DayPlan, related_name='restaurant_visits', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Resturant, related_name='restaurant_visits', on_delete=models.CASCADE)
    time = models.TimeField()

    def __str__(self):
        return f"{self.restaurant.name} on {self.day_plan.date}"




# Demo Plan
class Demo(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name}"
    

class Plan(models.Model):
    Startdate = models.DateField()
    duration = models.CharField(max_length=100)
    name = models.ForeignKey(Demo, related_name='demo', on_delete= models.CASCADE)
    activitys = models.IntegerField()

    def __str(self):
        return f"{self.Startdate} for {self.duration}"
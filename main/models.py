from django.db import models

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

    def __str__(self):
        return self.name
    

#Place Image Modles

class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='places/images/')
    

    def save(self, *args, **kwargs):
        #Ensure the directory structure is created based on the place name

        if self.place:
            self.image.field.upload_to = f'images/{self.place.name}/'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.place.name}"
    


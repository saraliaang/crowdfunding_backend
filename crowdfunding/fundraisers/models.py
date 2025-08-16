from django.db import models

# Create your models here.
class Fundraiser(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    destination_year = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)

# other attributes: 
# speed(auto conversion), goal (auto conversion) 
# set when the destination year

# current_speed, current_total_pledge
# auto update when the destination year



class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    fundraiser = models.ForeignKey(
        'Fundraiser',
        related_name = 'pledges',
        #this name has to match the one inside the serializer
        on_delete=models.CASCADE
        #if you delete the fundraiser, the pledges also got deleted
    )
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


# Create your models here.
class Fundraiser(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    destination_year = models.IntegerField()
    target = models.DecimalField(max_digits=12, decimal_places=2, editable=False)  
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        related_name='owned_fundraisers',
        on_delete=models.CASCADE
    )

    def save(self, *arg, **kwargs):
        if self.destination_year and not self.target:
            year_diff = datetime.now().year - self.destination_year
            self.target = year_diff*10000
        super().save(*arg, **kwargs)

    @property 
    def amount_raised(self):
        return self.pledges.aggregate(models.Sum('amount'))['amount__sum'] 

    @property
    def total_lightyear(self):
        return 1+float(self.target)*5e-7
    @property
    def current_lightyear(self):
        return self.pledges.aggregate(total=models.Sum('amount'))['total'] or 0


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

    supporter = models.ForeignKey(
        get_user_model(),
        related_name = 'pledges',
        on_delete=models.CASCADE

    )


#when anonymous is false, need to show real name?
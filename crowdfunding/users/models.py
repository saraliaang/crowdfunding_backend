from django.db import models
from django.contrib.auth.models import AbstractUser
#AbstractUSer means it's purly for inheretance, not to create a concrete instance



class CustomUser(AbstractUser):
    
    def __str__(self):
        return self.username
from django.db import models

# Create your models here.

class Profile(models.Model):

    first_name = models.CharField(max_length=255, help_text='Enter your first name')
    last_name = models.CharField(max_length=255, help_text='Enter your last name')

    def __str__(self):
        return self.first_name


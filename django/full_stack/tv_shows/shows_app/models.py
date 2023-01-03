from django.db import models
from datetime import datetime
import re

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['title']) < 2:
            errors['title'] = 'Title must be at least 2 characters'

        if len(postData['network']) < 3:
            errors['network'] = 'Network must be at least 3 characters'

        if len(postData['description']) < 10 and len(postData['description']) >= 1:
            errors['description'] = 'Description must be at least 10 characters'

        if datetime.strptime(postData['release_date'], '%Y-%m-%d') >= datetime.now():
            errors['release_date'] = 'Release date must be before now'

        # in case any email comes in in the future
        # EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
        #     errors['email'] = "Invalid email address!"

        return errors


# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
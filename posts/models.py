from django.db import models

# Create your models here.

class User(models.Model):
    """User model"""

    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 50)

    firs_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank = True)

    birthdate = models.DateField(blank = True, null=True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True )

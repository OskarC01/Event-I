from django.db import models

from user.models import CustomUser


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(
        max_length=255, blank=False, unique=False, null=False)
    last_name = models.CharField(
        max_length=255, blank=False, unique=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=True)
    birth_date = models.DateField(null=True, blank=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Location(models.Model):
    name = models.CharField(max_length=255, blank=False,
                            unique=True, null=False)
    address = models.CharField(
        max_length=255, blank=False, null=True, unique=True)
    email = models.EmailField(max_length=255, blank=False, null=True)
    phone = models.CharField(max_length=255, blank=False, null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(blank=True, default='')
    manager = models.ForeignKey(
        UserProfile, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Event(models.Model):
    AGE_RESTRICTION = (
        ('16+', '16+'),
        ('18+', '18+'),
        ('21+', '21+'),
        ('No age restriction', 'No age restriction'),
    )
    EVENT_TYPE = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
        ('Mixed', 'Mixed'),
    )
    title = models.CharField(max_length=255, blank=False,
                            unique=True, null=False)
    date = models.DateTimeField(blank=False, null=True)
    description = models.TextField(blank=True, null=False, default='')
    image = models.ImageField(upload_to='images/', blank=True)
    location = models.ForeignKey(
        Location, blank=False, on_delete=models.SET_NULL, null=True)
    is_favorite = models.BooleanField(default=False)
    event_type = models.CharField(
        max_length=255, choices=EVENT_TYPE, blank=False, null=True)
    age_restriction = models.CharField(
        max_length=255, choices=AGE_RESTRICTION, blank=False, null=True)
    entry_fee = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)
    maximum_participants = models.IntegerField(default=100, blank=False)
    creator = models.ForeignKey(
        UserProfile, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

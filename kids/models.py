
from django.db import models

# Create your models here.
class Kids(models.Model):
    kid_name = models.CharField(max_length=100, null=False, blank=False)
    kid_age = models.IntegerField(null=False, blank=False)
    parent_phone_number = models.CharField(max_length=12, null=False, blank=False)
    parent_email_address = models.EmailField(null=False, blank=False)

    def __str__(self):
        return self.kid_name


class Image(models.Model):
    CHOICES = (
        ('FRUIT', 'Fruit'),
        ('VEGETABLE', 'Vegetable'),
        ('GRAIN', 'Grain'),
        ('DAIRY', 'Dairy'),
        ('PROTIEN', 'Protien'),
        ('UNKNOWN', 'Unknown')
    )
    kid = models.ForeignKey(Kids, on_delete=models.CASCADE, null=False, blank=False)
    image_url = models.URLField(null=False, blank=False)
    created_on = models.DateTimeField(null=False, blank=False, auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(null=False, blank=False)
    is_approved = models.BooleanField(default=False, null=False, blank=False)
    approoved_by = models.CharField(max_length=100, null=False, blank=False)
    food_group = models.CharField(choices=CHOICES, default='UNKNOWN', max_length=15)

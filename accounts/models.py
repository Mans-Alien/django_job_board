from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def profile_image(instance, filename):
    imagename, extention = filename.split(".")
    return f"profile/{instance.user.id}/{instance.user.username}.{extention}"

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to=profile_image)
    city = models.ForeignKey("City", related_name="user_city", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username


#signal to create an empty profile
@receiver(post_save, sender= User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) 


class City(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
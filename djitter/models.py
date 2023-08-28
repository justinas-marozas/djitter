from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # type: ignore
    follows = models.ManyToManyField(  # type: ignore
        'self',
        related_name='followed_by',
        symmetrical=False,
        blank=True,
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender: User, instance: User, created: bool, **_):
    if not created:
        return
    user_profile = Profile(user=instance)
    user_profile.save()
    user_profile.follows.add(user_profile)
    user_profile.save()

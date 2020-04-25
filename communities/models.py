from django.db import models as models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from . import subcommunities.models.SubCommunity


class Community(models.Model):
    name = models.CharField(max_length=150,)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # subcomms = models.ForeignKey(to=SubCommunity, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

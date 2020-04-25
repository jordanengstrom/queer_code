from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from communities

class SubCommunity(models.Model):
    name = models.CharField(max_length=150,)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # community = models.ForeignKey(to=Community, on_delete=models.DO_NOTHING)

    def __str__(self): 
        return self.name

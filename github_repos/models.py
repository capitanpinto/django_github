import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models


class Repository(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1) and self.pub_date <= timezone.now()
        was_published_recently.admin_order_field = 'question_text'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'

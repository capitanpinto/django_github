import datetime
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
from django.db import models

def validate_github(value):
    if not ("github" in value):
        raise ValidationError(_("repository must be from github"), params={"value":value},)
def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
class Repository(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200, validators=[validate_github])
    created_at = models.DateTimeField(default=timezone.now)
    even_field = models.IntegerField(validators=[validate_even], default=0)

    def __str__(self):
        return self.name

    def validate_github(value):
        if not ("github" in value):
            raise ValidationError(_("repository must be from github"), params={"value":value},)

    def validate_even(value):
        if value % 2 != 0:
            raise ValidationError(
                _('%(value)s is not an even number'),
                params={'value': value},)
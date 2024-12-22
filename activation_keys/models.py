from django.db import models

# Create your models here.


class Key(models.Model):
    activation_key = models.CharField(max_length=200, unique=True)
    account = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"key:{self.activation_key}, account:{self.account}"

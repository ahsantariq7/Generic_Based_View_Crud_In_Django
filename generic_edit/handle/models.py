from django.db import models
from django.urls import reverse

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=200)
    no=models.IntegerField()
    
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    
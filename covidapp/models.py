from django.db import models
from django.urls import reverse
import datetime

# Create your models here.

class Hospital(models.Model):
    date_time 			=    	models.DateField()
    hospital_currently 	= 		models.TextField(blank=True)
    icucurrently		= 		models.TextField(blank=True)
    hospital_increase 	= 		models.TextField(blank=True)
    dead_daily			= 		models.TextField(blank=True)
    tested_today		=		models.TextField(blank=True)
    

    def get_absolute_url(self):
    	return reverse("hospital-list", kwargs={"id": self.id}) 
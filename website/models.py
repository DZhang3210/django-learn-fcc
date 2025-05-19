from django.db import models


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	first_name = models.CharField(max_length=50, null=True)
	last_name =  models.CharField(max_length=50, null=True)
	email =  models.CharField(max_length=100, null=True)
	phone = models.CharField(max_length=15, null=True)
	address =  models.CharField(max_length=100, null=True)
	city =  models.CharField(max_length=50, null=True)
	state =  models.CharField(max_length=50, null=True)
	zipcode =  models.CharField(max_length=20, null=True)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
from django.db import models
from .ClientModel import ClientModel

class SalesModel(models.Model):
  sale_id = models.IntegerField(primary_key=True, blank=False, null=False)
  client_id = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
  date = models.DateField(null=False, blank=False)
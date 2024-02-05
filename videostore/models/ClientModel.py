from django.db import models

class ClientModel(models.Model):
  client_id = models.IntegerField(primary_key=True, blank=False, null=False)
  name = models.CharField(max_length=255, null=False, blank=False)
  cpf = models.IntegerField(max_length=11, unique=True, null=False, blank=False)
  birthday = models.DateField(null=False, blank=False)
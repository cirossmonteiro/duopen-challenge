from django.core.validators import MinLengthValidator
from django.db import models


class Item(models.Model):
    id = models.CharField(max_length=36, validators=[MinLengthValidator(36)], primary_key=True)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()


class Account(models.Model):
    id = models.CharField(max_length=36, validators=[MinLengthValidator(36)], primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

class Transaction(models.Model):
    id = models.CharField(max_length=36, validators=[MinLengthValidator(36)], primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    # description = models.CharField(max_length=100)
    # currencyCode = models.CharField(max_length=3)
    # amount = models.FloatField()
    # date = models.DateTimeField()
    # category = models.CharField(max_length=100)
    # categoryId = models.CharField(max_length=100)


class User(models.Model):
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    age = models.PositiveSmallIntegerField()
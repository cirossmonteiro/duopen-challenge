from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

class Item(models.Model):
    id = models.CharField(max_length=36, validators=[MinLengthValidator(36)], primary_key=True)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    connector = models.JSONField()
    clientUserId = models.CharField(max_length=100)


class Account(models.Model):
    class AccountType(models.TextChoices):
        BANK = "BANK", _("BANK")
        CREDIT = "CREDIT", _("CREDIT")

    class AccountSubtype(models.TextChoices):
        CHECKING_ACCOUNT = "CHECKING_ACCOUNT", _("CHECKING_ACCOUNT")
        SAVINGS_ACCOUNT = "SAVINGS_ACCOUNT", _("SAVINGS_ACCOUNT")
        CREDIT_CARD = "CREDIT_CARD", _("CREDIT_CARD")

    id = models.CharField(max_length=36, validators=[MinLengthValidator(36)], primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    accountType = models.CharField(max_length=6, choices=AccountType)
    subtype = models.CharField(max_length=16, choices=AccountType)
    number = models.CharField(max_length=100)
    balance = models.FloatField()
    taxNumber = models.CharField(max_length=100, null=True)
    marketingName = models.CharField(max_length=100)
    owner = models.CharField(max_length=100, null=True)
    bankData = models.JSONField(null=True)
    creditData = models.JSONField(null=True)

class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        DEBIT = "DEBIT", _("DEBIT")
        CREDIT = "CREDIT", _("CREDIT")
    id = models.CharField(max_length=36, validators=[MinLengthValidator(36)], primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    date = models.DateTimeField()
    merchant = models.JSONField(null=True)
    description = models.CharField(max_length=100)
    currencyCode = models.CharField(max_length=3)
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    categoryId = models.CharField(max_length=100)
    transactionType = models.CharField(max_length=6, choices=TransactionType)

class User(models.Model):
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    age = models.PositiveSmallIntegerField()
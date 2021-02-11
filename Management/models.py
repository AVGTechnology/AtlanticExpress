from django.db import models
from django.shortcuts import redirect

from django.utils.crypto import get_random_string

# Create your models here.
dis = " package content is a Box... "


# Create logistics
class Logistic(models.Model):
    trackId = models.CharField(primary_key=True, default=get_random_string(10, 'ABED-0123456789'),
                               max_length=20, )
    sender = models.CharField(verbose_name="Sender Full name", max_length=50, null=False)
    sender_email = models.EmailField(verbose_name="Sender Email", max_length=225, null=False)
    sender_contact = models.CharField(verbose_name="Sender contact", max_length=30, null=False)
    origin = models.CharField(verbose_name="Origin", max_length=225, null=False, blank=False, default="none")
    Paid = models.CharField(verbose_name="sender paid", max_length=30, null=False)

    recipient = models.CharField(verbose_name="Recipient Full name", max_length=50, null=False)
    recipient_email = models.EmailField(verbose_name="Recipient Email", max_length=225, null=False)
    recipient_contact = models.CharField(verbose_name="Recipient contact", max_length=30, null=False)
    destination = models.CharField(verbose_name="Destination", max_length=225, null=False, blank=False, default="none")
    mode = models.CharField(verbose_name="Mode of transit", max_length=50, null=False, default='Air')

    item_des = models.TextField(verbose_name="Item Description", max_length=225, null=False, default=dis)
    weight = models.CharField(verbose_name="Physical Weight", max_length=50, null=False)
    date = models.DateField(verbose_name="Issued Date", max_length=50, null=False, auto_now_add=True)
    timestap = models.TimeField(auto_now_add=True)
    delivery_date = models.DateField()

    class Meta:
        ordering = ['timestap']

    def __str__(self):
        return '{} {} to {}'.format(self.trackId, self.sender, self.recipient)


class Location(models.Model):
    logistic = models.ForeignKey(Logistic, on_delete=models.CASCADE, )
    point = models.CharField(max_length=225, verbose_name="Clearance Event", null=False)
    Location = models.CharField(max_length=225, verbose_name="Location", null=False)
    timestap = models.TimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '{} {} '.format(self.logistic, self.date)


class PaymentAccount(models.Model):
    Acc_name = models.CharField(verbose_name="Account Name", max_length=50, null=False)
    Acc_number = models.CharField(max_length=30, verbose_name="Account Number", null=False)
    bank = models.CharField(max_length=50, verbose_name="Bank", null=False)

    def __str__(self):
        return '{} , {} , Account Number: {}'.format(self.Acc_name, self.bank, self.Acc_number)


class BillClient(models.Model):
    logistic = models.ForeignKey(Logistic, verbose_name="client", on_delete=models.CASCADE)
    account = models.ForeignKey(PaymentAccount, verbose_name="Choose Pay Account", on_delete=models.CASCADE)
    bill_dis = models.TextField(max_length=225, verbose_name="Bill Description", null=False)
    Amount = models.CharField(max_length=50, verbose_name="Total Amount", null=False)

    def __str__(self):
        return '{} ({}) '.format(self.logistic, self.Amount)


class Info(models.Model):
    website = models.CharField(max_length=50, verbose_name="Website", null=True, blank=True)
    contact = models.CharField(max_length=50, verbose_name="Contact", null=True, blank=True)
    address = models.CharField(max_length=50, verbose_name="Address", null=True, blank=True)
    email = models.CharField(max_length=50, verbose_name="Email", null=True, blank=True)

    def __str__(self):
        return '{} ({}) '.format(self.website, self.contact)

from django.contrib import admin
from django.shortcuts import redirect

from .models import Logistic, Location, PaymentAccount, BillClient, Info

# Register your models here.
# admin.site.register(Logistic)

admin.site.register(Info)
admin.site.register(BillClient)


@admin.register(Logistic)
class LogisticAdmin(admin.ModelAdmin):
    def response_add(self, request, obj, post_url_continue=None):
        return redirect('invoices')

    def response_change(self, request, obj, post_url_continue=None):
        return redirect('invoices')


admin.site.register(Location)


@admin.register(PaymentAccount)
class PaymentAccountAdmin(admin.ModelAdmin):
    def response_add(self, request, obj, post_url_continue=None):
        return redirect('dashboard')

    def response_change(self, request, obj, post_url_continue=None):
        return redirect('dashboard')

from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path("management/dashboard/", views.dashboard, name='dashboard'),
    path("management/logistic_list/", views.logistic_list, name='logistic_list'),
   # path("management/logistic_form/", views.logistic_form, name='logistic_form'),
    path("management/location_form/(<trackId>\d+)/", views.location_form, name='location_form'),
    path("management/bill_form/(<trackId>\d+)/", views.bill_form, name='bill_form'),
   # path("management/payment_form/", views.payment_account_form, name='payment_account_form'),
    path("management/logistic_invoice/", views.quick_invoice, name='quick_invoice'),
    path("management/invoices/", views.invoices, name='invoices'),
    path("management/invoice/details/(<trackId>\d+)/", views.invoices_details, name='invoices_details'),

    path("management/bills/", views.bill_client, name='bill_client'),
    path("management/bill/details/(<trackId>\d+)/", views.bill_details, name='bill_details'),

    path("management/logistic_details/(<trackId>\d+)/", views.logistic_details, name='logistic_details'),
    path("management/logistic_send_invoice/(<trackId>\d+)/", views.send_invoice, name='send_invoice'),
    path("management/logistic_send_bill/(<trackId>\d+)/", views.send_bill, name='send_bill'),
]

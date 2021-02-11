from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.template.defaultfilters import last

from Omoh_Shiping.settings import EMAIL_HOST_USER
from django.shortcuts import render, redirect
from .models import Logistic, PaymentAccount, Location, BillClient
from .forms import LocationUpdateForm, ClientBillForm
from .utils import render_to_pdf
from django.template.loader import render_to_string, get_template


# Create your views here.
@login_required
def dashboard(request):
    logistics = Logistic.objects.all()
    new_logistics = Logistic.objects.all().order_by("-date")[:5]
    pay_acc = PaymentAccount.objects.all()
    billed_client = BillClient.objects.all()
    return render(request, "dashboard.html", {
        "logistics": logistics,
        "new_logistics": new_logistics,
        "pay_acc": pay_acc,
        "billed_client": billed_client
    })


@login_required
def logistic_list(request):
    logistics = Logistic.objects.all().order_by("-date")
    return render(request, "logistic_list.html", {
        "logistics": logistics,
    })


@login_required
def logistic_details(request, trackId):
    logistics = Logistic.objects.get(trackId=trackId)
    location = Location.objects.all().filter(logistic__trackId=trackId)
    return render(request, "logistic_details.html", {
        "logistics": logistics,
        "location": location,
    })


@login_required
def location_form(request, trackId):
    form = LocationUpdateForm(request.POST)
    logistics = Logistic.objects.get(trackId=trackId)
    form.instance.logistic = logistics
    if form.is_valid():
        form.save()
        return redirect('logistic_details', trackId)
    else:
        form = LocationUpdateForm(request.POST)
    return render(request, 'locationUpdateForm.html', {"form": form, })


@login_required
def quick_invoice(request):
    logistic = Logistic.objects.all().first()
    return render(request, 'quick_invoice.html', {"logistic": logistic, })


@login_required
def send_invoice(request, trackId):
    logistic = Logistic.objects.get(trackId=trackId)
    # pdf_invoice = render_to_pdf('pdf/quick_invoice.html', {"logistic": logistic, })
    message = get_template('pdf/quick_invoice.html').render({"logistic": logistic, })
    email = EmailMessage()
    email.subject = "Atlantic Global Express Delivery "
    email.body = message
    email.from_email = EMAIL_HOST_USER
    email.to = [logistic.recipient_email, logistic.sender_email]
    email.content_subtype = "html"
    email.send()
    return redirect("dashboard")


@login_required
def bill_form(request, trackId):
    form = ClientBillForm(request.POST)
    logistics = Logistic.objects.get(trackId=trackId)
    form.instance.logistic = logistics
    if form.is_valid():
        form.save()
        return redirect('bill_details', trackId)
    else:
        form = ClientBillForm(request.POST)
    return render(request, 'billForm.html', {"form": form, })


@login_required
def bill_details(request, trackId):
    bill = BillClient.objects.get(logistic__trackId=trackId)
    billLog = Logistic.objects.get(trackId=trackId)
    location = Location.objects.all().filter(logistic__trackId=trackId).first()
    return render(request, 'bill_details.html', {"bill": bill,
                                                 "billLog": billLog,
                                                 "location": location, })


@login_required
def bill_client(request,):
    bill = BillClient.objects.all()
    return render(request, 'bill_client.html', {"bill": bill,
                                              })


@login_required
def send_bill(request, trackId):
    bill = BillClient.objects.get(logistic__trackId=trackId)
    billLog = Logistic.objects.get(trackId=trackId)
    location = Location.objects.all().filter(logistic__trackId=trackId).first()

    message = get_template('pdf/bill_details.html').render({"bill": bill,
                                                            "billLog": billLog,
                                                            "location": location, })
    email = EmailMessage()
    email.subject = "Atlantic Global Express Delivery Bill For  " + billLog.recipient
    email.body = message
    email.from_email = EMAIL_HOST_USER
    email.to = [billLog.recipient_email, ]
    email.content_subtype = "html"
    email.send()
    return redirect("dashboard")


def invoices(request):
    logistics = Logistic.objects.all().order_by("-date")
    return render(request, 'invoices.html', {"logistics": logistics, })


def invoices_details(request,trackId):
    logistic = Logistic.objects.get(trackId=trackId)
    return render(request, 'invoices_details.html', {"logistic": logistic, })

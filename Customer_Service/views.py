from django.shortcuts import render
from Management.models import Logistic, Location,Info
from django.db.models.functions import TruncMonth

# Create your views here.


def index(request):
    info = Info.objects.get(id=1)
    return render(request, "index.html", {'info': info})


def track_id(request):
    track = request.GET.get('trackId')
    logistics = Logistic.objects.get(pk=track)
    location = Location.objects.all().filter(logistic__trackId=track).order_by('-timestap')
    info = Info.objects.get(id=1)
    return render(request, "Logistic_detail.html", {"logistics": logistics,
                                                    "location": location,
                                                    'info': info
                                                    })

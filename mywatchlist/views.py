from django.shortcuts import render
from mywatchlist.models import ItemWatchlist
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_watchlist(request):
    watchlistdata = ItemWatchlist.objects.all()
    ddata = {'items' : watchlistdata,
     "Name" : "Halomoan Geraldo",
      "NPM" : "2106720885"}
    return render(request, "mywatchlist.html", ddata)

def show_xml(request):
    data = ItemWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ItemWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalogue(request):
    cataloguedata = CatalogItem.objects.all()
    ddata = {'items' : cataloguedata,
     "Name" : "Halomoan Geraldo",
      "NPM" : "2106720885"}
    return render(request, "katalog.html", ddata)
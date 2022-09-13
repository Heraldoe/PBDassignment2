from django.shortcuts import render

# TODO: Create your views here.
def show_catalogue(request):
    return render(request, "katalog.html")
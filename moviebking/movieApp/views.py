from django.shortcuts import render
from .models import Movie
from .models import Carosel
# Create your views here.
def home(req):
    obj=Movie.objects.all()
    obj2=Carosel.objects.all()
    return render(req,'index.html',{"result":obj,"Carosel":obj2})
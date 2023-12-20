from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import Furniture



def index(request):
    latest_furniture = Furniture.objects.all()
    furniture = Furniture.objects.all()
    ident = True

    
    return render(request, 'furniture/list.html', {'latest_furniture' : latest_furniture, 'Furniture' : furniture, 'ident' : ident})
    
        




def detail(request, furniture_id):
    try:
        a = Furniture.objects.get(id = furniture_id)
    except:
        raise Http404("Not found")
        
    return render(request, 'furniture/detail.html', {'furniture': a})
    

    


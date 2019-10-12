from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image , Location ,Category

# Create your views here.

def index(request):
    images = Image.objects.all()
    # locations = Location.objects.all()
    categories = Category.objects.all()
    
    return render(request,'index.html',{'images':images,'categories':categories})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all_Photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_Photos/search.html',{"message":message})



def filter_location(request, location):

    # try:
    location = Location.objects.get(id = location_id)
    images = Image.objects.filter(location = location.id).all()
    # except ValueError:
    #     # Raise 404 error when ValueError is thrown
    #     raise Http404()
    #     assert False

    return render(request, 'all_Photos/location.html', {"locations": location,'images':images})



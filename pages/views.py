from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor

# Create your views here.

def index(request):
    # who only 3 listing on the main page, with is published flagged
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }

    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    # dictionary to hold our method created above
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    # Get seller of month, has the mvp checkmark
    # pass our context as 3rd parameter
    return render(request, 'pages/about.html', context)
from django.shortcuts import render
from listings.models import agents

# Create your views here.
def index( request):
    context = agents.objects.all()
    return render(request, 'index.html', {'context':context})


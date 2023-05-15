from django.shortcuts import render
from .models import governer

# Create your views here.

def governers_index(request):
    members = governer.objects.all()
    context = {
        'members': members
    }
    return render(request, 'governers_index2.html', context)


def full_view(request, pk):
    member = governer.objects.get(pk=pk)
    context = {
        'member': member
    }
    return render(request, 'full_view.html', context)    

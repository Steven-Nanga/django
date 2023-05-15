from django.shortcuts import render
from .models import board

# Create your views here.

def board_index(request):
    members = board.objects.all()
    context = {
        'members': members
    }
    return render(request, 'index.html', context)


def full_view(request, pk):
    member = board.objects.get(pk=pk)
    context = {
        'member': member
    }
    return render(request, 'full_view.html', context)    

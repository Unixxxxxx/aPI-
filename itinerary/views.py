from django.shortcuts import render

def kedarnath(request):
    return render(request, 'itinerary/index.html', {})


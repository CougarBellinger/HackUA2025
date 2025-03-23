from django.shortcuts import render

# Create your views here.
def travel_question(request):
    return render(request, 'travel_buddy/travel_question.html')

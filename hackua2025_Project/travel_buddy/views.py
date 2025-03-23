from django.shortcuts import render
from django.conf import settings
from openai import OpenAI
import openai
from .utils import openai_client

# Create your views here.
def travel_question(request):

    question = "When do you want to travel?"
    answers = ["Spring", "Summer", "Next Month"]

    context = {
        "question": question,
        "answers": answers
    }
    return render(request, 'travel_buddy/travel_question.html', context)

def mood(request):
    moods = ["Relaxed", "Adventurous", "Inspired", "Pampered", "Connected", "Knowledgeable", "Artistic"]  # Hardcoded moods
    return render(request, 'travel_buddy/mood.html', {'moods': moods})

# Return "Prompt/'Get Itinerary'"

def itinerary_result_view(request):

    openai.api_key = settings.OPENAI_API_KEY
    client =openai_client.OpenAIClient()
    destination = 'Somewhere in Oceania'
    travel_type = 'Adventure'
    time = '1 week'
    rules = 'Try to keep costs low and provide booking links'

    itinerary_text = client.get_itinerary(destination, travel_type, time, rules)
    # Render the result in a template
    return render(request, 'travel_buddy/itinerary_result.html', {
        'itinerary': itinerary_text
    })

def other_textbox(request):
    return render(request, 'travel_buddy/other_textbox.html')
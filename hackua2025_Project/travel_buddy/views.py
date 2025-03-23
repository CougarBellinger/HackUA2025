from django.shortcuts import render
from django.conf import settings
from openai import OpenAI
import openai
from .utils import openai_client

# Create your views here.
def travel_question(request):
    # Define the questions
    questions = {
        "travel_time": {
            "question": "When do you want to travel?",
            "answers": ["Spring", "Summer", "Next Month"],
            "next": "destination",  # The next question to redirect to
        },
        "destination": {
            "question": "Where do you want to travel?",
            "answers": ["Europe", "Asia", "Oceania"],
            "next": None,  # No next question, this is the last one
        },
    }

    # Get the current question from the request or default to the first question
    question_id = request.GET.get("question_id", "travel_time")

    # If the question doesn't exist, redirect to the first question
    if question_id not in questions:
        return redirect(f"/questions/?question_id={next_question}")


    question_data = questions[question_id]

    # Retrieve previous answers from session
    selected_answers = request.session.get("selected_answers", {})

    if request.method == "POST":
        selected_answer = request.POST.get("answer")
        selected_answers[question_id] = selected_answer
        request.session["selected_answers"] = selected_answers  # Save in session

        # Redirect to the next question
        next_question = question_data["next"]
        if next_question:
            return redirect(f"/questions/?question_id={next_question}")
        else:
            return redirect("mood")  # Redirect to a summary or final page

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
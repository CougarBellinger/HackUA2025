from django.shortcuts import render, redirect
from django.conf import settings
from django.utils.translation.template import context_re
from openai import OpenAI
import openai
from .utils import openai_client

# Create your views here.
def travel_question(request):
    # Define the questions
    questions = {
        "travel_personality": {
            "question": "When you travel, are you more likely to...",
            "answers": ["Plan every detail meticulously", "Have a general idea but leave room for spontaneity", "Completely wing it and see where the wind takes me", "Follow recommendations and tips from locals or travel resources"],
            "next":"perfect_day"
        },
        "perfect_day": {
            "question": " Imagine your perfect travel day. Would it involve...",
            "answers": ["Exploring bustling city streets and iconic landmarks", "Relaxing on a beautiful beach or by a serene lake", "Hiking through nature and discovering hidden gems", "Immersing yourself in local culture and traditions"],
            "next":"travel_vibe"
        },
        "travel_vibe": {
            "question": "What's your ideal travel vibe? Are you looking for something that feels...",
            "answers": ["Adventurous and exciting", "Peaceful and rejuvenating", "Authentic and insightful", "Fun and social"],
            "next":"souvenir"
        },
        "souvenir": {
            "question": "If you could bring only one type of souvenir back from a trip, what would it most likely be?",
            "answers": ["Something practical and useful", "A beautiful piece of art or craftsmanship", "A unique local food or drink", "Photos and memories"],
            "next": "with_who"
        },
        "with_who": {
            "question": "Who are you most likely to be traveling with on this trip?",
            "answers": ["Traveling solo", "Traveling with a partner", "Traveling with family", "Traveling with friends or group"],
            "next": "duration"
        },
        "duration": {
            "question": "What would you like the duration of your trip to be?",
            "answers": ["Weekend Getaway (1-3 days)", "Short Escape (4-6 days)", "Week-Long Adventure (7-10 days)", "Extended Journey (11+ days)"],
            "next": "budget"
        },
        "budget": {
            "question": "What is your budget for this trip?",
            "answers": ["Shoestring Explorer ($ - Budget-friendly travel, save every penny!)", "Comfort Seeker ($$ - A balance of affordability and convenience)", "Luxury Adventurer ($$$ - Treat yourself to some premium experiences)", "VIP Globetrotter ($$$$ - No expense spared, live your best life!)"],
            "next": ""
        }
    }

    # Get the current question from the request or default to the first question
    question_id = request.GET.get("question_id", "travel_personality")

    # If the question doesn't exist, redirect to the first question
    if question_id not in questions:
        return redirect(f"/questions/?question_id=travel_personality")


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
            return redirect("itinerary_result_view")  # Redirect to a summary or final page

    context = {
        "question_id": question_id,
        "question":question_data["question"],
        "answers":question_data["answers"],
        "selected_answer":selected_answers.get(question_id,None)
    }

    return render(request, "travel_buddy/travel_question.html", context)

def mood(request):
    moods = ["Relaxed", "Adventurous", "Inspired", "Pampered", "Connected", "Knowledgeable", "Artistic"]  # Hardcoded moods
    return render(request, 'travel_buddy/mood.html', {'moods': moods})

def home(request):
    return render(request, 'travel_buddy/home.html')
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
from django.shortcuts import render

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

def other_textbox(request):
    return render(request, 'travel_buddy/other_textbox.html')
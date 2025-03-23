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

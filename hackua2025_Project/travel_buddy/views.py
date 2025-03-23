from django.shortcuts import render, redirect


# Create your views here.
def travel_question(request):
    # Define the questions
    questions = {
        "travel_time": {
            "question": "When do you want to travel?",
            "answers": ["Spring", "Summer", "Next Month"],
            "next": "destination_question",  # The next question to redirect to
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
        return redirect(f"?question_id=travel_time")

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
            return redirect(f"?question_id={next_question}")
        else:
            return redirect("mood")  # Redirect to a summary or final page

    context = {
        "question_id": question_id,
        "question": question_data["question"],
        "answers": question_data["answers"],
        "selected_answer": selected_answers.get(question_id, None),
    }
    return render(request, "travel_buddy/travel_question.html", context)

def mood(request):
    print(request.session["selected_answers"])
    moods = ["Relaxed", "Adventurous", "Inspired", "Pampered", "Connected", "Knowledgeable", "Artistic"]  # Hardcoded moods
    return render(request, 'travel_buddy/mood.html', {'moods': moods})


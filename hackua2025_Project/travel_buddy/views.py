from django.shortcuts import render, redirect


# Create your views here.
def travel_question(request):
    question = "When do you want to travel?"
    answers = ["Spring", "Summer", "Next Month"]
    question_id="travel"

    selected_answers = request.session.get("selected_answers", {})
    print(selected_answers)

    if request.method == "POST":
        selected_answer = request.POST.get("answer")
        selected_answers[question_id] = selected_answer
        request.session["selected_answers"] = selected_answers
        return redirect("relationship_question")

    context = {
        "question": question,
        "answers": answers,
        "selected_answer": request.session.get("selected_answer", None)
    }

    return render(request, 'travel_buddy/travel_question.html', context)

def relationship_question(request):
    question = "Who you travelling with?"
    question_id = "relationship"
    answers = ["Solo", "Bae", "Buddies"]

    selected_answers = request.session.get("selected_answers", {})
    print(selected_answers)

    if request.method == "POST":
        selected_answer = request.POST.get("answer")
        selected_answers[question_id] = selected_answer
        request.session["selected_answers"] = selected_answers
        return redirect("relationship_question")  # Reloads the page to show selection

    context = {
        "question": question,
        "question_id" : question_id,
        "answers": answers,
        "selected_answer": request.session.get("selected_answer", None)
    }

    return render(request, 'travel_buddy/travel_question.html', context)

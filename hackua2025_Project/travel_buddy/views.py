from django.shortcuts import render, redirect

# A simple list of questions with their available options.
QUESTIONS = [
    {
        'question': "What type of travel experience are you wanting to plan?",
        'options': ['Family-Friendly', 'Professional', 'Roamntic']
    },
    {
        'question': "Do you prefer domestic or international destinations?",
        'options': ['Domestic', 'International']
    },
    {
        'question':"Are you an early riser or night owl?",
        'options':['Early riser','Night owl']
    }
    # Add additional questions as needed.
]

def travel_questions(request):
    # Retrieve current step from session; default to 0 if not set.
    current_step = request.session.get('current_step', 0)

    if request.method == 'POST':
        # Capture the answer from the submitted form.
        answer = request.POST.get('answer')
        # Save the answer in session or database as needed.
        answers = request.session.get('answers', [])
        answers.append(answer)
        request.session['answers'] = answers
        
        # Move to the next question.
        current_step += 1
        request.session['current_step'] = current_step

        # If no more questions, redirect to a results page or summary.
        if current_step >= len(QUESTIONS):
            return redirect('result_page')

    # Render the current question as a card.
    if current_step < len(QUESTIONS):
        question_data = QUESTIONS[current_step]
        return render(request, 'question_page.html', {'question_data': question_data})

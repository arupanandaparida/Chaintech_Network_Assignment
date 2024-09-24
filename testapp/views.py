from django.shortcuts import render
import datetime
import random

quotes = [
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "An unexamined life is not worth living.",
    "Your time is limited, don't waste it living someone else's life."
]

def home(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_quote = random.choice(quotes)
    return render(request, 'testapp/base.html', {
        'current_time': current_time,
        'random_quote': random_quote
    })
from .forms import UserInfoForm
from .models import UserSubmission

def submit_info(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            UserSubmission.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email']
            )
            return render(request, 'testapp/submission_success.html', {'name': form.cleaned_data['name']})
    else:
        form = UserInfoForm()
    return render(request, 'testapp/submit_info.html', {'form': form})
def view_submissions(request):
    submissions = UserSubmission.objects.all()
    return render(request, 'testapp/view_submissions.html', {'submissions': submissions})

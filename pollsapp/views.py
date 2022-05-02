from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreatePollForm
from .models import Poll, Choice


# Create your views here.
def home(request):
    polls = Poll.objects.all()
    choices = Choice.objects.all()
    context = {
        'polls': polls,
        'choices': choices
    }
    return render(request,'poll/home.html', context)


def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = CreatePollForm()

    context = {'form' : form}
    return render(request, 'poll/create.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            print(request.POST)
            poll.option_one_count += 1
        elif selected_option == 'option2':
            print(request.POST)
            poll.option_two_count  += 1
        elif selected_option == 'option3':
            print(request.POST)
            poll.option_three_count += 1
        elif selected_option == 'option4':
            print(request.POST)
            poll.option_four_count += 1

        else:
            return HttpResponse(400, 'Invalid form option')
    
        poll.save()

        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'poll/vote.html', context)



def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'poll/results.html', context)


from django.shortcuts import render
from charative.models import Chara
from django.shortcuts import redirect
from django.contrib.auth.models import User
from charative.forms import MatchingQuestions


def index(request):

    poop, made = Chara.objects.get_or_create(name="Midas")
    print(poop.name)
    context = {}
    context['poop'] = poop

    return render(request, 'index.html', context)


def indexredirect(request):

    return redirect('index')


def edituser(request):

    if request.method == 'POST':

        form = MatchingQuestions(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('index')
        else:
            pass
    else:
        form = MatchingQuestions(instance = request.user)

    return render(request, 'edituser', {'form':form})

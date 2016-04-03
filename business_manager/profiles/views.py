from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def create_user(request):
    form = UserCreationForm()
    return render(request,
                  'profiles/profile_create_user.html',
                  {'form': form})

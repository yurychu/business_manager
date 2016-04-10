from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Purpose


class PurposesListView(ListView):
    model = Purpose


class PurposeCreateView(CreateView):
    model = Purpose
    fields = ['title', 'description']

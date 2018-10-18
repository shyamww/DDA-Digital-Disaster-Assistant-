from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from app.models import Entry, Camp


class CampList(ListView):
    queryset = Camp.objects.all()
    template_name = 'app/list/camps.html'
    context_object_name = 'camps'


class EntryList(ListView):
    queryset = Entry.objects.all()
    template_name = 'app/list/entries.html'
    context_object_name = 'entries'


class CampDetail(DetailView):
    queryset = Camp.objects.all()
    template_name = 'app/detail/camp.html'
    context_object_name = 'camps'


class EntryDetail(DetailView):
    queryset = Entry.objects.all()
    template_name = 'app/detail/entry.html'
    context_object_name = 'entries'


class CampCreate(CreateView):
    queryset = Camp.objects.all()
    template_name = 'app/edit/camp.html'
    fields = ['name', 'item', 'facility']


class EntryCreate(CreateView):
    queryset = Entry.objects.all()
    template_name = 'app/edit/entry.html'
    fields = ['type', 'country', 'state', 'local', 'discription']



























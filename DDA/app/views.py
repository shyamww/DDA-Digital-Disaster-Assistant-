from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from app.models import Entry, Camp
from django.db.models import Q
from django.contrib import messages


class CampList(ListView):
    queryset = Camp.objects.all()
    template_name = 'app/list/camps.html'
    context_object_name = 'camps'


class EntryList(ListView):
    model = Entry
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
    fields = ['name', 'location', 'items', 'facility']


class EntryCreate(CreateView):
    queryset = Entry.objects.all()
    template_name = 'app/edit/entry.html'
    fields = ['type', 'country', 'state', 'local', 'discription', 'photo', 'camp']


def search(request):
    template = 'app/search.html'
    if request.method == 'POST':
        srch = request.POST['search']

        if srch:
            match = Entry.objects.filter(Q(state__icontains=srch)
                                         | Q(country__icontains=srch)
                                         | Q(local__icontains=srch)
                                         )
            context = {
                'entries': match,

            }

            if match:
                return render(request, 'app/list/entries.html', context)
            else:
                messages.error(request, 'not found.')
        else:
            messages.error(request, 'search by country,state,local')
    return render(request, template)


print(Entry.objects.get(pk=1).camp.count())


























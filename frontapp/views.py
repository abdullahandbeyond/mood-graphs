from django.shortcuts import render
from .models import Tracking, Mood
from .forms import TrackingForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from django.views.generic import View, ListView
from .filters import TrackingFilter
from django.db.models import Count, Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

# Create your views here.
@login_required
def filter_mood(request):
    # filtering by user id
    trackings = Tracking.objects.filter(user = request.user.id)
    # initialization of variables
    labels = []; background = []; border = []; data = []

    # counting the moods
    queryset = trackings.values('mood__name', 'mood__background', 'mood__border').annotate(moodcounts=Count('mood__name')).order_by('-mood__name')
    queryset = queryset.exclude(mood__name__isnull=True)
    for entry in queryset:
        labels.append(entry['mood__name'])
        background.append(entry['mood__background'])
        border.append(entry['mood__border'])
        data.append(entry['moodcounts'])
    f = TrackingFilter(request.GET, queryset=queryset)
    return render(request, 'filter_mood.html', {'filter': f})

@login_required
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    form = TrackingForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.user = request.user
        save_it.save()
        messages.success(request, 'Successfully added mood')

    context['form']= form
    return render(request, "create_view.html", context)

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory, modelform_factory, inlineformset_factory
from django.contrib.auth.decorators import login_required
from .models import Gallery, Events
from .forms import EventsForm, ImageForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.generic import ListView


def gallery_list(request):
    events = Events.objects.filter(status='published')
    return render(request, "gallery/post/gallery.html", {"events": events})


def gallery_detail(request, id, name):
    event = get_object_or_404(Events, id=id, name=name, status='published')
    return render(request, 'gallery/post/detail.html', {'event': event})



@login_required
def add_gallery_event(request):
    galleryformset = modelformset_factory(Gallery, form=ImageForm, extra=3)

    if request.method == "GET":
        event_form = EventsForm()
        form_set = galleryformset(queryset=Gallery.objects.none())
        return render(request, 'gallery/post/add_event.html', {"event_form": event_form,
                                                               "form_set": form_set})
    elif request.method == "POST":
        event_form = EventsForm(request.POST)
        form_set = galleryformset(request.POST, request.FILES)

        if event_form.is_valid() and form_set.is_valid():
            event_obj = event_form.save()
            for form in form_set.cleaned_data:
                if form:
                    image = form['image']
                    Gallery.objects.create(image=image, event=event_obj)

            return HttpResponseRedirect('/')
        else:
            print(event_form.errors, form_set.errors)



# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpResponseRedirect
from .models import Note
from .forms import NoteForm

# Create your views here.
def home(request):
    notes = Note.objects
    template = loader.get_template('note.html')
    form = NoteForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save() 
 
    context = {'notes': notes, 'form': form}
    return render(request, 'note.html', context)
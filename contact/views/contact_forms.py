from typing import Any, Dict

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact
from contact.forms import ContactForm



def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context,
    )
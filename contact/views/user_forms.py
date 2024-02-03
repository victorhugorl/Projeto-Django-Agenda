from django.shortcuts import render
from contact.forms import RegisterForm
def register(request):
    form = RegisterForm()
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        },
        )
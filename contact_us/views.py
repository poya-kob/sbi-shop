from django.shortcuts import render

from .forms import ContactForm
from .models import ContactUs


def contact_us(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        first_name = contact_form.cleaned_data.get('first_name')
        last_name = contact_form.cleaned_data.get('last_name')
        email = contact_form.cleaned_data.get('email')
        title = contact_form.cleaned_data.get('title')
        text = contact_form.cleaned_data.get('text')

        ContactUs.objects.create(first_name=first_name, last_name=last_name, email=email, title=title, text=text)
        # todo: show user success message

        contact_form = ContactForm()
    context = {
        'form': contact_form
    }

    return render(request, 'contact_us/contact_us.html', context)

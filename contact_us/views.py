from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import ContactForm


class ContactUsView(FormView):
    template_name = 'contact_us/contact_us.html'
    form_class = ContactForm

    def form_valid(self, form):
        print(form)
        form.save()
        return super(ContactUsView, self).form_valid()

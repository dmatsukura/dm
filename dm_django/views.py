from django.shortcuts import render
from django.contrib import messages
from dm_portfolio.models import Project (
    UserProfile,
    Blog,
    Portfolio,
    Testmonial,
    Certificate,
)

from django.views import generic
from . forms import ContactForm


class IndexView(generic.TemplateView):
    pass


class ContactView(generic.FormView):
    template_name = 'dm_portfolio/contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. Email sent successfully')
        return super().form_valid(form)
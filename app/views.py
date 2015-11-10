# Create your views here.
import json

from django.http import HttpResponse, JsonResponse, Http404

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from accounts.forms import ContactForm
from app.forms import SearchForm


class HomeView(TemplateView):
    template_name = 'home.html'
    contact_form = ContactForm

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['contact_form'] = self.contact_form
        return context


class SearchView(FormView):
    template_name = 'search.html'
    form_class = SearchForm

    def form_valid(self, form):
        if self.request.is_ajax():
            text = self.request.POST.get("search_text", None)
            data = {
                'result': 'search success !!!',
                'message': text,
            }
            return JsonResponse(data=data)
        else:
            return Http404

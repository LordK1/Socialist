from django import forms
from django.forms import Textarea

__author__ = 'k1'


class SearchForm(forms.Form):
    """
    form with single field for search
    """
    search_text = forms.CharField(widget=forms.TextInput(attrs={'id': 'search-box', 'class': 'myfieldclass'}),
                                  required=True,
                                  help_text='please type anything that you want search :")'
                                  )




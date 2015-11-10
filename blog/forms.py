from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from blog.models import Post, Category

__author__ = 'k1'


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Title', help_text='this is required',
                            max_length=100,
                            widget=forms.TextInput(attrs={'id': 'id_title'}))
    content = forms.CharField(label='Content', help_text='This is piece shit ',
                              widget=forms.TextInput(attrs={'id': 'id_content', 'name': 'content'}))

    category = forms.ModelChoiceField(required=True, queryset=Category.objects.all(), label='Category',
                                      help_text='make choice for category or add new',
                                      )

    class Meta:
        model = Post
        fields = ('title', 'category', 'content')
        exclude = ('user',)
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique..."
            }
        }

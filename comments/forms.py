from django import forms
from django_comments.forms import CommentForm
from comments.models import PostComment

__author__ = 'k1'


class PostCommentForm(CommentForm):
    content = forms.CharField(max_length=300, required=True, help_text="Type your comment here !!!")

    def get_comment_model(self):
        # Use our custom comment model instead of default app .
        return PostComment

    def get_comment_create_data(self):
        # Use the of the superclass, and add in the content field
        data = super(CommentForm, self).get_comment_create_data()
        data['content'] = self.cleaned_data['content']
        return data

from comments.forms import PostCommentForm
from comments.models import PostComment


def get_model():
    return PostComment


def get_form():
    return PostCommentForm

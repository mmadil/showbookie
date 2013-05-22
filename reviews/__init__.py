from .models import CustomCommentManager
from .forms import CustomCommentFormManager

def get_model():
    return CustomCommentManager()

def get_form():
    return CustomCommentFormManager()

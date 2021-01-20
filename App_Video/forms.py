from django import forms
from App_Video.models import Video, Feedback


class CommentForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('comment',)

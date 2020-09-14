from django import forms
from .models import Comments,Articles_model


class CommentForm(forms.ModelForm):
      email=forms.EmailField(required=True)
      class Meta:
            model=Comments
            fields = '__all__'
            exclude = ('article','aproved',)
            

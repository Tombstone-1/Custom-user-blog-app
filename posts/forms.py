from django import forms
from .models import recipes

class create_post_form(forms.ModelForm):
    class Meta:
        model = recipes
        fields = '__all__'
        readonly = ['created_on', 'updated_on']
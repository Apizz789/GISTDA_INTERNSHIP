from django.forms import ModelForm

from .models import polygon

class InputForm(ModelForm):
    class Meta:
        model = polygon
        fields = '__all__'
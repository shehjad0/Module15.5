from django import forms
from .models import AlbumModel

class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = '__all__'
        ratings = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]
        widgets = {
            'rating': forms.RadioSelect(choices=ratings),
            'release_date' : forms.NumberInput(attrs={'type': 'date'})
        }
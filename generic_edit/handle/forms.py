from django import forms
from .models import students
class Contactform(forms.Form):
    name=forms.CharField(max_length=200)
    no=forms.IntegerField()
    text=forms.CharField(widget= forms.Textarea)
    
class Studentform(forms.ModelForm):
    class Meta:
        model=students
        fields=['name','no']
        
    
    
        
    


from django.shortcuts import render
from .forms import Contactform
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
#from django.views.generic.detail import DetailView
from .models import students
from django import forms
from .forms import Studentform
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
# Create your views here.
class Contactview(FormView):
    template_name='ahsan.html'
    form_class=Contactform
    success_url='/list/'

class Listview(TemplateView):
    template_name='thanks.html'

class Listview1(ListView):
    model=students
    template_name='thanks1.html'
    context_object_name='ahsan'
    queryset=students.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["myname"] = students.objects.filter(id=2)
        context['name']='My name is Ahsan'
        return context


class save_data(CreateView):
    template_name='ahsan1.html'
    model=students
    fields=['name','no']
    #success_url='/list1/'
    #success_url='/detail/<int:pk>/'
    
    def get_form(self):
        form=super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass'})
        form.fields['no'].widget=forms.PasswordInput(attrs={'class':'mypassword'})
        return form

class Detailviewa(TemplateView):
    model=students
    template_name='detail.html'
    #context_object_name='ahsan'
    #pk_url_kwarg='pk'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myname"] = students.objects.all().last()
        context['all']=students.objects.all()
        #context['name']='My name is Ahsan'
        return context

class StudentCreateView(CreateView):
    form_class=Studentform
    template_name='ahsan1.html'
    #success_url='/detail/'

class StudentUpdateView(UpdateView):
    model=students
    fields=['name','no']
    template_name='ahsan1.html'

class StudentDeleteView(DeleteView):
    model=students
    #fields=['name','no']
    template_name='delete.html'
    context_object_name='ahsan'
    success_url='/create'

    
    
    
    
    
    

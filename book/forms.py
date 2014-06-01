from django import forms
from book.models import Book, Chapter, Comment
from django.shortcuts import render_to_response, render

from django.template import RequestContext

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ('title', 'description', 'thumbnail')
    

class ChapterForm(forms.ModelForm):
    
    class Meta:
        model = Chapter
        fields = ('book', 'chaptertitle', 'text')
        

class CommentForm(forms.ModelForm): 
    
    first_name = forms.CharField(label=False,            
    widget=forms.TextInput(attrs={'class': 'form-control',
                                      'required': 'true',
                                      'placeholder': 'first name'
    })) 
    second_name = forms.CharField(label=False,            
    widget=forms.TextInput(attrs={'class': 'form-control',
                                  'required': 'true',
                                  'placeholder': 'second name'
    }))  

    comment = forms.Field(label=False,            
    widget=forms.TextInput(attrs={'class': 'form-control',
                                  'rows' : '3',
                                  'required': 'true',
                                  'placeholder': 'Comments'
    })) 
    
    class Meta:
        model = Comment
        fields = ('first_name', 'second_name', 'comment')
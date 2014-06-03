from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    username = forms.RegexField(
        label=False, max_length=30, regex=r"^[\w.@+-]+$",
                
       # help_text=_("Required. 30 characters or fewer. Letters, digits and "
        #              "@/./+/-/_ only."),
        error_messages={
            'invalid': ("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},
        widget=forms.TextInput(attrs={'class': 'form-control',

                            'type': "text",
                            'required': 'true',
                            'placeholder': 'username'
    })
     ) 

    email = forms.EmailField(required=True,
        label=False, max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control',
                            'type': "email",
                            'required': 'true',
                            'placeholder': 'Email'
       })        
       )  

    password1 = forms.CharField(label=False,            
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                      'required': 'true',
                                      'placeholder': 'Password'

    }))
                            
                                
    password2 = forms.CharField(label=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                      'required': 'true',
                                      'placeholder': 'Confirm Password'
            }))
        #help_text=_("Enter the same password as above, for verification."))              
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        # user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
            
        return user
    
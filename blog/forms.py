from django import forms
from .models import *
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _





class CommentForm(forms.ModelForm):
    
    name=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
    	'id':'name',
    	'placeholder':'Name*',
        'type': 'text',
        
        

    	}))

    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'id':'email',
        'placeholder':'Email*',
        'type' : 'email',

        }
    ))


    comment=forms.CharField(widget=forms.Textarea(attrs={
        
        'name':'message',
        'placeholder':'Your Message*',
        
        
    	}))

    
   
    class Meta:
        model = Comment    
        fields = ('name','email','comment')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""





# class ContactForm(forms.ModelForm):
    
#     name=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
#     	'class':'form-control form-control-lg',
#     	'placeholder':'Name*',
#         'type': 'text',
#         'name':'contact-name',
#         'id':'contact-name',
        

#     	}))

#     email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
#         'class':'form-control form-control-lg',
#         'id' : 'contact-email',
#         'name' : 'contact-email',
#         'placeholder':'Email*',
#         'type' : 'email',

#         }
#     ))

#     subject=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
#         'class':'form-control form-control-lg',
#         'id' : 'contact-phone',
#         'name' : 'contact-phone',
#         'placeholder':'Subject*',
#         'type' : 'text',
#         }))

#     text=forms.CharField(widget=forms.Textarea(attrs={
#         'class':'form-control form-control-lg',
#         'id' : 'contact-message',
#         'name' : 'contact-message',
#         'placeholder':'Your Message*',
        
        
#     	}))

    
   
#     class Meta:
#         model = ContactFormModel    
#         fields = ('name','email','subject','text')


#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for key, field in self.fields.items():
#             field.label = ""

class ContactForm(forms.Form):
    
    name=forms.CharField(widget=forms.TextInput(attrs={
        
        'name':'name',
        'placeholder':'Your Name*',
        
        
    }))

    phone=forms.CharField(widget=forms.TextInput(attrs={
        
        'name':'phone',
        'placeholder':'Your Phone*',
        
        
    }))

    email=forms.EmailField(widget=forms.EmailInput(attrs={
        
        'name':'Email',
        'placeholder':'Your Email*',
        
        
    }))

    message=forms.CharField(widget=forms.TextInput(attrs={
        
        'name':'name',
        'placeholder':'Your Name*',
        
        
    }))
    
    class Meta:
        model = Contact
        fields = ('name', 'phone', 'email', 'message' )
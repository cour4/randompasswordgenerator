from django import forms
  
# creating a form 
class checkboxes(forms.Form):
    chbox1      = forms.BooleanField(label='Include numbers',required=False)
    chbox2      = forms.BooleanField(label='Include special characters',required=False)
    chbox3      = forms.BooleanField(label='Include upper case letters',required=False)
    num         = forms.IntegerField(label='password length',required=True)
    
from django import forms

class SignupForm(forms.Form):
    your_name = forms.CharField(label='Tu nombre', max_length=100)
    ciudad = forms.CharField(label='Tu ciudad', max_length=50)
    email = forms.EmailField()
    fecha = forms.DateField()
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)

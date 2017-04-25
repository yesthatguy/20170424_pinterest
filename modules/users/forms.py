from django import forms

class SignupForm(forms.Form):
    your_name = forms.CharField(label='Tu nombre', max_length=100, initial="Alumno Dev.f")
    ciudad = forms.CharField(label='Tu ciudad', max_length=50, required=False)
    email = forms.EmailField()
    fecha = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)

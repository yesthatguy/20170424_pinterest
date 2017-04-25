from django.shortcuts import render

from .forms import SignupForm

# Create your views here.
def Signup(request):
    form = SignupForm()

    return render(request, 'users/signup.html', {'form': form})

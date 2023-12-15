from django.shortcuts import render,redirect
from .forms import UserRegisterationForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            #using this method the user will be added and you can see it from the admin page.
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('blog-home')
    else:
        form = UserRegisterationForm()
    return render(request, 'users/register.html', {'form': form})


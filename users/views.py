from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


<<<<<<< HEAD
=======
# CR: Do we really want to allow any random user to register as a seller in the system?
>>>>>>> d79f559d365d23b28060e8b43b6918a4df3b5588
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for { username }. You can now log in.')
            return redirect('sales-login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
    
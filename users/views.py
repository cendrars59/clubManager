from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import RegisterUserForm, UpdateProfileForm, UpdateUserForm


def register(request):
    """"""
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                f"compte utilisateur pour {username} a été créé, connectez-vous à votre compte"
            )
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        # request.FILES is used to take in account the submitted file
        profile_form = UpdateProfileForm(request.POST,
                                         request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request,
                f"compte utilisateur mis à jour"
            )
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    context = {
        'u_form': user_form,
        'p_form': profile_form
    }
    return render(request, 'users/profile.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = forms.EditProfile(request.POST, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = forms.EditProfile(instance=user)

    template_name = 'user/profile.html'
    context = {
        'form': form,
        'set': set,
    }
    return render(request, template_name, context)


def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)

    template_name = 'user/change_password.html'
    context = {'form': form}
    return render(request, template_name, context)


def delete_account_confirm_view(request):
    if request.method == 'GET':
        template_name = 'user/delete_account_confirm.html'
        return render(request, template_name)


def delete_account(request):
    if request.method == 'GET':
        user = request.user
        user.delete()
        return redirect('login')

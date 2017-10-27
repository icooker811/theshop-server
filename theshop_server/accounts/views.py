# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate

from .forms import UserLoginForm


def login_page(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                 login(request, user)
                 return redirect('pages:homepage')
            else:
                return render(request, 'login.html', {
                    'form': form,
                    'error_message': "The password is valid, but the account has been disabled!",
                })
        else:
            return render(request, 'accounts/login.html', {
                'form': form,
                'error_message': "The username and password were incorrect.",
            })
    form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('pages:homepage')


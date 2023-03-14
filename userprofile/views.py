from django.shortcuts import render, redirect, get_object_or_404
from .forms import  ProfileUpdateForm
from .models import UserProfile, Clinical_Detail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def profile(request):

  return render(request, 'userprofile/profile.html')

@login_required
def user_profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your Profile has been updated successfully')
            return redirect('userprofile:profile')

    else:
        form = ProfileUpdateForm(instance=request.user.userprofile)
    context = {
        'form': form,
    }
    return render(request, 'userprofile/profile_update.html', context)

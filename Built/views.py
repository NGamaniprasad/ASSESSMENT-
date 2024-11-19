from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Registration
from .forms import RegistrationForm

def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('view_users')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def view_users(request):
    registrations = Registration.objects.all()
    return render(request, 'view_users.html', {'registrations': registrations})


def update_user(request, user_email):
    # Fetch the user object based on email
    user = get_object_or_404(Registration, email=user_email)

    if request.method == "POST":
        form = RegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully!")
            return redirect('view_users')
    else:
        form = RegistrationForm(instance=user)

    return render(request, 'update_user.html', {'form': form, 'user': user})


def delete_user(request, user_email):
    # Fetch the user object based on email
    user = get_object_or_404(Registration, email=user_email)

    if request.method == "POST":
        user.delete()
        messages.success(request, "User deleted successfully!")
        return redirect('view_users')

    return render(request, 'delete_user.html', {'user': user})

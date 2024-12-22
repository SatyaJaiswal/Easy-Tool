from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.contrib import messages

def home_view(request):
    form = ReviewForm()  # Create a blank form
    return render(request, 'Home/home.html', {'form': form})

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to database
            messages.success(request, "Thank you for your review!")
            return render(request, 'Home/success.html')  # Redirect to success page
        else:
            messages.error(request, "There was an error in your form. Please try again.")
    else:
        form = ReviewForm()  # Display a blank form
    return render(request, 'Home/home.html', {'form': form})

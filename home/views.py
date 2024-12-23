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
            form.save()  
            messages.success(request, "thank you ! your review submit")
            return redirect('home')  
        else:
            messages.error(request, "There was an error in your form. Please try again.")
            print(form.errors)  
    else:
        form = ReviewForm() 
    
    return render(request, 'Home/home.html', {'form': form})
    
from django.shortcuts import render
from .models import Review
from django.db.models import Avg
from django.http import JsonResponse

def get_average_rating(request):
    reviews = Review.objects.all()
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    count = reviews.count()
    return JsonResponse({'average_rating': round(avg_rating, 2), 'count': count})

from django.http import JsonResponse
from django.db import models
from django.db.models import Sum

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    tool = models.CharField(max_length=50)
    rating = models.IntegerField()
    # suggestions = models.TextField()  # Add this if needed
    # review = models.TextField()  # Add this if needed

    def __str__(self):
        return self.name
def get_average_rating(request):
    reviews = Review.objects.all()
    total_rating = reviews.aggregate(Sum('rating'))['rating__sum'] or 0
    count = reviews.count()
    average_rating = total_rating / count if count > 0 else 0
    return JsonResponse({'average_rating': round(average_rating, 2), 'count': count})
from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review = models.TextField()
    suggestions = models.TextField(blank=True, null=True)  # Optional field
    rating = models.PositiveIntegerField()  # Updated to PositiveIntegerField

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.rating} stars"

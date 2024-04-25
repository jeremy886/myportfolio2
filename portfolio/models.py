from django.db import models

# Create your models here.
class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

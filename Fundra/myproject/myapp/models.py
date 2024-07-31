# myapp/models.py

from django.db import models

class SentimentData(models.Model):
    crypto = models.CharField(max_length=10)
    date = models.DateField()
    sentiment_score = models.FloatField()
    price = models.FloatField()
    recommendation = models.CharField(max_length=10)
    graph = models.TextField(default='')  # Ensure this line is present

    def __str__(self):
        return f"{self.crypto} - {self.date}"

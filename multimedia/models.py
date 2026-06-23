from django.db import models

# Create your models here.
# models.py
from django.db import models

class MediaAsset(models.Model):
    MEDIA_CHOICES = [
        ('IMAGE', 'Image'),
        ('VIDEO', 'Video'),
    ]

    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=5, choices=MEDIA_CHOICES)
    file = models.FileField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.get_media_type_display()})"

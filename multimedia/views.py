from django.shortcuts import render
from .models import MediaAsset

def media_gallery(request):
    assets = MediaAsset.objects.all()
    return render(request, 'landing_page.html', {'assets': assets})

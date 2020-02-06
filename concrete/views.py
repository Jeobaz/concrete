from django.shortcuts import render
from concrete.decorators import admin_required
from concrete.models import AlbumImage

def index(request):
    images = AlbumImage.objects.all()
    print(images)
    # for img in images:
    #     print(img.url)
    return render(request, 'index.html', context={'images': images})

@admin_required(login_url="/")
def createGallery(request):
    if request.method == 'GET':
        return render(request, 'createGallery.html')
    else:
        for el in request.FILES.getlist('files'):
            obj = AlbumImage(image = el)
            obj.save()
        return render(request, 'createGallery.html')
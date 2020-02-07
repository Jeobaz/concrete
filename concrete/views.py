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
        
        
def test(request):
    from django.core.mail import send_mail
    images = AlbumImage.objects.all()
    send_mail(
        'Subject here',
        'Here is the message.',
        'sender@xn--80aadqsd0ah9a8b.xn--p1ai',
        ['kirill.manov@list.ru'],
        fail_silently=False,
    )
    return render(request, 'index.html', context={'images': images})
from django.shortcuts import render, redirect
from concrete.decorators import admin_required
from concrete.models import AlbumImage

def index(request):
    #images = AlbumImage.objects.all()
    images = AlbumImage.objects.all().order_by('-id')[:6][::-1]
    #print(images)
    # for img in images:
    #     print(img.url)
    return render(request, 'index.html', context={'images': images})

# @admin_required(login_url="/")
def createGallery(request):
    if request.method == 'GET' and request.user.is_superuser:
        return render(request, 'createGallery.html')
    elif request.user.is_superuser:
        for el in request.FILES.getlist('files'):
            obj = AlbumImage(image = el)
            obj.save()
        return render(request, 'createGallery.html')
    else:
        return redirect('index')
        
        
def send(request):
    from django.core.mail import send_mail
    if request.method == 'POST':
        send_mail(
            "Новая заявка с качайбетон.рф",
            f"Завяка от: {request.POST['email'] }, \nИмя: {request.POST['name'] }, \nТелефон: {request.POST['tel'] }  \n" + "Текст заявки: " + request.POST['message'],
            'sender@xn--80aadqsd0ah9a8b.xn--p1ai',
            ['709090@inbox.ru'],
            fail_silently=False,
        )
        return redirect('index')
    else: 
        return redirect('index')
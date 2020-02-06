from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class AlbumImage(models.Model):
    #image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(1020)], format='PNG', options={'quality': 90})
    image = models.ImageField(upload_to='albums')
    alt = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.image.url)
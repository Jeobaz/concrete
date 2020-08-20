from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class Slide(models.Model):
    #image = ProcessedImageField(upload_to='slides', processors=[ResizeToFit(1020)], options={'quality': 90})
    image = models.ImageField(upload_to='slides')
    alt = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.image.url)
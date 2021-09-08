from django.db import models

class Slider(models.Model):
    img = models.ImageField(upload_to = "upload/slider")

    @staticmethod
    def get_all_slides():
        return Slider.objects.all


class Mainbody(models.Model):
    main_img = models.ImageField(upload_to = "upload/main_img")
    title = models.CharField(max_length = 1500)
    name = models.CharField(max_length = 20000000)
    imdb = models.DecimalField(decimal_places = 1, max_digits = 20)
    
    language1 = models.CharField(max_length = 100, blank = True, null = True)
    language2 = models.CharField(max_length = 100, blank = True, null = True)
    
    Genre1 = models.CharField(max_length = 100, blank = True, null = True)
    Genre2 = models.CharField(max_length = 100, blank = True, null = True)
    Genre3 = models.CharField(max_length = 100, blank = True, null = True)
    Genre4 = models.CharField(max_length = 100, blank = True, null = True)
    
    screenshot1 = models.ImageField(upload_to = "upload/screenshots")
    screenshot2 = models.ImageField(upload_to = "upload/screenshots")
    screenshot3 = models.ImageField(upload_to = "upload/screenshots")
    screenshot4 = models.ImageField(upload_to = "upload/screenshots")

    online = models.CharField(max_length = 2000000)

    link_480 = models.CharField(max_length = 2000000)
    link_720 = models.CharField(max_length = 2000000)
    link_1080 = models.CharField(max_length = 2000000, blank = True, null = True)
    
    yt_link = models.CharField(max_length = 2000000)

    desc = models.CharField(max_length = 20000)

    def __str__(self):
        return self.title

    @staticmethod
    def all_mainbody_items():
        return Mainbody.objects.all

    class Meta:
        ordering = ["-id"]
        
class Contact(models.Model):
    name = models.CharField(max_length = 25000)
    email = models.EmailField(null = True, blank = True)
    phone = models.CharField(max_length = 250, null = True, blank = True)
    body = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name
from django.contrib import admin
from home.models.index import Slider, Mainbody, Contact

class AdminMainbody(admin.ModelAdmin):
    list_display = ["id", "title", "imdb"]

admin.site.register(Slider)
admin.site.register(Mainbody, AdminMainbody)
admin.site.register(Contact)
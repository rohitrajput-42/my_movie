from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from home.models.index import Mainbody, Slider

class Detail(View):
    def get(self, request, id):
        images = Slider.objects.all()
        details = get_object_or_404(Mainbody, pk=id)
        return render(request, 'detail.html', {'details': details, 'images': images})
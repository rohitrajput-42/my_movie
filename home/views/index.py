from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from home.models.index import Slider, Mainbody
from django.core.paginator import Paginator, EmptyPage


class Index(View):
    def get(self, request):
        slides = Slider.objects.all()
        main_items = Mainbody.objects.all()
            
        p = Paginator(main_items, 6)
        page_num = request.GET.get('page', 1)

        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)

        context = {'slides': slides ,'main_items': page}

        return render(request, "index.html", context)
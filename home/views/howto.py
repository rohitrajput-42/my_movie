from django.shortcuts import redirect, render
from django.views import View

class Howto(View):
    def get(self, request):
        return render(request, "howto.html")
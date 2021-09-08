from django.shortcuts import render, redirect
from django.views import View

class Disclaimer(View):
    def get(self, request):
        return render(request, "disclaimer.html")
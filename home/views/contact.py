from django.shortcuts import render, redirect
from django.views import View
from home.forms import ContactForm

def Contact(request):

    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        confirm = False

        if form.is_valid():
            form.save()
            confirm = True

        return render(request, "contact.html", {'form': form, 'confirm': confirm})
        
    else:
        return render(request, "contact.html", {"form": form})    
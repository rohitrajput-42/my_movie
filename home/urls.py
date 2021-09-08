from django.urls import path
from home.views.index import Index
from home.views.details import Detail
from home.views.disclaimer import Disclaimer
from home.views.contact import Contact
from home.views.howto import Howto

urlpatterns = [
    path('', Index.as_view(), name = "index"),
    path('<int:id>', Detail.as_view(), name = 'detail'),
    path('disclaimer', Disclaimer.as_view(), name = "disclaimer"),
    path('contact', Contact, name = "contact"),
    path('howto', Howto.as_view(), name = "howto")
]
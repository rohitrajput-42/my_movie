from django.urls import path
from home.views.index import Index
from home.views.details import Detail

urlpatterns = [
    path('', Index.as_view(), name = "index"),
    path('<int:id>', Detail.as_view(), name = 'detail')
]
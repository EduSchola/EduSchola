from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('' , RedirectView.as_view(url='/'))
]

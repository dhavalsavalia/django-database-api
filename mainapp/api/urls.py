from django.conf.urls import url
from .views import MainAPIListAPIView

urlpatterns = [
    url(r'^$', MainAPIListAPIView.as_view(), name='persondata'),
]
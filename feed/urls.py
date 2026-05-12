from django.urls import path
from .views import HomepageView

app_name = 'feed'

urlpatterns = [
  path('', HomepageView.as_view(), name='index'),
]
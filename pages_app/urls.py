from django.urls import path,include
from .views import HomePagesView,AboutPagesView
app_name='pages_app'
urlpatterns = [
   path('',HomePagesView.as_view(),name='home'),
   path('about/',AboutPagesView.as_view(),name='about'),
]

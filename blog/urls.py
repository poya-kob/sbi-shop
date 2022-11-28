from django.urls import path

from .views import BlogList, BlogDetail

urlpatterns = [
    path("", BlogList.as_view(), name='blogs'),
    path("<int:pk>/", BlogDetail.as_view(), name='blog_detail'),
    path("<int:pk>/<str:title>/", BlogDetail.as_view(), name='blog_detail'),
]

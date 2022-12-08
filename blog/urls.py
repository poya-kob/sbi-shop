from django.urls import path

from .views import BlogList, BlogDetail, CommentsView

urlpatterns = [
    path("", BlogList.as_view(), name='blogs'),
    path("<int:pk>/", BlogDetail.as_view(), name='blog_detail'),
    path("comment/<int:pk>/", CommentsView.as_view(), name='comment'),
    path("<int:pk>/<str:title>/", BlogDetail.as_view(), name='blog_detail'),
]

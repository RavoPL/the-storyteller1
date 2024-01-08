from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>', views.SubmissionView.as_view(), name='submission'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('blog/templates/aboutpage', views.aboutpage, name="aboutpage"),
]
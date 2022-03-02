from django.urls import path
from .views import HomeView,inputview,addview,updateview,deleteview,addcategoryview,LikeView
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('artical/<int:pk>',inputview.as_view(),name="input"),
    path('addpost/', addview.as_view(),name="addpost"),
    path('addcategory/', addcategoryview.as_view(),name="addcategory"),
    path('artical/edit/<int:pk>',updateview.as_view(),name="updatepost"),
    path('artical/remove/<int:pk>',deleteview.as_view(),name="deletepost"),
    path('like/<int:pk>', LikeView,name='like_post'),
]

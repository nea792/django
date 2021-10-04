from django.urls import path,include
from .views import (postCreateView,
                     postDetailView,
                     postUpdateView,
                     postDeleteView,
                     CreateListPost,
                     UserpostListView
                     )

urlpatterns=[
    path('',CreateListPost.as_view(),name='home'),
    path('post/<int:pk>',postDetailView.as_view(),name='datail-post'),
    path('post/<str:username>',UserpostListView.as_view(),name='user-post'),
  #  path('post/new',postCreateView.as_view(),name='create-post'),
    path('post/<int:pk>/update',postUpdateView.as_view(),name='update-post'),
    path('post/<int:pk>/delete',postDeleteView.as_view(),name='delete-post'),
]
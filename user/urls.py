from django.urls import path
from .import views

urlpatterns = [
    path('user-create/', views.USERCreateView.as_view(), name='user_create'),
    path('user-list/', views.USERListView.as_view(), name='user_list'),
    path('user/<int:pk>/detail/', views.USERRetrieveView.as_view(), name='user_retrieve'),
    path('user/<int:pk>/delete/', views.USERDeleteView.as_view(), name='user_delete'),
    path('user/<int:pk>/update/', views.USERUpdateView.as_view(), name='user_update'),
    path('user-list-create/', views.userListCreateView.as_view(), name='movie_list_create'),
    path('user/<int:pk>/retrieve-update/', views.userRetrieveUpdateView.as_view(), name='user_retrieve_update'),
    path('user/<int:pk>/retrieve-destroy/', views.userRetrieveDestroyView.as_view(), name='user_retrieve_destroy'),
    path('user/<int:pk>/retrieve-update-destroy/', views.userRetrieveUpdateDestroyView.as_view(), name='user_retrieve_update_destroy'),
]
from django.urls import path
from .views import UserSignupView, UserLoginView, UserDeleteView, UserListView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('delete/<int:uid>/', UserDeleteView.as_view(), name='user-delete'),
    path('list/', UserListView.as_view(), name='user-list'),
]

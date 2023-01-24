from .views import RegisterView,LoginView,UserView,LogoutView,ClassView,ClassDeleteView,ClassUpdateView
from django.urls import path


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('class/', ClassView.as_view()),
    path('class/delete/<int:pk>/', ClassDeleteView.as_view(), name='class-delete'),
    path('class/update/<int:pk>/', ClassUpdateView.as_view(), name='class-update'),

]
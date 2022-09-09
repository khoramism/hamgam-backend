
from rest_framework.routers import DefaultRouter
from django.urls import path, include 
from . import views 
router = DefaultRouter()

#router.register('name', name_of_class)
#router.register('profile', views.UserProfileViewSet)
#router.register('feed', views.UserProfileFeedViewSet)
urlpatterns = [
    #path('', include(router.urls)),
    #path('login/', views.UserLoginApiView.as_view()),
    #path('', include('authemail.urls')),
    path('user/all', views.AccountUsersListView.as_view(), ),
    path('user/<int:pk>/update', views.AccountUpdateView.as_view(), ),
    path('user/<int:pk>/', views.AccountDetailView.as_view(), ),
    #path('', include('rest_auth.urls')),
    path('', include('rest_auth.urls')),
    path('',include('rest_email_auth.urls')),

]

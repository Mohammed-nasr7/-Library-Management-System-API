# library/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# تعريف الروتر وتسجيل النقاط الخاصة بالـ API
router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'transactions', views.TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),  # تضمين النقاط الخاصة بالـ API هنا
]

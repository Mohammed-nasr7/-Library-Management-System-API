# library_management_system/urls.py
from django.contrib import admin
from django.urls import path, include  # include مهم لضم روابط التطبيقات
from rest_framework import routers
from library import views

# تعريف الروتر لربط روابط الـ API
router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'transactions', views.TransactionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),  # صفحة الأدمن
    path('api/', include(router.urls)),  # تضمين روابط API هنا
]

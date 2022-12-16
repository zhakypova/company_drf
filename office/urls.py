from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('', views.ItemViewSet)

urlpatterns = [
    path('items/', include(router.urls)),
    path('firm/', views.firm_view, name = 'firm_view'),
    path('firm/<int:id>/', views.firm_detail, name = 'firm_detail'),
    path('category/', views.CategoryAPIView.as_view(), name='category'),
    path('category/<int:id>/', views.CategoryDetailAPIView.as_view(), name='category_detail'),
]
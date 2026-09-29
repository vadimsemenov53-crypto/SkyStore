from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    HomeListView,
    ProductAddCreateView,
    ProductDetailView,
    ContactView,
    ProductUpdateView,
    ProductDeleteView,
    ProductCategoryView
)

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeListView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_add/', ProductAddCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/category/<int:category_id>/', ProductCategoryView.as_view(), name='product_category')
]
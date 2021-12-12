from django.urls import path
from .views import *


urlpatterns = [
    path('category/', CategoryListView.as_view(), name="category"),
    path('category-detail/<int:id>/', CategoryDetailView.as_view(), name="category-detail"),
    path('', ExpenseListView.as_view(), name="expense"),
    path('<int:pk>', ExpenseDetailView.as_view(), name="expense-detail"),
]
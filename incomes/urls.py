from django.urls import path
from .views import *


urlpatterns = [
    path('category/', SourceListView.as_view(), name="category"),
    path('category-detail/<int:id>/', SourceDetailView.as_view(), name="category-detail"),
    path('', IncomeListView.as_view(), name="expense"),
    path('<int:pk>', IncomeDetailView.as_view(), name="expense-detail"),
]
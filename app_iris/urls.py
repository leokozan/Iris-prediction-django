from django.urls import path
from app_iris.views import IrisListView
from app_iris.views import IrisCreateView
from app_iris.views import IrisUpdateView
from app_iris.views import IrisDashboardView

urlpatterns = [
    path('', IrisListView.as_view(), name='iris_list'),
    path('create/', IrisCreateView.as_view(), name='iris_create'),
    path('<int:id>/', IrisUpdateView.as_view(), name='iris_update'),
    path('dashboard/', IrisDashboardView.as_view(), name='iris_dashboard'),
]

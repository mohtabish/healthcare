from django.urls import path
from . import views

urlpatterns = [
    path('', views.MappingListCreateView.as_view(), name='mapping-list-create'),
    path('<int:patient_id>/', views.PatientMappingView.as_view(), name='patient-mappings'),
    path('delete/<int:pk>/', views.MappingDetailView.as_view(), name='mapping-delete'),
]
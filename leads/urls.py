from django.urls import path
from .import views


urlpatterns = [
    
    path('leads-list/', views.LeadListView.as_view() , name = "leads_list" ),
    path('<int:id>/', views.lead_detail , name = "detail" ),
    path('lead-create/', views.LeadCreateView.as_view() , name = "lead-create" ),
    path('update/<slug:pk>/', views.LeadUpdateView.as_view() , name = "lead-update" ),
    path('delete/<int:id>/', views.lead_delete , name = "lead-delete" ),
]

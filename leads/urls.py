from django.urls import path
from .import views


urlpatterns = [
    
    path('leads-list/', views.lead_list , name = "leads_list" ),
    path('<int:id>/', views.lead_detail , name = "detail" ),
    path('lead-create/', views.lead_create , name = "lead-create" ),
    path('update/<int:id>/', views.lead_update , name = "lead-update" ),
    path('delete/<int:id>/', views.lead_delete , name = "lead-delete" ),
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('companies/', views.All_details.as_view(), name='company_list'),
    path('company/<int:pk>/', views.Company_Detail.as_view(), name='company_detail'),
    path('company/add/', views.AddCompanyView.as_view(), name='add_company'),
    path('product/add/<int:pk>/', views.Add_product.as_view(), name='add_product'),
    path('edit/<int:pk>/',views.CompanyUpdate.as_view(),name='edit'),
    path('delete/<int:pk>/',views.Delete_company.as_view(),name='delete_company'),
    path('emi/<int:id>/',views.emi_calculater,name='emi')
         
]


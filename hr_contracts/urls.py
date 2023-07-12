from django.urls import path
from hr_contracts import views
# from app_name import file_name

urlpatterns = [
	path('show_contract/', views.all_contracts),
	path('new_contract/', views.add_contract),
	path('update/<int:contract_id>/', views.update_contract),
	path('detail/<int:contract_id>/', views.contract),
	path('delete/<int:contract_id>/', views.delete_contract),
	path('search_by/', views.search_by),
    path('order_by/', views.order_by)
	# path('domain_name/', file_name.function_name)
]
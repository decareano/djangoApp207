from django.contrib import admin
from django.urls import path


from covidapp.views import hospital_create_view, hospital_detail_view, hospital_list_view, hospital_index_view
from covidapp import views

app_name = 'covidapp'

urlpatterns = [
	path('createCovid', hospital_create_view),
	path('', views.hospital_index_view, name='hospital-index'),
	path('hospitals/', views.hospital_list_view, name='hospital-list'),
	path('<int:id>/', views.hospital_detail_view, name='hospital-detail'),
	path('hospital_chart_view', views.hospital_chart_view, name='hospital_chart_view')
	#path('<int:id>/', hospital_detail_view),
	#path('product', product_detail_view, name='product-detail'),
    # path('create', product_create_view),
    # path('', product_list_view, name='product-list'),
    
    # path('initial', render_initial_data),
    # #path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    # path('<int:id>/delete/', product_delete_view, name='product-delete'),
   
]
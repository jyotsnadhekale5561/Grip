from django.urls import path
from . import views
app_name='bank_site'

urlpatterns = [
    path('',views.home_veiw,name="Home"),
    path('transfer/<int:pk>/',views.transfer,name="transfer"),
    path('view/',views.view_all,name="view_all"),
    path('transfers/',views.view_all_transfers,name='all_transfers')
]
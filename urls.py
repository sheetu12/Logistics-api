from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stateinfo/<int:pk>', views.state_detail),
    path('stateinfo/', views.state_list),
    path('couponinfo/<int:pk>', views.coupon_detail),
    path('couponinfo/', views.coupon_list),
    path('statusinfo/<int:pk>',views.status_detail),
    path('statusinfo/',views.status_list),
]

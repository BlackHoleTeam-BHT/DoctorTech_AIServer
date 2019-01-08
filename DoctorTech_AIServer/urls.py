from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diabetes/',include('Diabetes.urls')),
    path('breast-cancer/', include('BreastCancer.urls')),
    path('health/',include('Health.urls'))
]

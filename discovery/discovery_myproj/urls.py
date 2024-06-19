from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('discovery_myapp.urls')),  # discovery_myapp의 URL을 포함
    path('', RedirectView.as_view(url='/app/analyze/')),  # 루트 URL을 app/analyze로 리디렉션
]


from django.contrib import admin
from django.urls import path, include
from god.views import (
    home,
    hostSignup,
    hostLogin,
    hostCloseMeeting
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('hostLogin/', hostLogin, name='hostLogin'),
    path('hostSignup/', hostSignup, name='hostSignup'),
    path('hostCloseMeeting/', hostCloseMeeting, name='hostCloseMeeting'),
    path('god/', include('god.urls', namespace='god'))
]

from django.contrib import admin

from django.conf.urls import url, include
from django.urls import path
import Supervisor

urlpatterns = [
    url(r'show/', include('Supervisor.urls')),
    path('view/',Supervisor.views.view ),

	path('addVendar/',Supervisor.views.addVendar),
    path('viewVendar/',Supervisor.views.viewVendar )

]

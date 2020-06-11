from django.contrib import admin
from django.urls import path,include
from TimeTracker.views import index,register,logoutUser,loginUser,clearSites
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',index, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('Api.urls')),
    path('login/', loginUser, name='login'),
    path('signUp/', register, name='signup'),
    path('logout/', logoutUser, name='logout'),
    path('delete/', clearSites, name='delete')
]

urlpatterns += staticfiles_urlpatterns()
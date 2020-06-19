from django.contrib import admin
from django.urls import path, include
from TimeTracker.views import register, Logout, LoginUser, ClearSites, IndexView, UserList, UserDetails
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('admin-view/', UserList.as_view(), name='user_list'),
    path('admin-view/<int:pk>', UserDetails.as_view(), name='detail'),
    path('api/', include('Api.urls')),
    path('login/', LoginUser.as_view(), name='login'),
    path('signUp/', register, name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
    path('delete/', ClearSites.as_view(), name='delete')
]

urlpatterns += staticfiles_urlpatterns()

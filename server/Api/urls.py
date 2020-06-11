'''
  developed by Ashkan Ganj
  Github:https://github.com/Ashkan-agc
'''

from django.urls import path,include
from Api.views import UpdateAvtive,UserLoginApiView,get_data
urlpatterns = [
    path('ChartData/',get_data),
    path('update/', UpdateAvtive, name= 'update'),
    # path('remove/', removedTab, name='removed'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    
]

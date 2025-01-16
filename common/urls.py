from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    # should specify the template_name. or not, TemplateDoesNotExist error will be raised.
    path('login/', 
         auth_views.LoginView.as_view(template_name='common/login.html'),
                                        name='login'),
    path('logout/',
         views.logout_view, name='logout')
]

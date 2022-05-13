from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'users'
urlpatterns = [
    path('signup', views.RegistrationView.as_view(), name='signup'),
    path('signin', views.SignInView.as_view(), name='signin'),
    # path('user/', views.UserSearchView.as_view(), name='search'),
    path('user/<int:pk>', views.UserProfileView.as_view(), name='profile'),
    path('user/<slug:slug>', views.UserProfileView.as_view(), name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

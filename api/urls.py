from django.urls import path
from .views import ClientUserSignupView

urlpatterns = [
    path('client/signup/', ClientUserSignupView.as_view(), name='client-signup'),
]

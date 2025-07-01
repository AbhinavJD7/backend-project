from django.urls import path
from .views import ClientUserSignupView,ClientUserVerifyEmailView

urlpatterns = [
    path('client/signup/', ClientUserSignupView.as_view(), name='client-signup'),
    path('client/verify-email/', ClientUserVerifyEmailView.as_view(), name='client-verify-email'),

]

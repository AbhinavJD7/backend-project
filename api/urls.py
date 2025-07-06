from django.urls import path
from .views import ClientUserSignupView,ClientUserVerifyEmailView,OpsFileUploadView , ClientFilesListView ,GenerateDownloadLinkView, DownloadFileView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('client/signup/', ClientUserSignupView.as_view(), name='client-signup'),
    path('client/verify-email/', ClientUserVerifyEmailView.as_view(), name='client-verify-email'),
    path('client/login/', TokenObtainPairView.as_view(), name='client-login'),
    path('ops/upload/', OpsFileUploadView.as_view(), name='ops-file-upload'),
    path('client/files/', ClientFilesListView.as_view(), name='client-files-list'),
    path('client/download-link/<int:file_id>/', GenerateDownloadLinkView.as_view(), name='generate-download-link'),
    path('client/download-file/', DownloadFileView.as_view(), name='download-file'),

]

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClientUserSignupSerializer
from .models import CustomUser
from django.core.signing import Signer,BadSignature

class ClientUserSignupView(APIView):
    def post(self, request):
        serializer = ClientUserSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Encrypt user id for verification URL
            signer = Signer()
            encrypted = signer.sign(user.id)
            # Build encrypted URL (change host as per deployment)
            encrypted_url = f"http://localhost:8000/api/client/verify-email/?token={encrypted}"
            # Here you’d send the email in production (or use Celery!)
            return Response({
                "message": "Sign up successful. Use this link for email verification.",
                "verify_url": encrypted_url
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ClientUserVerifyEmailView(APIView):
    def get(self, request):
        token = request.GET.get('token')
        if not token:
            return Response({"message": "No token provided."}, status=400)
        signer = Signer()
        try:
            user_id = signer.unsign(token)
            user = CustomUser.objects.get(pk=user_id, user_type='client')
            user.is_active = True
            user.save()
            return Response({"message": "Email verified successfully. You can now log in."})
        except (BadSignature, CustomUser.DoesNotExist):
            return Response({"message": "Invalid or expired verification link."}, status=400)


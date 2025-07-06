from rest_framework import serializers
from .models import CustomUser
from .models import SharedFile


class ClientUserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            user_type='client'
        )
        user.is_active = False  # Require email verification
        user.save()
        return user

class SharedFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedFile
        fields = ['file']

    def validate_file(self, value):
        allowed_types = ['.pptx', '.docx', '.xlsx']
        import os
        ext = os.path.splitext(value.name)[1].lower()
        if ext not in allowed_types:
            raise serializers.ValidationError('Only .pptx, .docx, .xlsx files are allowed.')
        return value
    
class SharedFileListSerializer(serializers.ModelSerializer):
     class Meta:
        model = SharedFile
        fields = ['id', 'file', 'uploaded_at', 'uploader']


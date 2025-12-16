from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    repassword = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email', 
            'first_name',
            'last_name',
            'password',
            'repassword',
        ]

    def validate_password(self, value):
        '''
        validate the password to ensure it meets certain criteria
        such as minimum length, contains at least one digit, one letter, etc.
        '''
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in value):
            raise serializers.ValidationError("Password must contain at least one letter.") 
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in value):
            raise serializers.ValidationError("Password must contain at least one lowercase letter.")
        if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for char in value):
            raise serializers.ValidationError("Password must contain at least one special character.") 
        if self.initial_data.get('repassword') != value:
            raise serializers.ValidationError("Passwords do not match.")
        return value
        
    def create(self, validated_data):
        '''
        Create and return a new User instance, given the validated data.
        '''
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            password=validated_data.get('password')
        )
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email', 
            'first_name',
            'last_name',
        ]

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email', 
        ]

class UserPasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_new_password = serializers.CharField(write_only=True)

    def validate_new_password(self, value):
        '''
        validate the new password to ensure it meets certain criteria
        such as minimum length, contains at least one digit, one letter, etc.
        '''
        if len(value) < 8:
            raise serializers.ValidationError("New password must be at least 8 characters long.")
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("New password must contain at least one digit.")
        if not any(char.isalpha() for char in value):
            raise serializers.ValidationError("New password must contain at least one letter.") 
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("New password must contain at least one uppercase letter.")
        if not any(char.islower() for char in value):
            raise serializers.ValidationError("New password must contain at least one lowercase letter.")
        if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for char in value):
            raise serializers.ValidationError("New password must contain at least one special character.") 
        if self.initial_data.get('confirm_new_password') != value:
            raise serializers.ValidationError("New passwords do not match.")
        return value
    
    def validate(self, data):
        ''' 
        Validate that the old password is correct.
        '''
        user = self.context['request'].user
        if not user.check_password(data['old_password']):
            raise serializers.ValidationError({"old_password": "Old password is not correct."})
        return data
    
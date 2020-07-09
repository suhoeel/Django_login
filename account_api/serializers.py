from rest_framework import serializers
from django import forms
from .models import UserAccount, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserAccountSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()
    
    class Meta:
        model = UserAccount
        fields = '__all__'

    def create(self, validated_data):
        user_profile_data = validated_data.pop('user_profile')
        profile = UserProfile.objects.create(**user_profile_data)
        account = UserAccount.objects.create(user_profile=profile, **validated_data)
        return account



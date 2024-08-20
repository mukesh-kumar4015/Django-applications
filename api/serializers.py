from rest_framework import serializers
from incident_app.models import Incident, UserProfile
from django.contrib.auth.models import User


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'

    def create(self, validated_data):
        return Incident.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.incident_id = validated_data.get('incident_id', instance.incident_id)
        instance.incident_type = validated_data.get('incident_type', instance.incident_type)
        instance.incident_details = validated_data.get('incident_details', instance.incident_details)
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def update(self, instance, validated_data):
        print("hello")
        instance.save()
        return  instance


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(source='user_profile', many=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'profile')

    def create(self, validated_data):
        return User.objects.create(**validated_data)


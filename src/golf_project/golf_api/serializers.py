from rest_framework import serializers, fields

from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our profile object."""

    class Meta:
        model = models.UserProfile
        fields = ('email', 'lastname', 'firstname', 'handicap')
        extra_kwargs = {
            'last_login': {'read_only': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """Used to create a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            lastname=validated_data['lastname'],
            firstname=validated_data['firstname'],
            handicap=validated_data['handicap']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

class CourseSerializer(serializers.ModelSerializer):
    """A serializer for our course object."""

    class Meta:
        model = models.Course
        fields=('__all__')

class HoleSerializer(serializers.ModelSerializer):
    """A serializer for our hole objects."""

    class Meta:
        model = models.Hole
        fields = ('__all__')

class MatchStrikeSerializer(serializers.ModelSerializer):
    """A serializer for our strikes in a match event."""

    class Meta:
        model = models.MatchStrike
        fields = ('__all__')

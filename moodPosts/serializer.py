from rest_framework import serializers
from moodPosts.models import Moodposts


class MoodSerializer(serializers.ModelSerializer): # forms.ModelForm
    class Meta:
        model = Moodposts

        fields = [
            'user',
            'mood',
        ]
        read_only_fields = ['user']
from rest_framework import serializers
from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'created_at', 'completed']

    def validate_title(self, value):

        if ToDo.objects.filter(title=value).exists():
            raise serializers.ValidationError("This value for title already exists.")
        return value

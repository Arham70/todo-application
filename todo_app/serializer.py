from rest_framework import serializers
from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'created_at', 'completed']


        def create(self, validated_data):
            # Exclude 'created_at' and 'completed' from being passed during creation
            validated_data.pop('created_at', None)
            validated_data.pop('completed', None)
            return super().create(validated_data)


class ToDoDocumentationSerializer(serializers.ModelSerializer):
        class Meta:
            model = ToDo
            fields = ['title', 'description']

            def validate_title(self, value):
                if ToDo.objects.filter(title=value).exists():
                    raise serializers.ValidationError("This value for title already exists.")
                return value

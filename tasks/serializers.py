from rest_framework import serializers
from .models import Task
from users.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    assigned_to_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'project', 'assigned_to',
                  'assigned_to_id', 'status', 'due_date', 'created_at']
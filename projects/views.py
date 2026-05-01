from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def project_list(request):
    if request.method == 'GET':
        projects = Project.objects.filter(created_by=request.user) | Project.objects.filter(members=request.user)
        serializer = ProjectSerializer(projects.distinct(), many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        if request.user.role != 'admin':
            return Response({'error': 'Only admins can create projects'}, status=403)
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response({'error': 'Project not found'}, status=404)

    if request.method == 'GET':
        return Response(ProjectSerializer(project).data)

    if request.method == 'PUT':
        if request.user.role != 'admin':
            return Response({'error': 'Only admins can edit projects'}, status=403)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        if request.user.role != 'admin':
            return Response({'error': 'Only admins can delete projects'}, status=403)
        project.delete()
        return Response({'message': 'Deleted successfully'}, status=204)
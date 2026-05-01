from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # API routes
    path('api/users/', include('users.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/tasks/', include('tasks.urls')),

    # Frontend pages (using 'page/' prefix to avoid conflict with API)
    path('', TemplateView.as_view(template_name='login.html')),
    path('page/login/', TemplateView.as_view(template_name='login.html')),
    path('page/register/', TemplateView.as_view(template_name='register.html')),
    path('page/dashboard/', TemplateView.as_view(template_name='dashboard.html')),
    path('page/projects/', TemplateView.as_view(template_name='projects.html')),
    path('page/tasks/', TemplateView.as_view(template_name='tasks.html')),
]

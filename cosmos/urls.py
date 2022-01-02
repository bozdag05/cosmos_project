from django.urls import path, include
from .views import *
from django.http import StreamingHttpResponse
from camera import VideoCamera, gen

urlpatterns = [
    path('', index, name='index'),
    path('authors/', authors, name='authors'),
    path('author/<int:author_id>/', author, name='author'),
    path('reports/', reports, name='reports'),
    path('get_report/<int:report_id>/', report, name='report'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add/', index, name='add_report'),
    path('observation/', observation, name='observation'),
    path('broadcast/', index, name='index'),
    path('monitor/', lambda r: StreamingHttpResponse(gen(VideoCamera()),
                                                     content_type='multipart/x-mixed-replace; boundary=frame'),
         name='monitor'),
]

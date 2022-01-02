from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'OK')
            return redirect('index')
        else:
            messages.error(request, 'error')
    else:
        form = UserRegisterForm()
    return render (request, 'cosmos/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'error')
    else:
        form = UserLoginForm()

    return render(request, 'cosmos/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')

def index(request):
    reports = Reports.objects.all()
    title = 'Отчёты'
    context= {
        'reports': reports,
        'title': title
    }

    return render(request, 'cosmos/index.html', context=context)

def reports(request):
    reports = Reports.objects.all()
    title = 'Отчёты'
    context= {
        'reports': reports,
        'title': title
    }

    return render(request, 'cosmos/reports.html', context=context)

def authors(request, ):
    authors = Author.objects.all()
    title = 'Авторы проекта'
    context= {
        'authors': authors,
        'title': title
    }

    return render(request, 'cosmos/authors.html', context=context)

def author(request, author_id):
    author = Author.objects.get(pk=author_id)
    """try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        author = None"""
    return render(request, 'cosmos/author.html', {'author': author})

def report(request, report_id):
    item = Reports.objects.get(pk=report_id)

    return render(request, 'cosmos/get_report.html', {'item': item})

def observation(request):
    title = 'IP-camera'

    return render(request, 'cosmos/observation.html', {'title': title,})


'''from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading

class VideoCamera(object):
    template_name = 'cosmos/observation.html'
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def livefe(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass'''
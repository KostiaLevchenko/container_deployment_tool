import docker
from django.shortcuts import render, redirect, get_object_or_404
from . forms import RunContainer
from . models import Container
# Create your views here.




def run(image, cmd):
    client = docker.from_env()
    container = client.containers.run(image, cmd, detach=True)
    return container


def run_another_container(request):
    if request.method == 'POST':
        run(image=request.POST.get('image_name'), cmd=request.POST.get('cmd_text'))
        return render(request, 'container_deploy/run_another_container.html')
    else:
        return render(request, 'container_deploy/run_another_container.html')


def images_list(request):
    client = docker.from_env()
    images = client.images.list()
    return render(request, 'container_deploy/images_list.html', {'images': images})


def containers_list(request):
    client = docker.from_env()
    containers = client.containers.list()
    return render(request, 'container_deploy/containers_list.html', {'containers': containers})

import docker
from django.shortcuts import render, redirect, get_object_or_404
from . forms import RunContainer
from . models import Container


def run(image, cmd):
    client = docker.from_env()
    container = client.containers.run(image, cmd, detach=True)
    return container


def stop(container_id):
    client = docker.from_env()
    container = client.containers.get(container_id)
    return container.stop()


def remove(container_id):
    client = docker.from_env()
    container = client.containers.get(container_id)
    return container.remove()


def run_another_container(request):
    if request.method == 'POST':
        run(image=request.POST.get('image_name'), cmd=request.POST.get('cmd_text'))
        return render(request, 'container_deploy/run_another_container.html')
    return render(request, 'container_deploy/run_another_container.html')


def images_list(request):
    client = docker.from_env()
    images = client.images.list()
    return render(request, 'container_deploy/images_list.html', {'images': images})


def containers_list(request):
    if request.method == 'POST':
        if request.POST.get('method_type') == "stop":
            stop(container_id=request.POST.get('container_id'))
        else:
            remove(container_id=request.POST.get('container_id'))
    client = docker.from_env()
    containers = client.containers.list(all=True)
    running = [container for container in containers if container.status == 'running']
    exited = [container for container in containers if container.status == 'exited']
    return render(request, 'container_deploy/containers_list.html', {'containers': containers, 'running': running, 'exited': exited})

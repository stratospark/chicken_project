from fabric.api import local
from fabric.context_managers import cd
from fabric.operations import run


def deploy_frontend():
    local('cd frontend; grunt build')
    local('rsync -vramlHP frontend/dist www@vegan-oasis.tk:~/Code/chicken_project/frontend')
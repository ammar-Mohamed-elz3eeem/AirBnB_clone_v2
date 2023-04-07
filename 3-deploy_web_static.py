#!/usr/bin/python3
"""
This script will deploy all my work to remote servers i have
using fabric commands do_pack and do_deploy
"""
from fabric.api import *
from datetime import datetime
from os.path import exists
env.hosts = ["52.91.153.115", "52.91.202.178"]


def do_pack():
    """
    This function will archieve
    all my files in web static folder
    """

    time = datetime.now()
    arcieve_name = "web_static_{}.tgz".format(time.strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -czvf versions/{} web_static".format(arcieve_name))
    if create is not None:
        return "versions/{}".format(arcieve_name)
    else:
        return None


def do_deploy(archive_path):
    """
    This function will archieve
    all my files in web static folder
    """

    if exists(archive_path) is False:
        return False
    try:
        fn = archive_path.split("/")[-1]
        file_name = fn.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, file_name))
        run("tar -xzf /tmp/{} -C {}{}/".format(
            fn, path, file_name))
        run("rm /tmp/{}".format(fn))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, file_name))
        run("rm -rf {}{}/web_static/".format(path, file_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, file_name))
        return True
    except Exception as e:
        return False


def deploy():
    """
    this function will call do_pack and do_deploy
    to make deployments automatically to servers we have
    """

    create = do_pack()
    if create is None:
        print("REALLY NONE")
        return False
    do_deploy(create)

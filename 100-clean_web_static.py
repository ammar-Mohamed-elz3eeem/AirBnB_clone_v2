#!/usr/bin/python3
"""
This script will deploy all my work to remote servers i have
using fabric commands
"""
from fabric.api import *
from datetime import datetime
from os import listdir, path as p
env.hosts = ["100.25.200.200", "54.237.27.107"]


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
    - put archive in /tmp/archive_name.tgz
    - make directory /data/web_static/releases/
    - extract archive /tmp/archive_name.tgz to
      folder /data/web_static/releases/archive_name
    - remove archive_name.tgz from /tmp folder
    - move files from /data/web_static/releases/archive_name/web_static/
      to /data/web_static/releases/archive_name
    - remove directry web_static inside
      /data/web_static/releases/archive_name/
    """

    if p.exists(archive_path) is False:
        return False
    try:
        fn = archive_path.split("/")[-1]
        file_name = fn.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}{}/".format(path, file_name))
        run("sudo tar -xzf /tmp/{} -C {}{}/"
            .format(fn, path, file_name))
        run("sudo rm /tmp/{}".format(fn))
        run("sudo mv {0}{1}/web_static/* {0}{1}/"
            .format(path, file_name))
        run("sudo rm -rf {}{}/web_static/".format(path, file_name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}{}/ /data/web_static/current"
            .format(path, file_name))
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


def do_clean(number=0):
    """ clean all releases from my web servers """
    number = int(number)
    number = 1 if number <= 0 else number
    tars = sorted(listdir("./versions"))
    length = len(tars) - number
    with lcd("versions"):
        [local(f"rm {tars[i]}") for i in range(length)]
    with cd("/data/web_static/releases"):
        archs = run("ls -tr").split()
        length = len(archs) - number
        [run("sudo rm -rf ./{}".format(archs[i])) for i in range(length)]

#!/usr/bin/python3
"""
Fab file to deploy archive from
local to host server
"""
from fabric.api import *
from os.path import exists
env.hosts = ["52.91.153.115", "52.91.202.178"]


def do_deploy(archive_path):
    """
    This function will archieve
    all my files in web static folder
    """

    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        fn = archive_path.split("/")[-1]
        file_name = fn.split(".")[0]
        path = "/data/web_static/releases/"
        run("mkdir -p {}{}/".format(path, file_name))
        run("tar -xzf /tmp/{} -C {}{}".format(\
        archive_path, path, file_name))
        run("rm /tmp/{}".format(fn))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, file_name))
        run("rm -rf {}{}/web_static/".format(path, file_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, file_name))
        return True
    except:
        return False

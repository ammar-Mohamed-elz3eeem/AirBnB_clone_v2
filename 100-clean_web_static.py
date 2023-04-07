#!/usr/bin/python3
"""
This script will deploy all my work to remote servers i have
using fabric commands
"""

from fabric.api import *
import os

env.hosts = ["100.25.200.200", "54.237.27.107"]


def do_clean(number=0):
    """
    clean all releases from my web servers according to number
    Args:
        number (int): number of releases we want to keep
        in the system, if number less than or equal to 1 so
        system will kep only most recent release
    """

    number = int(number)
    number = 1 if number <= 0 else number
    tars = sorted(os.listdir("./versions"))
    length = len(tars) - number

    with lcd("versions"):
        [local(f"rm ./{tars[i]}") for i in range(length)]

    with cd("/data/web_static/releases"):
        archs = run("ls -tr").split()
        length = len(archs) - number
        [run("sudo rm -rf ./{}".format(archs[i])) for i in range(length)]

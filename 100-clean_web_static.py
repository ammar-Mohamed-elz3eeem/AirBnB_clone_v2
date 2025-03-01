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
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]

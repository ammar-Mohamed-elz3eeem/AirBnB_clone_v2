#!/usr/bin/python3
"""
Fab file to create archieve from
all files in my web_static folder
"""
from datetime import datetime
from fabric.api import *


def do_pack():
    time = datetime.now()
    arcieve_name = "web_static_{}.tgz".format(time.strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -czvf versions/{} web_static".format(arcieve_name))
    if create is not None:
        return arcieve_name
    else:
        return None

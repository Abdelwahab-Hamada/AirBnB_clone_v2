#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

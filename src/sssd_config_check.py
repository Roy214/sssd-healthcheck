"""
Validate /etc/sssd/sssd.conf
* Author:    abroy@redhat.com
"""
# !/usr/bin/python3
import os


def sssd_config_check():
    status = os.system("sssctl config-check")
    if status == 0:
        print("sssd.conf looks good via sssctl command")
    else:
        print(os.system("sssctl config-check"))


def main():
    sssd_config_check()


main()

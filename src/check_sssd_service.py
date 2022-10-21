"""
Check if sssd service is running
* Author:    abroy@redhat.com
"""
#!/usr/bin/python3
import os

def is_sssd_active():
    status = os.system("systemctl status sssd" '> /dev/null')
    return status

def main():
    if is_sssd_active() == 0:
        print("SSSD is Running")
    else:
        print("SSSD is not active please use `sssd -i d9` command to start sssd in debug mode")

main()

import os
import command

def is_sssd_active():
    status = os.system("systemctl status sssd" '> /dev/null')
    return status

def main():
    if is_sssd_active() == 0:
        print("SSSD is Running")
    else:
        print("SSSD is not active")

main()

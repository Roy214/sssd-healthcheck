# SSSD(System Security Services Daemon) Health Check
This tool will verify basic prechecks of sssd client system joined with Active Directory and sssd client running on IPA system. 

## Overview
This tool will validate multiple components in order to work sssd smoothly with AD and IPA. Following the the faetures of this tool:
  - Check if sssd package is installed it will also check if the latest package is installed.
  - Validate sssd config and permission of /etc/sssd/sssd.conf.
  - Validate if sssd service is running in case if it's faling it will show the command to run sssd in debug mode.
  - Validate ports and firewall.
  - Validate keytab, kvno version.
  - Enable sssd debugging and check for common errors.
    - Check if sssd backend is going offline.
    - Check if any of the sssd service is getting killed by watchdog.
    - sdap_async_sys_connect request failed: Connection timed out.
    - Check if the login is being denied by AD-GPO.
    - Use sssctl analyze tool to anlayze the log.

## Upstream sssd Documentation 
The most up-to-date documentation of sssd can be found at https://sssd.io.

## Configure Virtual Environment For This Tool
  
## Contacts


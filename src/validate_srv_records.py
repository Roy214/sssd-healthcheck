#!/usr/bin/python3

"""
* Author : Nikhil Suryawanshi <nsuryawa@redhat.com>

This program will check if srv records for "ldap" and "kerberos" service are resolvable

"""
def validte_srv_records():

    import sys

    sys.path.insert(1, './../py-venv/lib/python3.6/site-packages')
    sys.path.insert(1, './../py-venv/lib64/python3.6/site-packages')

    import dns.resolver
    import dns.query


    domain = input ("Please enter ldap domain:")
    try:
        dns.resolver.query('_ldap._tcp.'+domain, 'SRV')
        print ("srv records for ldap are present")
    except:
        print ("Unable fetch to fecth SRV records for ldap")
    try:
        dns.resolver.query('_kerberos._tcp.'+domain, 'SRV')
        print("srv records for kerberos are present")
    except:
        print ("Unable fetch to fecth SRV records for kerberos")

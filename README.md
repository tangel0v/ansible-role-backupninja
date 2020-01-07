Role Name
=========

This role will install and configure backupninja based on my own needs. It uses a temporal folder to create a full backup of a list of directories and encrypt it using GPG (in the last version). This role is used to see how to transform a service into a ansible role and show different ways to improve it.

Requirements
------------

To use this role you should have installed:
* tar, gzip

Role Variables
--------------
This role has several variables that should be filled:
* ninja_when: schedule the running of backupninja.
* ninja_backupname: name of the temporal TAR.
* ninja_backupname_def: name of the definitive TAR.
* ninja_backupdir: the location of the temporal TAR.
* ninja_backupdir_def: The final location of the whole backup.
* ninja_compress: method to compress the backups.
* ninja_includes: list of folders to be copied into the backup.
* ninja_excludes: list of the directories to be excluded by default.
* ninja_mysql_hotcopy: To use _hotcopy_ in MySQL or not.
* ninja_mysql_sqldump: To use sqldump as way to backup MySQL.
* ninja_mysql_compress: To compress or not the mysql dump.
* ninja_mysql_dbhost: The host to connect and do the backup.
* ninja_mysql_backupdir: The location of the MySQL backup.
* ninja_mysql_databases: The list of databases to be copied.
* ninja_mysql_username: The user to be used to do the MySQL backups.
* ninja_mysql_password: The password to be used to do the MySQL backups.


Dependencies
------------

This role has no dependencies

Example Playbook
----------------

```yaml
---
- name: Deploy backupninja to backup a MySQL and some folders in Debian
  hosts: my-own-server
  become: true
  vars:
    - ninja_backupname: "files"
    - ninja_backupname_def: "my-own-server"
    - ninja_backupdir: "/tmp/backups"
    - ninja_backupdir_def: "/var/lib/backups"
    - ninja_includes: "/var/www/nextcloud"
    - ninja_mysql_backupdir: "/tmp/backups"

  roles:
    - role: backupninja
```

```yaml
---
- name: Deploy backupninja to backup a MySQL and some folders in CentOS
  hosts: my-own-server
  become: true
  vars:
    - ninja_backupname: "files"
    - ninja_backupname_def: "my-own-server"
    - ninja_backupdir: "/tmp/backups"
    - ninja_backupdir_def: "/var/lib/backups"
    - ninja_includes: "/var/www/nextcloud"
    - ninja_mysql_username: "bckadmin"
    - ninja_mysql_userpassword: "mysuperhardtorememberpassword"
    - ninja_mysql_backupdir: "/tmp/backups"

  roles:
    - role: backupninja
```

License
-------

GPLv3

Author Information
------------------
Tangelov - https://tangelov.me

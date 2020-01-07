Role Name
=========

This role will install and configure backupninja based on my own needs. It uses a temporal folder to create a full backup of a list of directories and encrypt it using GPG. My recommendation is to use it to backup config files and databases to do a quick disaster recovery plan in small servers and PCs.

Requirements
------------

To use this role you should have installed:
* tar, gzip

Role Variables
--------------

| Variables   |      Description      |  Type |
|----------|:-------------|:------|
| ninja\_when | Time Scheduler for Backupninja | String |
| ninja\_backupname |  Name of a temporal TAR file | String |
| ninja\_backupname\_def | Name of the definitive TAR file | String |
| ninja\_backupdir | Path with the location of the temporal TAR file | String |
| ninja\_backupdir\_def | Path with the location of the definitive TAR file | String |
| ninja\_compress | Method to compress the backups done with Backupninja | String |
| ninja\_includes | List of folders to be saved by the backup | String |
| ninja\_excludes | List of folder to be excluded by default | String |
| ninja\_mysql\_hotcopy | To use _hotcopy_ in MySQL or not | String |
| ninja\_mysql\_sqldump | To use sqldump as method to backup MySQL | String |
| ninja\_mysql\_compress | To compress the MySQL dump or not | String |
| ninja\_mysql\_dbhost | The host where the database is stored | String |
| ninja\_mysql\_backupdir | Path with the location of the MySQL backup | String |
| ninja\_mysql\_databases | List of databases to be saved in the backup. "all" means all databases | String |
| ninja\_mysql\_username | The user to backup the MySQL databases | String |
| ninja\_mysql\_password | The password of the user to connect to MySQL server | String |
| ninja\_gpg\_encryption\_enabled | Boolean to enable the use of GPG cypher in the final step | Boolean |
| ninja\_gpg\_user | GPG user to encrypt the final backup (_username@domain_) | String |

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

```yaml
---
- name: Deploy backupninja to do an encrypted backup
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
    - ninja_gpg_encryption_enabled: true
    - ninja_gpg_user: "popeye@spinash.org"

  roles:
    - role: backupninja
```

License
-------

GPLv3

Author Information
------------------
Tangelov - https://tangelov.me

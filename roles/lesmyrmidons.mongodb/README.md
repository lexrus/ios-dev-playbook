ansible-role-mongodb
====================

[![Build Status](https://travis-ci.org/lesmyrmidons/ansible-role-mongodb.svg?branch=master)](https://travis-ci.org/lesmyrmidons/ansible-role-mongodb)

Ansible Role - Mongodb on RHEL/CentOS and Debian/Ubuntu.

## Requirements

None.

## Role Variables

For Debian / Ubuntu :

	url_apt_key: "http://keyserver.ubuntu.com/pks/lookup?op=get&search="
	mongodb_repository: "deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen"

To change the list of packages to install:

	mongodb_packages:
	  - mongodb-org

## Example Playbook

    - hosts: nosql
      roles:
        - { role: lesmyrmidons.mongodb }

## License

MIT / BSD
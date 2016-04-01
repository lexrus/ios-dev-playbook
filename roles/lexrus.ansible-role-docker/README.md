ansible-role-docker
=========

An Ansible role to install Docker in Debian or Ubuntu.

https://docs.docker.com/engine/installation/linux/debian/

Requirements
------------

64bit Debian / Ubuntu

installation
------------

    ansible-galaxy install lexrus.ansible-role-docker

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: lexrus.ansible-role-docker }

License
-------

BSD

Author Information
------------------

[Lex Tang](http://lexrus.com)([@lexrus](https://twitter.com/lexrus))

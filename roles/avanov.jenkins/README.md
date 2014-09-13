avanov.jenkins
==============================

Ansible role for Jenkins CI

Install it with the following command:

```bash
$ ansible-galaxy install avanov.jenkins
```

Requirements
------------

None

Role Variables
--------------

Here is the list of all variables and their default values:

* ``jenkins_name: jenkins``
* ``jenkins_user: jenkins``
* ``jenkins_group: "{{ jenkins_user }}"``
* ``jenkins_http_port: 8080``
* ``jenkins_home_path: /var/lib/jenkins``
* ``jenkins_java_path: /usr/bin/java``
* ``jenkins_servlet_prefix: /``
* ``jenkins_pidfile: /var/run/jenkins/jenkins.pid``


Dependencies
------------

None

Example Playbook
-------------------------

    - hosts: servers
      roles:
         - { role: avanov.jenkins, jenkins_http_port: 8888 }

License
-------

MIT

Author Information
------------------

Maxim Avanov (https://maximavanov.com)
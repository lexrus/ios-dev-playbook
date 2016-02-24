Phabricator
=========

Phabricator installer to connect to an existing db or run mysql on the same box.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

    protocol: http
    server_url: secure.vagrant.dev
    web_root: /var/www
    database_config:
      user: phabricator
      pass: secret
      host: 127.0.0.1
    php_ini_config:
      timezone: America/New_York
      post_max_size: 32M
      validate_timestamps: 0

Example Playbook
----------------

Simple playbook that is enabled for use of clustering. Never use the default key in production:

    ---
    - hosts: localhost
      sudo: yes
      gather_facts: yes
      roles:
        - phabricator

License
-------

MIT

Author Information
------------------

Produced by NoWait

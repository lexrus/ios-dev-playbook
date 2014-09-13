add-ssh-keys-from-github
========================

Given a list of GitHub usernames, this Ansible role downloads their SSH public
keys from GitHub and adds them to `~/.ssh/authorized_keys`.

Requirements
------------

* `httplib2` - installed automatically via PIP

Role Variables
--------------

    add_ssh_keys_from_github:
      usernames:
        - alice
        - bob
        - carol

License
-------

BSD

Author Information
------------------

George Miroshnykov <george.miroshnykov@gmail.com>

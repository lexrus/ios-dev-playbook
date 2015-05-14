dependencies
============

The seafile.yml example playbook deploys seafile with nginx as frontend reverse
proxy and ssl terminator.

It deploys the a mysql server (using the Galaxy role bennojoy.mysql) and also 
enables fastcgi and webdav.

For nginx, it needs the Ginsys.nginx role, which is a fork of bennojoy's nginx
role.


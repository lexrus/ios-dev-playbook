# iOS Dev Playbook

[![Build Status](https://img.shields.io/travis/lexrus/ios-dev-playbook/master.svg?style=flat)](https://travis-ci.org/lexrus/ios-dev-playbook)
[![GitHub tag](https://img.shields.io/github/tag/lexrus/ios-dev-playbook.svg?style=flat)](https://github.com/lexrus/ios-dev-playbook)
![License](https://img.shields.io/github/license/lexrus/ios-dev-playbook.svg?style=flat)

作为一个 iOS 开发人员，会一些基础的运维技术能使工作流更加顺，并为创业团队节省不少运维成本。
这个 [Ansible](http://www.ansible.com) Playbook 的仓库，可以用来快速配置 iOS 开发需要的一些服务。
当然，如果经费充裕，直接使用优质的收费服务更省时省力。

因为精力有限，大部分配置只在 64bit __Debian Jessie__(Debian 8) 上跑通部署测试，
理论上 Ubuntu 14.04 以上也能用。
请先阅读 [Ansible 的入门文档](http://docs.ansible.com)，不然遇到问题可能会没有方向。
如果你用 macOS，建议在 [Dash](http://kapeli.com/dash) 里安装 Ansible 的文档。

## 服务列表

#### [Docker](https://docker.com) `rake docker`
目前大部分服务都没有运行在 Docker 里。
理想的运行方式是每一个服务都以 Docker container 的形式运行，互不干扰。等有空了再改。

#### [Gogs](http://gogs.io) :443 `rake gogs`
用 Go 语言编写的 Git 服务，特点是功能精简和速度快，树莓派也能流畅运行。
我自己就在用，用的人比较少的话内存占用稳定在 100M 左右。
`rake gogs` 安装后默认开了注册功能，如果要禁用，运行 `rake gogsdr` 即可。
新版本升级后，再运行 `rake gogs` 和 `rake gogsdr` 可以自动完成升级。
这个 role 默认会用 [le.sh](https://github.com/Neilpang/le) 自动生成 [LetsEncrypt](https://letsencrypt.org) 的 SSL 证书，
每隔 80 天自动更新证书。
如果不想用 SSL 可以加上 `SSL=false` 这个参数。

#### [GitLab](https://github.com/gitlabhq/gitlabhq) :80 `rake gitlab`
知名的开源 Git 服务，特点是功能全面。
安装完成后默认用户名是 `root`, 密码为 `5iveL!fe`。
GitLab 对内存有一定要求，建议使用最少 1G 内存的主机。
另外，如果已经成功安装，再次运行 `rake gitlab` 可进行数据备份和程序升级。
手动操作可以看[官方的说明](https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/doc/update.md)。

#### [Jenkins](http://jenkins-ci.org) :8080 `rake jenkins`
开源的持续集成服务，很多人用它来做自动编译打包 IPA 的事。
不过界面不好看，我个人更喜欢 Atlassian Bamboo。

#### [Ghost](https://ghost.org/) :443 `rake ghost`
如果你想同时建一个 Blog 记录开发中的心得或者创业的艰辛，Ghost 是个不错的工具。
它比 Wordpress 更轻巧，皮肤也都非常简洁。
这个 role 使用 [Caddy](https://caddyserver.com) 提供了 HTTP2 支持，并自动生成 LetsEncrypt 的免费 SSL 证书。
默认会自动装上这些皮肤: [ghostium](https://github.com/oswaldoacauan/ghostium)、[ghostrayder](https://github.com/k9ordon/ghostrayder)、[ghostwriter](https://github.com/roryg/ghostwriter)、[GhostScroll](https://github.com/grmmph/GhostScroll)、[Readium](https://github.com/starburst1977/Readium)

#### [Uptime](http://www.redotheweb.com/uptime/) :8082 `rake uptime`
默认用户 `root`，密码 `admin`。
非常轻巧的服务器可用率监控服务，监控小团队的服务可用率肯定是够了。
如果不想自己搭的话推荐用完全免费的 [UptimeRobot](https://uptimerobot.com) 代替。
更全面的监控应该用
[Munin](http://munin-monitoring.org) /
[Nagios](http://www.nagios.org) /
[Sensu](http://sensuapp.org) 等工具实现。

#### [Ajenti](http://ajenti.org) :8000 `rake ajenti`
这是服务器管理工具，功能全，比较重。
如果喜欢把所有服务都装在一起的话，装上这个也不错。默认用户 `root`，密码 `admin`。
Ajenti 强烈建议使用 SSL 连接，但是 Safari 访问非 443 端口使用自签证书的服务器会比较麻烦，所以我暂时禁用了，可以进管理界面打开。
不使用 SSL 有安全隐患，请避免在生产环境使用这样的配置。
另外，重签证书可以用 `ajenti-ssl-gen hostname.com -f; service ajenti restart`;

#### [Huginn](https://github.com/cantino/huginn) :5000 `rake huginn`
算是 IFTTT 的 geek 版本，可以用来定制各种触发条件，可以自动完成很多事。
默认用户 `admin`，密码 `password`。

#### [S🀫🀫🀫🀫🀫🀫🀫🀫🀫s](https://github.com/clowwindy/shadowsocks)
此处打码一百字。

#### [haproxy](http://www.haproxy.org) `rake haproxy`
代理 Gmail，装完后设置本地的 `/etc/hosts`，加上:
```
__YOUR_SERVER_IP__   smtp.gmail.com
__YOUR_SERVER_IP__   pop.gmail.com
__YOUR_SERVER_IP__   imap.gmail.com
```


## 使用方法

### 通过 SSH 远程配置，通常是用 Mac 操作远程服务器

1. `sudo pip install ansible docker-py` - 安装 Ansible
1. `git clone https://github.com/lexrus/ios-dev-playbook.git` - 下载项目
1. `cd ios-dev-playbook` - 进入目录
1. `cp ansible_hosts.ini{.example,}` - 复制 ansible_hosts.ini.example 到 ansible_hosts.ini，然后修改相应的服务器地址
1. 如果要备份这些配置，可以用 `rake dropbox`，它会把重要的配置备份到 `~/Dropbox/.ios-dev-playbook` 目录下
1. 确保你的服务器可以用 [SSH key 验证登录](http://www.debian-administration.org/article/530/SSH_with_authentication_key_instead_of_password)
1. 安装相应的服务，如 GitLab: `rake gitlab`，更多命令用 `rake -T` 列出
1. 如果遇到问题可以试着用 `rake deps` 更新第三方 roles，用 [Ansible Galaxy](https://galaxy.ansible.com) 更新依赖的 roles([.ansible_galaxy_dependencies](https://github.com/lexrus/ios-dev-playbook/blob/master/.ansible_galaxy_dependencies))

### 在当前主机上做本地配置，适合 Debian 或 Ubuntu 单机手动操作

1. `sudo apt-get install ansible docker-py git python python-setuptools python-pip`
1. `sudo pip install ansible docker-py` - 安装 Ansible
1. `git clone https://github.com/lexrus/ios-dev-playbook.git` - 下载项目
1. `cd ios-dev-playbook` - 进入目录
1. `ansible-playbook 059_uptime.yml -i ansible_localhost.ini` - 安装相应的服务

## 注意事项

1. 备份策略是: 等有空了再备份 @__@#
2. 各个服务的使用方法这里就不赘述了，我在上面的列表里加了相应的链接;
5. 端口都是 :80 的服务不能装在一起，再设置一个二级域名吧;

## 测试

测试需要 [Vagrant](https://www.vagrantup.com/)，在本项目目录中 `rake test_ubuntu` 就会拉一个 ubuntu/trusty64 的镜像试着跑大部分配置，测 Debian Jessie 请用 `rake test_debian`。
如果你用的是 macOS，推荐先装 [Brew](http://brew.sh) 和 [Cask](http://caskroom.io)，然后运行 `brew cask install vagrant virtualbox`。
Vagrant 测试的 roles 都写在 [tests/vagrant_test.yml](https://github.com/lexrus/ios-dev-playbook/blob/master/tests/vagrant_test.yml) 里了。

本地用 Vagrant 测试会消耗很多时间，尤其是在网速不理想的情况下。并且，请确保你的电脑有至少 2G 的空闲内存。

Travis 设置了测试 playbook 的语法是否正确，以及 `001_common_utilities.yml` 是否能顺利跑通。

## 上哪搞服务器?

欢迎你使用我的推广链接注册自己的虚拟服务器：

[我的 DigitalOcean 推广链接](https://www.digitalocean.com/?refcode=3eb5cf371fc9) 新加坡节点延时都很低，每月 5 刀起，通过推广链接注册就送 10 刀。

[我的 Linode 推广链接](http://www.linode.com/?r=9f144941e797d495a10c2841c3137ce1acde5f15) Linode 服务非常稳定，性能也不错。

[我的 Vultr 推广链接](http://www.vultr.com/?ref=6822054) 最低每月 5 刀，使用优惠码 SSDVPS 就送 20 刀。


## 协议

本项目的源码遵循 MIT 协议，详见 `LICENSE` 文件。

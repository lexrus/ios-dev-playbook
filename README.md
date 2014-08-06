# ios-dev-playbook

这是一个 [Ansible](http://www.ansible.com) playbook 的仓库，可以用它快速配置好你的服务器(目前只支持 Debian Wheezy/testing)，同时可以用来安装以下服务端(没勾勾的还没好)：

- [x] Countly Server (master)
- [x] GitLab 7.1
- [x] Shadowsocks
- [x] COW
- [ ] Jenkins - 还没测试过
- [ ] Redmine
- [ ] Ghost
- [ ] Wordpress
- [ ] LoopBack
- [ ] APNS
- [ ] Seafile / ownCloud
- [ ] QuincyKit Server
- [ ] Munin - 需要么？
- [ ] Nagios - 不需要么？
- [ ] Sensu - 真的要这么强大么？

请先阅读 [Ansible 的入门文档](http://docs.ansible.com)，不然遇到问题可能会没有方向。
如果你用 Mac OS X，建议你在 [Dash](http://kapeli.com/dash) 里安装 Ansible 的文档。

## 使用方法

1. 先安装 Ansible: ```sudo pip install ansible```;
2. 用 [Ansible Galaxy](https://galaxy.ansible.com) 安装本仓库中的依赖([ansible_galaxy_dependencies.txt](https://github.com/lexrus/ios-dev-playbook/blob/master/ansible_galaxy_dependencies.txt)): ```rake init```;
3. 复制 ansible_hosts.example 到 ansible_hosts 后修改相应的服务器地址;
4. 确保你的服务器可以用 [SSH key 验证登录](http://www.debian-administration.org/article/530/SSH_with_authentication_key_instead_of_password);
5. 安装相应的服务，如 GitLab: ```rake gitlab```，更多命令用 ```rake -T``` 列出。

## 备份

~~暂未实现~~

## 已知问题

1. 从源码编译安装 nodejs 非常慢，之后会考虑用 deb 包安装；
2. 使用方法应该更无脑，Rakefile 有待改进。

## 测试

测试需要 Vagrant，在本项目目录中 ```rake test``` 就会拉一个 ubuntu/trusty64 的镜像试着跑大部分配置。
如果你用的是 Mac OS X，推荐先装 [Brew](http://brew.sh) 和 [Cask](http://caskroom.io)，然后运行 ```brew cask install vagrant virtualbox```。
Vagrant 测试的 roles 都写在 [VagrantTest.yml](https://github.com/lexrus/ios-dev-playbook/blob/master/VagrantTest.yml) 里了。

## 上哪搞服务器?

欢迎你使用我的推广链接注册自己的虚拟服务器：

[我的 DigitalOcean 推广链接](https://www.digitalocean.com/?refcode=3eb5cf371fc9) (使用优惠码 ```10TOSHIP``` 注册就送 10 刀) 新加坡和旧金山节点延时都很低，每月 5 刀起。

[我的 Linode 推广链接](http://www.linode.com/?r=9f144941e797d495a10c2841c3137ce1acde5f15) Linode 虽然贵一点(每月 10 刀起)，但是服务非常稳定，性能也不错。

## 为什么不用 Chef 或 Puppet?

Chef 做这事更合适，但是 Ansible 的 YML 相对更容易编写，上手快。

## 反馈

请 [提 issue](https://github.com/lexrus/ios-dev-playbook/issues/new) 或者在 Twitter 上 [@lexrus](https://twitter.com/lexrus)。

## 协议

```
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.

```
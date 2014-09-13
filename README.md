# ios-dev-playbook

这是一个 [Ansible](http://www.ansible.com) playbook 的仓库，可以用它快速配置好你的 Debian 或 Ubuntu，同时可以用来安装以下服务端(没勾勾的还没好)：

- [x] [Countly Server](https://github.com/Countly/countly-server)
- [x] [GitLab](https://github.com/gitlabhq/gitlabhq) 7.2 (用户名: "root", 初始密码: "5iveL!fe")
- [x] [Shadowsocks](https://github.com/clowwindy/shadowsocks)
- [x] [COW](https://github.com/cyfdecyf/cow)
- [x] [Jenkins](http://jenkins-ci.org)
- [ ] [Wordpress](http://wordpress.org)
- [ ] [Ghost](https://github.com/TryGhost/Ghost)
- [ ] [LoopBack](http://loopback.io)
- [ ] [Uniqush](http://uniqush.org) (APNS)
- [ ] [QuincyKit](https://github.com/therealkerni/QuincyKit)
- [ ] [Mail-in-a-Box](https://github.com/mail-in-a-box/mailinabox)
- [ ] [Munin](http://munin-monitoring.org) / [Nagios](http://www.nagios.org) / [Sensu](http://sensuapp.org)

请先阅读 [Ansible 的入门文档](http://docs.ansible.com)，不然遇到问题可能会没有方向。
如果你用 Mac OS X，建议你在 [Dash](http://kapeli.com/dash) 里安装 Ansible 的文档。


## 使用方法

1. 先安装 Ansible: ```sudo pip install ansible```;
2. 复制 ansible_hosts.example 到 ansible_hosts 后修改相应的服务器地址;
3. 确保你的服务器可以用 [SSH key 验证登录](http://www.debian-administration.org/article/530/SSH_with_authentication_key_instead_of_password);
4. 安装相应的服务，如 GitLab: ```rake countly```，更多命令用 ```rake -T``` 列出。
5. 如果遇到问题可以试着更新第三方 roles，用 [Ansible Galaxy](https://galaxy.ansible.com) 更新依赖的 roles([ansible_galaxy_dependencies.txt](https://github.com/lexrus/ios-dev-playbook/blob/master/ansible_galaxy_dependencies.txt)): ```rake init```;</del>


## 注意事项

1. 暂时没有备份策略;
2. 各个服务的使用方法这里就不赘述了，我在上面的列表里加了相应的链接;
3. GitLab 对内存有一定要求，建议使用最少 1G 内存的主机，不过我在执行 GitLab 的 role 前加了设置 swap 等于两倍内存的 role，一般 512M 内存的 VPS 也能撑住 5 人以下的小团队。


## 测试

测试需要 Vagrant，在本项目目录中 ```rake test``` 就会拉一个 ubuntu/trusty64 的镜像试着跑大部分配置。
如果你用的是 Mac OS X，推荐先装 [Brew](http://brew.sh) 和 [Cask](http://caskroom.io)，然后运行 ```brew cask install vagrant virtualbox```。
Vagrant 测试的 roles 都写在 [VagrantTest.yml](https://github.com/lexrus/ios-dev-playbook/blob/master/VagrantTest.yml) 里了。


## 上哪搞服务器?

欢迎你使用我的推广链接注册自己的虚拟服务器：

[我的 DigitalOcean 推广链接](https://www.digitalocean.com/?refcode=3eb5cf371fc9) 新加坡节点延时都很低，每月 5 刀起，通过推广链接注册就送 10 刀。

[我的 Linode 推广链接](http://www.linode.com/?r=9f144941e797d495a10c2841c3137ce1acde5f15) Linode 虽然贵一点(每月 10 刀起)，但是服务非常稳定，性能也不错。


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
# ios-dev-playbook

这是一个 [Ansible](http://www.ansible.com) playbook 的仓库，可以用它快速配置 iOS 开发需要的服务器，仅支持 Debian 和 Ubuntu。请先阅读 [Ansible 的入门文档](http://docs.ansible.com)，不然遇到问题可能会没有方向。如果你用 Mac OS X，建议在 [Dash](http://kapeli.com/dash) 里安装 Ansible 的文档。

目前可以安装的服务有(没勾勾的还没好)：

- [x] [Countly Server](https://github.com/Countly/countly-server)
- [x] [GitLab](https://github.com/gitlabhq/gitlabhq) 7.5.3 (用户名: `root`, 初始密码: `5iveL!fe`)
- [x] [Shadowsocks](https://github.com/clowwindy/shadowsocks)
- [x] [COW](https://github.com/cyfdecyf/cow)
- [x] [Jenkins](http://jenkins-ci.org) (默认在 8080 端口，设置在 `011_jenkins.yml`)
- [x] [Ghost](https://ghost.org/)
- [x] [NewRelic](https://newrelic.com) agent
- [ ] [Phabricator](http://phabricator.org)
- [ ] [Wordpress](http://wordpress.org)
- [ ] [LoopBack](http://loopback.io)
- [ ] [Uniqush](http://uniqush.org) (APNS)
- [ ] [QuincyKit](https://github.com/therealkerni/QuincyKit)
- [ ] [Mail-in-a-Box](https://github.com/mail-in-a-box/mailinabox)
- [ ] [Munin](http://munin-monitoring.org) / [Nagios](http://www.nagios.org) / [Sensu](http://sensuapp.org)


## 使用方法

1. `sudo pip install ansible` - 安装 Ansible
1. `git clone https://github.com/lexrus/ios-dev-playbook.git` - 下载项目
1. `cd ios-dev-playbook` - 进入目录
1. `cp ansible_hosts{.example,}` - 复制 ansible_hosts.example 到 ansible_hosts，然后修改相应的服务器地址
1. 确保你的服务器可以用 [SSH key 验证登录](http://www.debian-administration.org/article/530/SSH_with_authentication_key_instead_of_password)
1. 安装相应的服务，如 GitLab: `rake countly`，更多命令用 `rake -T` 列出
1. 如果遇到问题可以试着用 `rake init` 更新第三方 roles，用 [Ansible Galaxy](https://galaxy.ansible.com) 更新依赖的 roles([ansible_galaxy_dependencies.txt](https://github.com/lexrus/ios-dev-playbook/blob/master/ansible_galaxy_dependencies.txt))


## 注意事项

1. 备份策略是: 永不备份;
2. 各个服务的使用方法这里就不赘述了，我在上面的列表里加了相应的链接;
3. GitLab 对内存有一定要求，建议使用最少 1G 内存的主机，不过我在执行 GitLab 的 role 前加了设置 swap 等于两倍内存的 role，一般 512M 内存的 VPS 也能撑住 5 人以下的小团队，但是一般运维会建议不要使用 swap；
4. 建议 Web 服务不要装在一起。
5. Ghost 的 role 会自动装上这些 themes: [ghostium](https://github.com/oswaldoacauan/ghostium)、[ghostrayder](https://github.com/k9ordon/ghostrayder)、[ghostwriter](https://github.com/roryg/ghostwriter)、[GhostScroll](https://github.com/grmmph/GhostScroll)、[Readium](https://github.com/starburst1977/Readium)


## 测试

测试需要 Vagrant，在本项目目录中 `rake test` 就会拉一个 ubuntu/trusty64 的镜像试着跑大部分配置。
如果你用的是 Mac OS X，推荐先装 [Brew](http://brew.sh) 和 [Cask](http://caskroom.io)，然后运行 `brew cask install vagrant virtualbox`。
Vagrant 测试的 roles 都写在 [VagrantTest.yml](https://github.com/lexrus/ios-dev-playbook/blob/master/VagrantTest.yml) 里了。


## 赞助

如果你觉得这个项目有用，那就请我喝一杯咖啡吧。我的 PayPal 和支付宝帐号都是: `lexrus@gmail.com`


## 上哪搞服务器?

欢迎你使用我的推广链接注册自己的虚拟服务器：

[我的 DigitalOcean 推广链接](https://www.digitalocean.com/?refcode=3eb5cf371fc9) 新加坡节点延时都很低，每月 5 刀起，通过推广链接注册就送 10 刀。

[我的 Linode 推广链接](http://www.linode.com/?r=9f144941e797d495a10c2841c3137ce1acde5f15) Linode 虽然贵一点(每月 10 刀起)，但是服务非常稳定，性能也不错。


## 反馈

请 [提 issue](https://github.com/lexrus/ios-dev-playbook/issues/new) 或者在 Twitter 上 [@lexrus](https://twitter.com/lexrus)。


## 协议

本项目的源码遵循 MIT 协议，详见 `LICENSE` 文件。
# ios-dev-playbook

这是一个 [Ansible](http://www.ansible.com) playbook 的仓库，可以用它们快速地配置好你的 Debian Wheezy(当然 testing 也行)，同时可以用来安装以下服务端：

- [x] Countly Server (master)
- [x] GitLab 7.1
- [x] Shadowsocks
- [x] COW
- [ ] QuincyKit Server - 还没写进来
- [ ] Jenkins - 还没测试过
- [ ] Munin - 需要么？
- [ ] Nagios - 不需要么？
- [ ] Sensu - 真的不用这么强大的。

请先阅读 Ansible 的入门文档，不然遇到问题可能会没有方向。

## 用法

1. 先安装 Ansible: ```sudo pip install ansible```
2. 安装本仓库中的依赖: ```rake init```
3. 复制 ansible_hosts.example 到 ansible_hosts 后修改相应的服务器地址
4. 安装相应的服务，如 GitLab: ```rake gitlab```

## 已知问题

1. 从源码安装 nodejs 非常慢

## 测试

测试需要 Vagrant，直接 ```rake test``` 就会拉一个 ubuntu/trusty64 的镜像试着跑大部分配置。

## 赞助

欢迎你使用我的推广链接注册自己的虚拟服务器：

[我的 DigitalOcean 推广链接](https://www.digitalocean.com/?refcode=3eb5cf371fc9) (使用优惠码 ```10TOSHIP``` 注册就送 10 刀)

[我的 Lindoe 推广链接](http://www.linode.com/?r=9f144941e797d495a10c2841c3137ce1acde5f15)

## 为什么不用 Chef 或 Puppet?

因为 Ansible 好上手，我写着写着才发现 Chef 做这事更合适。

## 反馈

请发 issue 或者在 Twitter 上 [@lexrus](https://twitter.com/lexrus)。
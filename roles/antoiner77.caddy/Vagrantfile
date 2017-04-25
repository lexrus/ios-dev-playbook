# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.define "jessie" do |jessie|
    jessie.vm.box = "debian/jessie64"
  end

  config.vm.define "precise" do |precise|
    precise.vm.box = "bento/ubuntu-12.04"
  end

  config.vm.define "trusty" do |trusty|
    trusty.vm.box = "bento/ubuntu-14.04"
  end

  config.vm.define "xenial" do |xenial|
    xenial.vm.box = "bento/ubuntu-16.04"
  end

  config.vm.define "centos7" do |centos7|
    centos7.vm.box = "bento/centos-7.3"
  end

  config.vm.define "fedora22" do |fedora22|
    fedora22.vm.box = "bento/fedora-22"
  end

  config.vm.provision "ansible" do |ansible|
      ansible.playbook = 'tests/test.yml'
  end

  $script = <<SCRIPT
  # curl localhost and get the http response code
  while ! curl -Is localhost:2020 -o /dev/null; do
    sleep 1 && echo -n .
  done
  http_code=$(curl --silent --head --output /dev/null -w '%{http_code}' localhost:2020)
  case $http_code in
    200|404) echo "$http_code | Server running" ;;
    000)     echo "$http_code | Server not accessible!" >&2 ;;
    *)       echo "$http_code | Unknown http response code!" >&2 ;;
  esac
SCRIPT
  # Fix 'stdin: is not a tty' error
  config.ssh.pty = true
  config.vm.provision :shell, inline: $script

  config.vm.synced_folder ".", "/vagrant", disabled: true
end

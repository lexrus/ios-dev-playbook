desc "Install dependencies"
task :deps do
  exec "ansible-galaxy install --ignore-errors --force " \
    " --role-file=ansible_galaxy_dependencies.txt"
end

desc "Upgrade to wheezy"
task :prepare do
  exec "ansible-playbook 000_prepare_wheezy.yml -l cloud"
end

desc "Install common utitilies"
task :common do
  exec "ansible-playbook 001_common_utilities.yml"
end

desc "Add SSH keys from GitHub"
task :github_keys do
  exec "ansible-playbook 002_ssh_keys_from_github.yml -l cloud"
end

desc "Set swap on"
task :swapon do
  exec "ansible-playbook 003_swapon.yml"
end

desc "Install Ajenti"
task :ajenti do
  exec "ansible-playbook 009_ajenti.yml"
end

desc "Install Countly server"
task :countly do
  exec "ansible-playbook 012_countly.yml -l countly"
end

desc "Install GitLab server"
task :gitlab do
  exec "ansible-playbook 010_gitlab.yml -l gitlab"
end

desc "Install Jenkins server"
task :jenkins do
  exec "ansible-playbook 011_jenkins.yml -l jenkins"
end

desc "Install Ghost server"
task :ghost do
  exec "ansible-playbook 030_ghost.yml -l ghost"
end

desc "Install cow server"
task :cow do
  exec "ansible-playbook 020_cow_backend.yml -l cow_backend"
end

desc "Install shadowsocks server"
task :shadowsocks do
  exec "ansible-playbook 022_shadowsocks.yml -l shadowsocks"
end

desc "Install & config NewRelic agent"
task :newrelic do
  exec "ansible-playbook 053_newrelic.yml"
end

desc "Install uptime"
task :uptime do
  exec "ansible-playbook 059_uptime.yml -l uptime"
end

desc "Test Ubuntu"
task :test_ubuntu do
  system "VAGRANT_VAGRANTFILE=VagrantfileUbuntu vagrant up --no-provision"
  system "VAGRANT_VAGRANTFILE=VagrantfileUbuntu vagrant provision"
end

desc "Test Debian"
task :test_debian do
  system "VAGRANT_VAGRANTFILE=VagrantfileDebian vagrant up --no-provision"
  system "VAGRANT_VAGRANTFILE=VagrantfileDebian vagrant provision"
end
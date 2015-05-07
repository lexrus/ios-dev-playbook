desc "Sync to/with Dropbox"
task :dropbox do
  exec "ansible-playbook 100_sync_with_dropbox.yml -i ansible_localhost.ini"
end

desc "Install dependencies"
task :deps do
  exec "ansible-galaxy install --ignore-errors --force " \
    " --role-file=.ansible_galaxy_dependencies"
end

desc "Upgrade to jessie"
task :jessie do
  exec "ansible-playbook 000_prepare_jessie.yml -l cloud"
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

desc "Install docker"
task :docker do
  exec "ansible-playbook 004_docker.yml"
end

desc "Install Ajenti"
task :ajenti do
  exec "ansible-playbook 009_ajenti.yml"
end

desc "Install GitLab server"
task :gitlab do
  exec "ansible-playbook 010_gitlab.yml -l gitlab"
end

desc "Install Jenkins server"
task :jenkins do
  exec "ansible-playbook 011_jenkins.yml -l jenkins"
end

desc "Install Countly server"
task :countly do
  exec "ansible-playbook 012_countly.yml -l countly"
end

desc "Install Gogs server"
task :gogs do
  exec "ansible-playbook 013_gogs.yml -l gogs"
end

desc "Disable Registration of Gogs"
task :gogsdr do
  exec "ansible-playbook 014_gogs_disable_registration.yml --tags=config,wait,restart -l gogs"
end

desc "Install Ghost server"
task :ghost do
  exec "ansible-playbook 030_ghost.yml -l ghost"
end

desc "Install cow server"
task :cow do
  exec "ansible-playbook 020_cow_backend.yml -l cow_backend"
end

desc "Install Gem in a Box"
task :geminabox do
  exec "ansible-playbook 040_geminabox.yml -l geminabox"
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

desc "Install Huginn"
task :huginn do
  exec "ansible-playbook 060_huginn.yml -l huginn"
end

desc "Test Ubuntu"
task :test_ubuntu do
  system "vagrant up ubuntu --no-provision"
  system "vagrant provision ubuntu"
end

desc "Test Debian"
task :test_debian do
  system "vagrant up debian --no-provision"
  system "vagrant provision debian"
end

task :default => [:common]

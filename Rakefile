desc "Install dependencies"
task :init do
  exec "sudo ansible-galaxy install --role-file=ansible_galaxy_dependencies.txt --ignore-errors"
end

desc "Upgrade to wheezy"
task :prepare do
  exec "ansible-playbook 000_prepare_wheezy.yml -l cloud"
end

desc "Install common utitilies"
task :common do
  exec "ansible-playbook 001_install_common_utilities.yml"
end

desc "Add SSH keys from GitHub"
task :github_keys do
  exec "ansible_playbook 002_add_ssh_keys_from_github.yml -l cloud"
end

desc "Set swap on"
task :swapon do
  exec "ansible-playbook 003_swapon.yml"
end

namespace :test do

  desc "Test all"
  task :all do
    `vagrant up`
    `vagrant provision`
  end

end
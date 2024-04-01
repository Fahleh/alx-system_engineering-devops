# Configures a  server with custome HTTP header.

exec {'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
  before   => Exec['add_header'],
}

exec { 'add_header':
  environment => ["HOST=${hostname}"],
  provider => shell,
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}

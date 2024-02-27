# This Puppet manifest configures a new Ubuntu machine

class nginx_install {
  package { 'nginx':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "
      server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html;
        server_name _;
        location / {
          try_files \$uri \$uri/ =404;
        }
        location /redirect_me {
          return 301 https://www.example.com;
        }
      }
    ",
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}

include nginx_install

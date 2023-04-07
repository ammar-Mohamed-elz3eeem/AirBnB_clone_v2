# puppet web static set up

package { 'nginx':
  ensure   => installed,
  provider => 'apt'
}

file { '/data':
  ensure => 'directory',
  group  => 'ubuntu',
  owner  => 'ubuntu'
}

file { '/data/web_static':
  ensure => 'directory'
}

file { '/data/web_static/releases':
  ensure => 'directory'
}

file { '/data/web_static/shared':
  ensure => 'directory'
}

file { '/data/web_static/releases/test':
  ensure => 'directory'
}

file { '/data/web_static/current':
  ensure => '/data/web_static/releases/test'
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
}

exec { 'configure nginx':
  command  => 'sed -i "/listen 80 default_server/a location /hbnb_static {alias /data/web_static/current/;}" /etc/nginx/sites-enabled/default',
  provider => 'shell',
  require  => Package['nginx']
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx']
}

# to automate the task of creating a custom HTTP header respons

package { 'nginx':
  ensure => present,
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Holberton School',
  path    => '/var/www/html/index.html'
}

exec { 'redirection 1':
  command  => "sed -i '/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=doF7owZ0blk permanent;'  /etc/nginx/sites-available/default  && service nginx restart",
  provider => 'shell',
}

exec { 'restart nginx':
  command  => 'service nginx restart',
  provider => 'shell',
}

service { 'nginx':
  ensure => running,
  enable => true,
}

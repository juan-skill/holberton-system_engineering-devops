# configure the number of request allowed

exec {'worker_proocess':
  command => "sed -i 's/-n 15/-n 2000/g' /etc/default/nginx; service nginx restart",
  path    => ['/usr/bin', '/bin'],
}

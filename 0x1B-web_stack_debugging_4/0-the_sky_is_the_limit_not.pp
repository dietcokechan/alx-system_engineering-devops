# sky is the limit
exec {'sky is the limit':
  command  => 'echo "ULIMIT=\"-n 25000\"" > /etc/default/nginx && sudo service nginx restart',
  provider => shell,
}

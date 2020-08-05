# Configure SSH client to use private key ~/.ssh/holberton and refuse to authenticate using a password
include stdlib

file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

#!/usr/bin/env bash
# we will be using the puppet to make changes to our configuration file

file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => '  IdentityFile ~/.ssh/school',
  ensure => 'present',
}

file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => '  PasswordAuthentication no',
  ensure => 'present',
}

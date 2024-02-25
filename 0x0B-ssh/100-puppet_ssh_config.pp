#!/usr/bin/env bash
# we will be using the puppet to make changes to our configuration file

file { 'ect/ssh/ssh_cofig':
	ensure = => present,
content =>"
	#ssh client configuration
	host*
	identityFile ~/.ssh/school
	passwordAuthentication no
	"
}

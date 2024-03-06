# File: site.pp

# Check server resources
exec { 'check_server_resources':
  command => 'free -m && df -h',
}

# Update server software
package { 'update_server_packages':
  ensure => 'latest',
}

# Restart Apache service
service { 'apache':
  ensure  => 'running',
  enable  => true,
  require => Package['update_server_packages'],
}

# Restart PHP service
service { 'php':
  ensure  => 'running',
  enable  => true,
  require => Package['update_server_packages'],
}

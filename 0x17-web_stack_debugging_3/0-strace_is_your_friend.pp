# File: site.pp

# Define a class for Apache installation and configuration
class { 'apache':
  service_ensure => 'running',  # Ensure Apache service is running
}

# Define a class for PHP installation and configuration
class { 'php':
  package_ensure => 'present',  # Ensure PHP package is installed
}

# Check and set permissions for the directories used by Apache
file { '/var/www/html':
  ensure => 'directory',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

# Check Apache configuration files for errors
exec { 'check_apache_config':
  command     => 'apache2ctl configtest',
  refreshonly => true,
  notify      => Service['apache'],
}

# Check PHP configuration files for errors
exec { 'check_php_config':
  command     => 'php -v',
  refreshonly => true,
}

# Update server software
package { 'update_server_packages':
  ensure  => 'latest',
  require => Exec['check_apache_config', 'check_php_config'],
}

# Restart Apache service if configuration changes or updates are applied
service { 'apache':
  ensure    => 'running',
  enable    => true,
  subscribe => [File['/var/www/html'], Exec['check_apache_config'], Package['update_server_packages']],
}

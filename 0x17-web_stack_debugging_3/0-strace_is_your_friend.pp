# File: site.pp

# Ensure Apache is installed and running
class { 'apache':
  service_ensure => 'running',
}

# Ensure PHP is installed
class { 'php':
  package_ensure => 'present',
}

# Set up Apache configuration
file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => file,
  content => template('apache/000-default.conf.erb'),
  notify  => Service['apache'],
}

# Set up PHP configuration
file { '/etc/php/5.5/apache2/php.ini':
  ensure  => file,
  content => template('php/php.ini.erb'),
  notify  => Service['apache'],
}

# Restart Apache service after configuration changes
service { 'apache':
  ensure    => 'running',
  enable    => true,
  subscribe => [File['/etc/apache2/sites-available/000-default.conf'], File['/etc/php/5.5/apache2/php.ini']],
}

# File: site.pp

# Ensure Apache is installed and running
class { 'apache':
  service_ensure => 'running',
}

# Ensure PHP is installed
class { 'php':
  package_ensure => 'present',
}

# Define the path to the WordPress settings file
$wordpress_settings_file = '/var/www/html/wp-settings.php'

# Manage the WordPress settings file
file { $wordpress_settings_file:
  ensure  => file,
  content => inline_template("
<?php
# Managed by Puppet

# Read the current content of the file
${current_content} = file_get_contents('${wordpress_settings_file}');

# Replace 'phpp' extensions with 'php'
${new_content} = str_replace('phpp', 'php', ${current_content});

echo ${new_content};
"),
  notify  => Service['apache'],
}

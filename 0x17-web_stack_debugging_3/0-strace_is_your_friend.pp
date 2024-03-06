# File: site.pp

# Replaces occurrences of 'phpp' extensions with 'php' in the WordPress file `wp-settings.php`.

exec { 'fix-wordpress-file':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

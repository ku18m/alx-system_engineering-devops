#!/usr/bin/pup
#install flask from pip3 v2.1.0
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

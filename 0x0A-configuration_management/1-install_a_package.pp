# Puppet manifest to install Flask package from pip3

# Define package resource to install Flask and Werkzeug
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.1.1',  # Specify the version required by Flask 2.1.0
  provider => 'pip3',
}

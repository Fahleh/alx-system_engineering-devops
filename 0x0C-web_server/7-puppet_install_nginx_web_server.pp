#setup nginx

package {
    'nginx':
    ensure => installed,
}

file {'/var/www/html/index.nginx-debian.html':
    content => 'Hello World!',
}

file_line {'configure redirection':
    path  =>  '/etc/nginx/sites-available/default',
    after =>  'server_name _;',
    line  =>  "\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=2bI8XsdNb-c&list=PLVipAi3U-Jos-gFKT434UTj2D9x7t83IH;\n\t}\n",
}

service {'nginx':
    ensure => running,
}

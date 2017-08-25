#!/bin/sh
exe_user=www
exe_group=www
pcre_path=/usr/local/pcre
openssl=/usr/local/openssl

cd /work/systools/nginx/

./configure --with-http_stub_status_module \
--with-http_ssl_module \
--with-http_gzip_static_module \
--with-http_spdy_module \
--user=$exe_user \
--group=$exe_group
--with-openssl=$openssl \
--with-pcre=$pcre_path \

make
make install

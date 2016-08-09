#!/usr/bin/env bash
sudo service nginx stop
/<your_path>/letsencrypt/letsencrypt-auto certonly -t -d <domain_name> --renew-by-default
sudo service nginx restart

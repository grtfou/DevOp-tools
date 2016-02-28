#!/usr/bin/env bash
sudo service nginx stop
/<your_path>/letsencrypt/letsencrypt-auto certonly -t -d <domain_name> --renew
sudo service nginx restart

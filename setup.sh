#!/bin/bash

sudo chmod +x renew_cert.sh cleanup.sh
(crontab -l; echo "0 0 1 */2 * bash ./todo_app/renew_cert.sh"; echo "0 0 * * * bash ./todo_app/cleanup.sh") | crontab -

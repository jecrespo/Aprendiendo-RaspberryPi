#!/bin/bash
cd /home/pi
raspistill -o imagen.jpg
sftp -oPort=22 open user@www.server.com <<EOF
user usuario
password secreta
put imagen.jpg
EOF
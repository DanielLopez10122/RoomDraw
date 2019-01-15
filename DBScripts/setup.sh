#!/bin/sh

USER="$1"

# if for some reason we decide to change the sql user
if [ -z "$USER" ]; then
	USER="root"
fi

cat *.sql | mysql -u root -p


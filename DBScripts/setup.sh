#!/bin/sh

USER="$1"

# if for some reason we decide to change the sql user
if [ -z "$USER" ]; then
	USER="root"
fi

rm generated.sql
cat *.sql procs/*.sql | tee generated.sql | mysql -u $USER -p

#!/bin/sh

. ./common.sh

GET /rooms?dorm=0 $@
echo

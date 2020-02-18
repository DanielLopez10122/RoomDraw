#!/bin/sh

HOST="localhost"
PORT="8000"
HEADER_FILE="default_headers"

while getopts "h:" args; do
	case "$args" in
		h)
			HEADER_FILE="$OPTARG";;
	esac

done
shift $((OPTIND-1))

GET() {
	path="$1"
	shift 1
	curl -L -H @$HEADER_FILE ${HOST}:${PORT}/${path} $@
}

DELETE() {
	path="$1"
	shift 1
	curl -L -X DELETE -H @$HEADER_FILE ${HOST}:${PORT}/${path} $@
}

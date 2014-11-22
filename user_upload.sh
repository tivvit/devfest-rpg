#!/bin/bash

curl -i \
-H "Accept: application/json" \
-H "Content-Type:application/json" -X \
POST --data '{"name": $1, "email": $2}' "https://practical-well-728.appspot.com/_ah/api/devfest_cdh_api/v1/user"

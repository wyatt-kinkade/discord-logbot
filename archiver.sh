#!/bin/bash

DATE=`date "+%F-%T"`
FILEPATH='/var/log/discord/discord.log'

mv "$FILEPATH" "$FILEPATH-$DATE"

gzip "$FILEPATH.log-$DATE"

echo "$FILEPATH-$DATE Archived"

#!/bin/bash

DATE=`date "+%F-%T"`
FILEPATH='/var/log/discord/discord.log'

action () {
mv "$2" "$2-$1"

gzip "$2-$1"

echo "$2-$1 Archived"
}
FILEPATH='/var/log/discord/discord.log'
action "$DATE" "$FILEPATH"
FILEPATH='/var/log/discord/discord_audit.log'
action "$DATE" "$FILEPATH"


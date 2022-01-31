# discord-logbot
Figured to spin a rough utility up for logging in a few discord servers, spent a little extra time to package everything up for deployment

## Install Process
You're expected to know basics on discord bots and systemd, if you're working with an alternative init system you'll need to adjust your init system accordingly. archiver.sh is technically optional but reccomended

```
git clone https://github.com/wyatt-kinkade/discord-logbot.git
cd discord-logbot
```

Edit `archiver.sh` and `settings.yaml` with the correct filepaths/filenames as well as the bot token from the developer portal where needed. Defaults have been set for the file locations

```
chmod +x archiver.sh
chmod +x discordlogger.py
sudo cp archiver.sh /bin/
sudo cp discordlogger.py /bin/
sudo mkdir /etc/discordlogger/
sudo cp settings.yaml /etc/discordlogger/
sudo cp discordlogger.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start discordlogger.service
sudo systemctl status discordlogger.service
```


Add the following line to the root user's crontab using `sudo crontab -e`
`0 0 * * * /bin/archiver.sh`

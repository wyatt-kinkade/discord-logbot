#!/usr/bin/python3
import discord
import random
import os
import yaml
from datetime import datetime

client = discord.Client()

def var_load():
    with open("/etc/discordlogger/settings.yaml", "r") as stream:
        try:
            settings = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return settings

def logdir():
    if not os.path.isdir(path):
        os.mkdir(path)

def teefunc(i):
    print(i)
    f = open(path + filename, "a")  # append mode
    f.write( i + "\n")
    f.close()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.invisible)
    log = 'We have logged in as {0.user}'.format(client)
    teefunc(log)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content
    channel = message.channel
    author = message.author
    guild = message.guild
    msg_datetime = message.created_at
    time = msg_datetime.strftime("%m/%d/%Y, %H:%M:%S")
    msg_id = str(message.id)
    log = "[" + time + "]" + author.name + "#" + author.discriminator + " said '" + content + "' in " + channel.name + " in " + guild.name + " - Message ID: " + msg_id 

    if len(message.embeds) > 0:
        embed_list_raw = message.embeds
        embed_list = [discord.Embed.to_dict(embed) for embed in embed_list_raw]
        log = log + " with the following embeds " + str(embed_list)

    if len(message.attachments) > 0:
        attachment_list = message.attachments
        url_list = [attachment.url for attachment in attachment_list]
        log = log + " with the following attachments " + ' '.join(url_list)

    teefunc(log)

@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return

    content = message.content
    channel = message.channel
    author = message.author
    guild = message.guild
    msg_datetime = datetime.now()
    time = msg_datetime.strftime("%m/%d/%Y, %H:%M:%S")
    msg_id = str(message.id)
    log = "[" + time + "]" + author.name + "#" + author.discriminator + " deleted '" + content + "' from " + channel.name + " in " + guild.name + " - Message ID: " + msg_id

    if len(message.embeds) > 0:
        embed_list_raw = message.embeds
        embed_list = [discord.Embed.to_dict(embed) for embed in embed_list_raw]
        log = log + " with the following embeds " + str(embed_list)

    if len(message.attachments) > 0:
        attachment_list = message.attachments
        url_list = [attachment.url for attachment in attachment_list]
        log = log + " with the following attachments " + ' '.join(url_list)

    teefunc(log)

@client.event
async def on_message_edit(before, after):
    if before.author == client.user: 
        return

    before_content = before.content
    after_content = after.content
    channel = before.channel
    author = before.author
    guild = before.guild
    msg_datetime = after.edited_at
    time = msg_datetime.strftime("%m/%d/%Y, %H:%M:%S")
    msg_id = str(after.id)
    log = "[" + time + "]" + author.name + "#" + author.discriminator + " changed a post from '" + before_content + "' to '" + after_content + "' in " + channel.name + " in " + guild.name + " - Message ID: " + msg_id 

    if len(before.embeds) > 0:
        embed_list_raw = before.embeds
        embed_list = [discord.Embed.to_dict(embed) for embed in embed_list_raw]
        log = log + " with the following embeds " + str(embed_list)

    if len(before.attachments) > 0:
        attachment_list = before.attachments
        url_list = [attachment.url for attachment in attachment_list]
        log = log + " with the following attachments " + ' '.join(url_list)

    teefunc(log)

settings = var_load()
token = settings['token']
path = settings['path']
filename = settings['filename']
logdir()
client.run(token)

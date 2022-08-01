import os
import yaml

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

def audit_teefunc(i):
    print(i)
    f = open(path + audit_log, "a")  # append mode
    f.write( i + "\n")
    f.close()
#!/usr/bin/env python
from gdata_handler import find_channels
from json_config import config_read, config_write

def addchannel_ui(channel_name):
    try:
        results = find_channels(channel_name, 5)
    except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

    num_results = len(results)
    response = ""

    if num_results == 0:
        print "\nno results found for \"%s\"\n" % channel_name
        print "\nno new sources were added for tracking\n"
        return None

    elif num_results == 1:
        print "%s (%s)\nDescription: %s\n" % (results[0].title,
                results[0].id, results[0].description)
        while response.lower() != 'y' and response.lower != 'n':
            print "\nwould you like to add this source?",
            response = raw_input("[y]es or [n]o: ")
            if response.lower() == 'y':
                print "\nsource '%s' is now tracked\n" % results[0].title
                return results[0]
            elif response.lower() == 'n':
                print "\nno new sources were added for tracking\n"
                return None

    else: # greater than 1
        print "\nmultiple hits for \"%s\":\n" % channel_name
        for i in range(num_results):
            print "%d - %s (%s)\nDescription: %s\n" % (i+1,
                    results[i].title, results[i].id, results[i].description)

        response = None
        while response != 'n':
            print "\nwhich source would you like to add?",
            response = raw_input("[1-%s] or [n]one: " % str(num_results))

            try:
                num_selected = int(response)
            except ValueError:
                num_selected = -1

            if num_selected >= 1 and num_selected <= num_results +1:
                print "\nsource '%s' is now tracked\n" % \
                    results[int(response)-1].title
                return results[int(response)-1]
                
        return None
        print "\nno new sources were added for tracking\n"

def rmchannel_ui(config_dict, channel):
    try:
        channel_num = int(channel)
        if len(config_dict['channels']) < channel_num:
            print "\nno sources were removed from tracking\n"
            return None
        else:
            print "\nsource '%s' no longer tracked\n" % \
                sorted(config_dict['channels'])[channel_num] 
            return sorted(config_dict['channels'])[channel_num]
    except ValueError:
        if channel in config_dict['channels']:
            print "\nsource '%s' no longer tracked\n" % channel 
            return channel
        else:
            print "\nno sources were removed from tracking\n"
            return None

def lschannel_ui(config_dict):
    names = sorted(config_dict['channels'])
    print "\nCurrently tracked sources:"
    print "--------------------------"
    for i in range(len(names)):
        print '%3d - "%-s" (%s)' % (i, names[i],
            config_dict['channels'].get(names[i]))
    print "--------------------------\n"

if __name__ == "__main__":
    CONFIG = config_read("temp")
    print CONFIG
    ADD = addchannel_ui("Monstercat")
    if ADD != None:
        CONFIG['channels'][ADD.title] = ADD.id
    print CONFIG
    lschannel_ui(CONFIG)
    print rmchannel_ui(CONFIG, 22)
    print rmchannel_ui(CONFIG, "aaa")
    print rmchannel_ui(CONFIG, "Monstercat")
    if "Monstercat" in CONFIG['channels']:
        del CONFIG['channels']["Monstercat"]
    config_write(CONFIG, "temp")

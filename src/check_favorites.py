# Read recent videos and detect if they are a user's favorite
# Not really...working yet.  
def read_artists(songs):
    '''Sample function for how to read files with song information'''
    # Acquire title of recent downloads (artist and title)
    fp = open('URLs.txt', 'r') 
    all_songs = fp.readlines()
    fp.close()
    title = all_songs[0].partition(',')[2].rstrip() # not sure if this works
    # for each person with favorites, open (or just have 1 file with muliple dictionary entries)
    # Get favorite artists to search with
    f = open('favorites/erik.txt', 'r')
    lines = f.readlines()
    f.close()
    #favorites = []
    new_songs = []
    # for favorite in lines:
    #    if favorite.rstrip() in title:
    #        favorites.append(favorite)
    
    for song in all_songs:
        for favorite_artist in lines:
            song_title = song.partition(',')[2].rstrip()
            if favorite_artist.rstrip() in song_title:
                print "new song is %s" % song_title 
                new_songs.append(song_title)
            else:
                print "song not found"

    print "yep\n"
    print lines
    print "got heem\n"
    print all_songs


    # for item in lines, if item is inside list of artists, add title to list to send (append)
    # after it's done, send it to notify().  Do this for each person's favorites (could be passed
    # in)
    # notify_text(title, person, ...)
    # To split the entry, partition based on the ','
    # Note there are now 3 fields -- Channel, URL, title
    # To get rid of '\n', use .rstrip()
    # Do what you want after this ...

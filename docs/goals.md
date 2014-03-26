Splatfilch: Goals

# Abstract
__Splatfilch__ is an automated music sharing system that aims to be something between an internet radio station and a shared folder, but with enhanced functionality.  Music will be aggregated from various sources ([YouTube](www.youtube.com), [Soundcloud](www.soundcloud.com), torrents, etc) and shared with all users of the service.  The music selection will change over time as new tracks are released, and users will have the option of flagging tracks for retention so they remain available. 

# Requirements
- Aggregate music from all sources into a centralized location and tag appropriately
- Download audio from sources on a regular schedule 
- Provide users an interface to flag tracks for retention
- Retain tracks flagged for retention
- Remove tracks after either:
- size constraints are met on server
- tracks expire after given time if not flagged for retention

# Stretch Goals
- Implement ability for user to add their favorite artists
- Notify user when their favorite artists release music (email, text)

- Universal method to flag tracks for retention that works across common players/interfaces
- Intelligent download rules (avoid obvious duplicates)
- Stream files to user’s mobile devices/computers.
    - list of __Splatfilch__ approved apps.

    # Extras
    - Streaming solution that does not rely on specific application on user’s device.  (Subsonic or similar)

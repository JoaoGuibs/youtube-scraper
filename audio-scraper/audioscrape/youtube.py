# coding=utf-8
"""Rip audio from YouTube videos."""
import os
import re

import pafy
from time import sleep

try:
    from urllib.parse import urlencode
    from urllib.request import urlopen
except ImportError:
    from urllib import urlencode, urlopen

def scrape(query, include, exclude, quiet, overwrite, max_songs_down = 6):
    """Search YouTube and download audio from discovered videos."""

    # Search YouTube for videos.
    url = 'http://youtube.com/results?' + urlencode({'search_query': query})
    html = urlopen(url).read().decode('utf-8')
    video_ids = re.findall(r'watch\?v=(.{11})', html)

    print("The number of found videos is: ", len(video_ids))
    n_songs_down = 0
    # Go through all found videos.
    for video_id in video_ids:

        #Stop when number of songs is reached or when the number of the desired songs is in the folder
        if(n_songs_down >= max_songs_down and len(os.listdir(os.getcwd() + "/")) >= max_songs_down):
            break

        # Fetch metadata and available streams.
        # If id is not valid, don't download and move to the next one
        try:
            video = pafy.new(video_id)
        except Exception as e: 
            print(str(e) + "\n")
            print("File not downloaded")
            continue 

        # Collect video metadata.
        metadata = video.keywords + [
            video.title, video.author, video.description, video.category
        ]
        haystack = ' '.join(metadata).lower()

        # Don't download audio if video lacks a required term in its metadata.
        if include:
            if all(w not in haystack for w in include):
                continue

        # Don't download audio if video has a forbidden term in its metadata.
        if exclude:
            if any(w in haystack for w in exclude):
                continue

        # Always prefer highest quality audio.
        audio = video.getbestaudio()

        # Skip existing files.
        try:
            if os.path.isfile(audio.filename) and not overwrite:
                n_songs_down += 1
                continue
            
            sleep(1)
            # Download audio to working directory.
            audio.download(quiet=quiet)
            #Increase when song is downloaded correctly
            n_songs_down += 1

        except Exception as e:
            print(str(e) + "\n")
            continue 

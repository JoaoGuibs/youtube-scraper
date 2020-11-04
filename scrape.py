import sys
sys.path.append("./audio-scraper/")

import pandas as pd
import audioscrape
import os
import pafy 


def main():

    PATH = os.path.dirname(os.path.abspath(__file__))
    OUT_DIR = "/outputs/"
    max_songs = 8
    #Read the csv with the songs
    #Get the title and artist, to use in the search query
    titles = pd.read_csv("songs_to_scrape.csv").TITLE
    authors = pd.read_csv("songs_to_scrape.csv").ARTIST

    #The search string will be the title + artist + LIVE for live version rendition
    search_strings = [f"{title} {author} Live" for title, author in zip(titles, authors)]

    #This is sets the API KEY
    #The API key needs to be created in the google console website (https://console.developers.google.com)
    YOUTUBE_API_KEY = ""#"" 
    pafy.set_api_key(YOUTUBE_API_KEY) 
    
    #Query all the musics in the csv 
    for i, s in enumerate(search_strings):

        title_path = f"{PATH}/{OUT_DIR}/{titles[i]}"

        if os.path.isdir(title_path):
            if len(os.listdir(title_path)) >= max_songs:
                print("Already have enough performances of the song")
                continue
        else:
          #Creates dir if it does not exist
          os.makedirs(title_path)

        os.chdir(title_path)

        print(f"Downloading into {title_path}")
        audioscrape.download(query=s, include=False, exclude=False, quiet=False, max_songs_down = max_songs)
        break 

    return 0

if __name__ == "__main__":
    main()
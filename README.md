# Youtube scraper example:

This is a simple scripting example that uses the audio scraper code (https://github.com/carlthome/audio-scraper), to scrape songs given in a csv file.

The script runs a query with the song name and the artist, plus some extra keywords we may want to add and downloads a certain number of songs, corresponding to the search query, from youtube, in **.webm** format. 

## Requirements and Installation (Ubuntu):

 * Python and python-pip: ```sudo apt-get install python3 python3-pip```
 * Pipenv: ```pip3 install pipenv``` 

 In the main folder of the project run:
 * Install project dependencies with pipenv: ```pipenv sync```
 * Run the script: ```pipenv run python scrape.py```

 **Note:** A valid API key should be added inside the *scrape.py* script. The API key can be obtained in: https://console.developers.google.com/ - a google account must be associated, in order to get access.
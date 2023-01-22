# CheckHarmfulLinks

Simple application to check if a list of links can be resolved by the DNS server

## Description

With this code you can check if your server is able to resolve a list of links to see if your protection against dangerous links is up to date.

## How to use

1. Create a file named ```harmfulLinks.txt``` which contains all the links you want your system to check (Always **ONE** link per line)
2. Start the file ```main.py``` with Python on your computer (Make sure that your DNS settings are set correctly before running the file.)
3. Check the results of the check in the ```results_sorted.txt``` file once the program is finished.

## Results

The program tries to resolve all the links contained in the ```harmfulList.txt``` file.
If an error occurs during the resolution or the result of the resolution is 0.0.0.0 / :: the link is skipped and only a short feedback is written to the console.
All links that can be resolved are written to the ```results_sorted.txt``` file. There the links are sorted alphabetically and duplicates are removed if available. 

## Licensing

You can read everything about the license in the LICENSE file in this repository.

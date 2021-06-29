# PaperScraper

This is a quick python script to automatically download all PDFs from The University of Warwick's past paper site.

## Usage

You'll need to provide an SSO token from a cookie so the script can access the page. Sign into warwick.ac.uk/pastpapers, and make sure you set the sign in settings to remember you.

Next open devtools, and navigate to the storage tab. There you should be able to find your cookies for this site. You want with one with the key `WarwickSSO`. Copy the value of it, and assign it to the constant `COOKIE_TOKEN` in the script.

By default the url points to all DCS past papers for all years. You can change this by navigating to the page you want the papers from, and changing the `URL` parameter at the top of the script.

The papers are organised by year. If you want to make a PR to organise them by module or some other way feel free.

## Disclaimer

This script is provided for personal use only. Downloaded papers may not be shared with anyone, even other students. I am not responsible for anything you do with this script, nor anything you do with the files you download using it.

> These papers are provided for private study purposes only. You may print them, but must not distribute them, in any form, even to other students.

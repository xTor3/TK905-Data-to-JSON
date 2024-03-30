# TK905-Data-to-JSON
Do you have a TK905 GPS tracker and want to export the data in JSON format?
This simple script can help you to convert data to JSON and append new data when you want.

## How to use
1. login to your [mytkstar](tkstar.net) account, and next go to the "playback" section of the GPS tracker you want to export data.
2. choose the period of the data you are interested in
   * I don't know why but if you choose a period bigger than 9/10 days, mytkstar doesn't download all the data. No problem, download the data in several separate files and put them in a folder.
3. download this script by  `git clone https://github.com/xTor3/TK905-Data-to-JSON.git` or with the download button, and put inside the repository's folder the folder with raw data.
4. from the terminal, inside the repository's folder, send the command `python script.py <raw_folder_name> [old_json_name]` (bs4 library is required), where *raw_folder_name* is the folder with raw data and, optionally, *old_json* is a name of a JSON that contains data of a previous export, in case of you only want to append new raw data present in the folder.
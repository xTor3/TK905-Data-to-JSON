import json
from bs4 import BeautifulSoup
import os
import sys


def clean_data(soup):
   raw_val = soup.find_all("th")

   array = [raw_val[i:i+9] for i in range(9, len(raw_val), 9)] # The first nine elements are the heading
   for sub_array in array:
      del sub_array[0]
      del sub_array[-1]
      del sub_array[-1]

      for i in range(6):
         sub_array[i] = sub_array[i].text
         if i > 0 and i < 5:
            sub_array[i] = float(sub_array[i])
         if i == 5:
            sub_array[i] = int(sub_array[i][:-1])
      
      date_and_hour = sub_array[0].split()
      sub_array[0] = date_and_hour[0]
      sub_array.insert(1, date_and_hour[1])

   return array

def insert_in_dict(dictionary, array):
    for sub_array in array:
        if sub_array[0] not in dictionary:
            dictionary[sub_array[0]] = [sub_array[1:]]
        else:
            if sub_array[1:] not in dictionary[sub_array[0]]:
                dictionary[sub_array[0]].append(sub_array[1:])

def json_output(dictionary):
    f = open('clean.json', 'w')
    f.write(json.dumps(organized, indent=2))
    f.close()


if __name__ == "__main__":
   organized = {}
   raw_folder_name = ''

   if len(sys.argv) > 2:
      raw_folder_name = sys.argv[1]
      last_json = open(sys.argv[2])
      organized = json.load(last_json)
   elif len(sys.argv) > 1:
      raw_folder_name = sys.argv[1]
   else:
      print("Please insert the folder name with the raw files")
      exit()

   raw_folder_path = os.getcwd() + '/' + raw_folder_name
   files = os.listdir(raw_folder_path)

   for raw in files:
      if raw[0] != '.':
         print(f'Elaborating: {raw}')
         with open(os.getcwd() + '/' + raw_folder_name + '/' + raw, "r", encoding="utf-8") as file:
            html_content = file.read()
         soup = BeautifulSoup(html_content, "html.parser")
         clean = clean_data(soup)
         insert_in_dict(organized, clean)
   
   organized = dict(sorted(organized.items()))
   json_output(organized)
   
   print(f'{len(organized.keys())} days are registered:')
   registered_date = list(organized.keys())
   for i in range(0, len(registered_date), 7):
      print(registered_date[i:i+7])

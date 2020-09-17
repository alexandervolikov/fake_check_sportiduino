import json
import os
import os.path


def open_all_json_files(file_start_name):
    '''Collects all files_start_nameYYYYMMDDHHMMSS.json form /data into a list of dictionaries
    '''
    list_from_jsons = []

    for file_name in os.listdir(path = 'data'):
        if file_name[0:8] == file_start_name:
            json_file = open(f'data/{file_name}','r',encoding = 'utf-8')
            list_from_jsons.extend(json.load(json_file))
            json_file.close()

    return list_from_jsons

print('loading data')

#loading chip data
data = open_all_json_files('readData')

#load station data
dump = open_all_json_files('dumpData')

#create a more convenient dictionary for marks at stations
dumped_cp = {}
for dump_cp in dump:
    dumped_cp[dump_cp['cp']] = dump_cp['cards']

print('start checking data')

#go through all the chips from the data
for chip in data:
    #check all the marks in them
    for mark in chip['punches']:
        # if the kp number is in the dictionary with the read station numbers
        # check if the number is the corresponding chip number
        # write, if we caught a fake mark, we output the raw data of the chip and station
        if mark[0] in dumped_cp:
            if chip['card_number'] not in dumped_cp[mark[0]]:
                print(f'\nfake cp {mark[0]} in the chip {chip["card_number"]}')
                print(f'raw data of the chip {chip["card_number"]}')
                print(chip)
                print(f'raw data of the station {mark[0]}')
                print(dumped_cp[mark[0]])

print('\nFinish checking.\nFor exit press Enter')
a = input()
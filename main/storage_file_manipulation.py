import json
import csv
import io
import os
import fileinput
import filecmp
from hashlib import sha256


class storage_file_manipulation:
    jsonPath = "currentInventory.json"
    desfilePath = "desFile.json"
    deslockPath = "deslock.txt"

    def generate_files():
        #Important note for changes to the dictionary setup:
        #All parts are the name of a matrix that displays total amount of that part how many are in stock and how many are out of stock
        #That looks like "WxLxH": [Total, In, Out]
        currentinventory_dict = {
            "Aluminum_C_Channels_Whole_Length": {
                    "2x25x1": [20, 20, 0],
                    "2x20x1": [20, 20, 0],
                    "2x15x1": [20, 20, 0],
                    "2x10x1": [20, 20, 0],
                    "2x5x1": [20, 20, 0],
                    "2x25x2": [20, 20, 0],
                    "2x20x2": [20, 20, 0],
                    "2x15x2": [20, 20, 0],
                    "2x10x2": [20, 20, 0],
                    "2x5x2": [20, 20, 0],
                    "5x25x1": [20, 20, 0],
                    "5x20x1": [20, 20, 0],
                    "5x15x1": [20, 20, 0],
                    "5x10x1": [20, 20, 0],
                    "5x5x1": [20, 20, 0]
            },
            "Steel_C_Channels_Whole_Length": {
                    "2x25x1": [20, 20, 0],
                    "2x20x1": [20, 20, 0],
                    "2x15x1": [20, 20, 0],
                    "2x10x1": [20, 20, 0],
                    "2x5x1": [20, 20, 0],
                    "2x25x2": [20, 20, 0],
                    "2x20x2": [20, 20, 0],
                    "2x15x2": [20, 20, 0],
                    "2x10x2": [20, 20, 0],
                    "2x5x2": [20, 20, 0],
                    "5x25x1": [20, 20, 0],
                    "5x20x1": [20, 20, 0],
                    "5x15x1": [20, 20, 0],
                    "5x10x1": [20, 20, 0],
                    "5x5x1": [20, 20, 0]
            },
            "Aluminum_L_Channel": {
                    "2x25x2": [20, 20, 0],
                    "2x20x2": [20, 20, 0],
                    "2x15x2": [20, 20, 0],
                    "2x10x2": [20, 20, 0],
                    "2x5x2": [20, 20, 0]
            },
            "Cut_Aluminum_C_Channels": {
                    "2x25x1 or smaller": [40, 40, 0],
                    "2x25x2 or smaller": [40, 40, 0],
                    "5x25x1 or smaller": [40, 40, 0]
            },
            "Cut_Steel_C_Channels": {
                    "2x25x1 or smaller": [40, 40, 0],
                    "2x25x2 or smaller": [40, 40, 0],
                    "5x25x1 or smaller": [40, 40, 0]
            },
            "Omniwheels": {
                "4in": [40, 40, 0],
                "3.25in": [40, 40, 0],
                "2.75in": [40, 40, 0]

            },
            "Tractionwheels": {
                "4in": [40, 40, 0],
                "3.25in": [40, 40, 0],
                "2.75in": [40, 40, 0]
            },
            "Mechanumwheels": {
                "4in": [40, 40, 0],
                "2in": [40, 40, 0]
            }
        }

        desfile_dict ={
            
        }

        with open(deslockPath, 'x') as file:
            file.write("initialize")
        file.close()
        

    def writeJSONdesfile(id, subsequentData):
        #write with sha256 id and the relevant json array data
        new_dic = {id : {subsequentData}}
        with open(desfilePath,'w') as outfile:
            json.dump(new_dic, outfile)
        outfile.close()

    def translate_csv_to_json(csvFile):
        pwjsonArray = []
        with open(csvFile, encoding='utf-8') as csvf:
            #load csv file data
            csvIn = csv.DictReader(csvf)
        
        #convert to pydict
        for row in csvIn:
            pwjsonArray.append(row)

        #generate id for new object
        inDat = input(csvFile)
        outDat = sha256(inDat.encode('utf-8').hexdigest)

        #write to desFile with sha256 id
        writeJSONdesfile(outDat, pwjsonArray)
        with open(deslockPath, 'a') as outfile:
            outfile.write(outDat + ", " + csvFile)
        outfile.close()
    
    def read_index():
        print("a")

    def change_part_availibility():
        print("a")

import json
import csv
import subprocess
from hashlib import sha256


class storage_file_manipulation:

    jsonPath = "./assets/files/currentInventory.json"
    desfilePath = "./assets/files/desFile.json"
    deslockPath = "./assets/files/deslock.txt"
    
    def generate_files():
        deslockPath = storage_file_manipulation.deslockPath
        desfilePath = storage_file_manipulation.desfilePath
        jsonPath = storage_file_manipulation.jsonPath
        #Important note for changes to the dictionary setup:
        #All parts are the name of a matrix that displays total amount of that part how many are in stock and how many are out of stock
        #That looks like "WxLxH": [Total, In, Out]
        currentinventory_dict = {
            "Build_materials": {
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
                "Wheel_items": {
                    "Omni_wheels": {
                        "4in": [40, 40, 0],
                        "3.25in": [40, 40, 0],
                        "2.75in": [40, 40, 0]
                    },
                    "Traction_wheels": {
                        "4in": [40, 40, 0],
                        "3.25in": [40, 40, 0],
                        "2.75in": [40, 40, 0]
                    },
                    "Mechanum_wheels": {
                        "4in": [40, 40, 0],
                        "2in": [40, 40, 0]
                    }
                },
                "Pneumatic_items": {
                    "Pneumatic_cylinders": {
                        "75mm_cylinder": [0, 0, 0],
                        "50mm_cylinder": [0, 0, 0],
                        "25mm_cylinder": [0, 0, 0]
                    },
                    "Air_tank_200mL": [3, 0, 3],
                    "Pressure_regulation": {
                        "Air_Pressure_Gauge": [2, 0, 2],
                        "Air_Pressure_Regulator": [2, 0, 2],
                        "Air_Pressure_Regulator_Mounting_Bracket": [2, 0, 2]
                    },
                    "Tubing_Cutter": [1, 1, 0],
                    "Solenoids": [4, 4, 0],
                    "Fittings": {
                        "Shut_Off_Valve_Fitting": [3, 0, 30],
                        "Elbow_Fittings": [],
                        "Tee_Fittings": [],
                        "Air_Flow_Valve_Fittings": [],
                        "Straight_Male_Fittings": [],
                        "Straight_Female_Fittings": [],
                        "Valve_Stem": []
                    },
                    "Tubing&Plugs": {
                        "4mm_Plugs": [10, 0, 10],
                        "4mm_Tubing": [10, 0, 10]
                    }
                }
            }
        }  

        desfile_dict = {
            
        }


        with open(deslockPath, 'w+') as file:
            file.write("initialize")
        file.close()

        with open(desfilePath, 'w+') as file0:
            json.dump(desfile_dict, file0, indent = 2)
        file0.close()
        
        with open(jsonPath, 'w+') as file1:
            json.dump(currentinventory_dict, file1, indent = 2)
        file1.close()
        
    def writeJSONdesfile(id, subsequentData):
        desfilePath = storage_file_manipulation.desfilePath
        #write with sha256 id and the relevant json array data
        new_dic = {id : {subsequentData}}
        with open(desfilePath,'w') as outfile:
            json.dump(new_dic, outfile)
        outfile.close()

    def translate_csv_to_json(csvFile):
        deslockPath = storage_file_manipulation.deslockPath
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
        storage_file_manipulation.writeJSONdesfile(outDat, pwjsonArray)
        with open(deslockPath, 'a') as outfile:
            outfile.write(outDat + ", " + csvFile)
        outfile.close()
    
    def read_indice(knownIndice):
        jsonPath = storage_file_manipulation.jsonPath
        file = open(jsonPath, 'r')
        fileData = json.loads(file.read())
        for i in fileData[knownIndice]:
            print(i)
        file.close()


    def change_part_availibility():
        print("a")

    def find_in_directory(fileName):
        subprocess.run(["find", fileName])

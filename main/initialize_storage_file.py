import json
import io
import os
import fileinput
import filecmp


class initialize_storage_file:
    def generate_json_file():
        #Important note for changes to the dictionary setup:
        #All parts are the name of a matrix that displays total amount of that part how many are in stock and how many are out of stock
        #That looks like "WxLxH": [Total, In, Out]
        dict = {
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
                    "5x5x1": [20, 20, 0],
                }
        }
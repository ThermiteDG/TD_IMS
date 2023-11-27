# TD_IMS
 Python program to keep inventory of Vex parts for robots, but it can be modified for anything.
## Dependency Script
 Script to verify the install of integral packages using apt & pip as this program is designed to run on a Ubuntu enabled SBC.
## How are things measured in the JSON file?
Good question. Every 5 holes on a piece of material gives a rough equivalence of 5 holes to 2.5 inches. Based on this measurement we can classify individual pieces based on the amount of holes with a conversion factor for inches. This also works in reverse since the system is not counting the holes but rather finding the length and width of a piece. This is how the basic classification works.


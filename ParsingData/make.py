import csv
import json
lines = csv.reader(open("lifeExpectancy.csv", "rU"))
fifties = []  
eighties = []  
twenty05 = []  
for lat, lon, fifty, eighty, five in lines: #creating json of values of all countries and years
    fifties = fifties + [lat, lon, fifty]
    eighties = eighties + [lat, lon, eighty]
    twenty05 = twenty05 + [lat, lon, five]
output = [
    ["Life 1950", fifties],
    ["Life 1980", eighties],
    ["Life 2005", twenty05]
]
print json.dumps(output)

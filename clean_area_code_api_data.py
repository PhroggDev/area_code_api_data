"""This script removes the unchanging key 'US' from downloaded area code number data"""
import json

DATAFILE = "area_codes.json"

with open(DATAFILE, encoding="utf-8") as file:
    data = json.load(file)

# keys for this data
# `area-code`
# `city`
# `state`
# `country`
# `latitude`
# `longitude`
# 'country' is 'US' for all entries so let's dispose
# of that key
# The others will eventually be migrated to a db

keep_keys = ["area-code", "city", "state", "latitude", "longitude"]

for d in data:
    del d["country"]

NEWJSONFILE = "US_area_codes.json"
with open(NEWJSONFILE, "w", encoding="utf-8") as newfile:
    json.dump(data, newfile)

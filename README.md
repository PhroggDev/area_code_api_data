# Retrieve Data from API about US NPA areas aka: Area Codes

This was a simple project I undertook while learning about processing  
JSON (JavaScript Object Notation) data using Python(ver 3)  
To any seasoned Python script writers this code could use a lot of  
work and some organization. However, it suited me fine at the time  
of creation as my goal was simply to get a handle on retrieving and  
manipulating JSON data with the Python Standard Library.  
I used a cost-free api at [DEDOLIST](https://dedolist.com/) where a  
number of data sources are available without Authorization. Also  
available are API end-points for Postal Codes, a few word lists, the  
Periodic Table of Elements as well as Airport information, Country  
Region Codes and UTC Timezones.

These scripts leverage the Python module `requests` to retrieve the  
data in JSON format. Then use the standard library `json` module to  
read the data, remove non-changing key (all the data is for US cities and states)  
then write it back out sans the ["country"] key to file for later  
processing and probable migration to an SQLite3 db.

---

[get_ac_json.py][get] fetches the JSON data for US Area Codes  
[clean_area_code_api_data.py][clean] removes the 'country' key, which is unchanging  
for all the entries. Then writes the data back out to `US_area_codes.json`

---

It's released under a Public Domain license. Feel free to incorporate any  
part of it in your own project(s) w/o attribution. Not that there's anything  
special here :stuck_out_tongue_winking_eye:

## ToDo:
+ add some header checking after Response is returned once I figure out how this api does rate-limiting


[clean]: clean_area_code_api_data.py
[get]: get_ac_json.py

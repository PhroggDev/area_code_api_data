# coding: utf-8
"""Save Area Code data for Cities in USA to a file"""
import json
from requests import get

SAVEFILE = "area_codes.json"

URL = "https://api.dedolist.com/api/v1/business/area-codes-usa/"

resp = get(URL, timeout=3)
if resp.status_code == 200:
    print("So good so far...")
    print(f"Server returned http status {resp.status_code}")
    json_content = resp.json()
    print("Saved retrieved data to a variable...")

with open(SAVEFILE, "w", encoding="utf-8") as file:
    json.dump(json_content, file)
    print(f"Saved JSON Data to {SAVEFILE}")

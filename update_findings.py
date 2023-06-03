from get_csv import download_csv
from parse_csv import read_csv
from update_sheets import write_sheet
from config import read_config
import time
import os

print("Read config")
config = read_config()
today = time.strftime("%Y-%m-%d")

print("Download CSV")
download_csv(url=config["wp-admin-url"], form_id=config["form-id"], login=config["login"], password=config["password"])

print("Parse CSV")
findings = read_csv(f'cfdb7-{today}.csv')

print("Delete CSV")
os.remove(f'cfdb7-{today}.csv')

print("Write Sheet")
write_sheet(config["spreadsheet-id"], config["template-worksheet-id"], findings, today)

print("Done")
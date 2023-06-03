# update-findings
This script makes the following assumptions:
- You have a Wordpress webpage
- You use Contact Form 7
- You use Contact Form 7 Database Addon
- You use the exact data structure as my use-case - this is obviously untrue so feel free to modify the relevant code and use this repo as a guideline. I am not going to parametrise or open this script for custom parsers. Treat this as a demo.

This script does the following:
- Logs in as a Wordpress user in a headless browser using Selenium
- Exports a CSV for a given form
- Parses the data to retrieve only the relevant data
- Creates a new worksheet (named after the current date) out of a template in a Google Sheets spreadsheet and fills it with the form responses.

## Prerequisites
### pyyaml
PyYAML is used for config parsing

https://pyyaml.org/

To install run `pip install pyyaml`

### selenium
Selenium is used to log into Wordpress and download the CSV

https://www.selenium.dev/

To install run `pip install selenium`

### chrome webdriver
Chromium webdriver is used to ensure Selenium can run headless on a VPS for automation purposes

https://chromedriver.chromium.org/

To install follow Keegan Leary's guide here

https://www.keeganleary.com/setting-up-chrome-and-selenium-with-python-on-a-virtual-private-server-digital-ocean/

### gspread
gspread is used to interact with Google Sheets

https://github.com/burnash/gspread

To install run `pip install gspread`

Follow the following link to set up a service account for gspread to use. Use the default `~/.config/gspread/service_account.json` location for the credentials .json

https://docs.gspread.org/en/latest/oauth2.html

## Wordpress setup
You need credentials for a user with a role that has `cfdb7_access` granted. We recommend creating a service user with only this role access.

## Google Sheets setup
Create a spreadsheet with a template worksheet containing the header, custom formatting, filters, slicers, etc. This worksheet will be copied and the copy will be filled with data

## Config
Before use make sure to put all required information in `config.yml`. The template is provided in the repository
```
wp-admin-url: "https://example.com/wp-admin"
form-id: "0"
login: "user"
password: "password"
spreadsheet-id: "1A4212"
template-worksheet-id: 12345
```
| Argument               | Description                                                                   |
|------------------------|-------------------------------------------------------------------------------|
| wp-admin-url:          | The URL you use to log into the Wordpress admin panel                         |
| form-id:               | Form id for the form you want to export as CSV                                |
| login:                 | username for the Wordpress user used to access the CSV                        |
| password:              | password for the Wordpress user used to access the CSV                        |
| spreadsheet-id:        | Spreadsheet id found in the url of the target Google Sheets file              |
| template-worksheet-id: | Worksheet id (gid) of the worksheet used as a template for the new worksheets |

## Run the script
To run the script execute `python3 update_findings.py` after filling in the config and fulfilling all the prerequisites.

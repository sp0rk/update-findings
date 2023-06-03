import csv
from finding import Finding

def read_csv(filename):
    def read_location(row):
        gps = row["Where Gps"]
        has_gps = gps != ""
        picker = f'{row["Cf7 Location Lat"]},{row["Cf7 Location Lng"]}'
        return gps if has_gps else picker

    def read_photos(row):
        return row["Photos"].split(",")

    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        findings = []
        for row in csv_reader:
            location = read_location(row)
            photos = read_photos(row)
            finding = Finding(date=row["Date"], username=row["Username"], email=row["Email"], species=row["Species"], tree=row["Tree Species"], height=row["Height"], direction=row["Direction"], info=row["Info"], location=location, photos=photos)

            findings.append(finding)

        return findings
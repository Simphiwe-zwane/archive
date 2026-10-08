"""Reading and writing the Archive file.

YOU IMPLEMENT THIS FILE.

The file format is CSV with no header row. One record per line, five fields
separated by commas, in this order:

    id,title,city,year,condition
    MS001,Tarikh al-Sudan,Timbuktu,1655,fragile

Remember Session 1: a file is one long line of characters. The comma
separates fields; the newline separates records. Nothing else is doing
any work.
"""

import csv
from archive.errors import MalformedRecordError
from archive.validation import validate_record

FIELD_NAMES = ["id", "title", "city", "year", "condition"]


def parse_line(line):
    
    WordList = line.split(',')

    return {
        "Id" : WordList[0],
        "Title" : WordList[1],
        "City" : WordList[2],
        "Year" : WordList[3],
        "Condition" : WordList[4]
    }



def load_archive(path):
    validRecords = []
    invalidRecords = []
    with open(path, "r") as f:
        data = csv.reader(f)
        for row in data:
            record = parse_line(row.replace("(", ""))
            record = parse_line(row.replace(")", ""))
            record = parse_line(row.replace("[", ""))
            record = parse_line(row.replace("]", ""))
            
            if validate_record(row) == ():
                validRecords.append()
            else :
                invalidRecords.append(row)
    return (validRecords, invalidRecords)



def save_archive(path, records):
    
    with open(path, "a") as f:
        writer = csv.writer(f)

    for record in records:
        writer.writerow(record.values())


    

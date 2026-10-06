"""Questions we ask the Archive.

YOU IMPLEMENT THIS FILE.

Every function here takes `records` — a list of record dicts as produced by
load_archive — and answers one question about the collection. None of them
touch a file. None of them print anything. They return values.

Keep in mind from Week 2: the structure you are given decides which of these
is cheap and which is expensive. All of these are linear scans over a list.
Note in your README which one would be instant with a dictionary instead.
"""


def count_before(records, year):
    count = 0
    for record in records:
        if int(record["year"]) < year:
            count += 1
    return count



def find_by_city(records, city):
    matches = []
    target_city = city.lower()
    for record in records:
        if record["city"].lower() == target_city:
            matches.append(record)
    return matches



def oldest(records):
    if not records:
        return None

    oldest_record = records[0]
    
    for record in records:
        if int(record["year"]) < int(oldest_record["year"]):
            oldest_record = record
            
    return oldest_record


def cities_summary(records):
    summary = {}
    for record in records:
        city = record["city"]
        if city in summary:
            summary[city] += 1
        else:
            summary[city] = 1
    return summary

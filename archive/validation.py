"""Validation rules for manuscript records.

YOU IMPLEMENT THIS FILE.

Every validate_* function takes a raw string (exactly as it came out of the
CSV file) and returns a tuple:

    (True, "")              the value is trustworthy
    (False, "reason here")  the value is not, and here is why

The reason is a short human-readable string. The autograder checks the
boolean, not your exact wording — but a teammate reading your rejection log
should understand it, so write it for them.

READ THIS BEFORE YOU START
--------------------------
The year range is INCLUSIVE at both ends: 1100 and 1900 are VALID.
1099 and 1901 are not. Most marks lost in Part A are lost on that line.
"""

from archive.errors import MalformedRecordError  # noqa: F401  (you may not need it here)

KNOWN_CITIES = ["Timbuktu", "Djenne", "Gao", "Walata", "Chinguetti"]

VALID_CONDITIONS = ["fragile", "fair", "good"]

MIN_YEAR = 1100
MAX_YEAR = 1900


def validate_id(value):
    if (len(value) == 5 and 
        value.startswith("MS") and 
        value[2:].isdigit() and 
        value[2:] != "000"):
        return True, "Valid Input"
    else:
        return False, ("Invalid Input. Pls put valid input.  "
                       "Valid: MS001, MS742 "
                       "Invalid: MS1, MS0012, ms001, XX001, MS000, MS00A")





def validate_title(value):
    if len(value.strip()) >= 3:
        return True, "Valid Input"
    else:
        return False, ("Invalid Input. Pls put valid input.  "
                       "Valid: Tarikh al-Sudan "
                       "Invalid: '', '   ', 'Ab'")



def validate_city(value):
    if value.strip().lower() in (city.lower() for city in KNOWN_CITIES):
        return True, "Valid Input"
    else:
        return False, ("Invalid Input. Pls put valid input.  "
                       "Valid: Timbuktu, Djenne, Gao, Walata, Chinguetti "
                       "Invalid: Kano, '   ', 'New York'")



def validate_year(value):
    If value.isdigit():
        year = int(value)
        if MIN_YEAR <= year <= MAX_YEAR:
            return True, "Valid Input"
        else:
            return False, ("Invalid Input. Pls put valid input.  "
                           "Valid: 1655, 1100, 1900 "
                           "Invalid: '', '   ', 'c.1590', 'sixteen fifty', '1099', '1901', '2087'")
    else:
        return False, ("Invalid Input. Pls put valid input.  "
                       "Valid: 1655, 1100, 1900 "
                       "Invalid: '', '   ', 'c.1590', 'sixteen fifty', '1099', '1901', '2087'")
   
def validate_condition(value):
    """A condition must be one of VALID_CONDITIONS, case-insensitively.

    Valid:   "fragile", "GOOD", "Fair"
    Invalid: "excellent", "", "ok"

    Returns (bool, str).
    """
    raise NotImplementedError("validate_condition")


def validate_record(record):
    """Validate a whole record dictionary.

    record is a dict with the keys: id, title, city, year, condition.

    Returns a LIST of reasons the record is invalid — one string per broken
    rule, in this field order: id, title, city, year, condition.
    An empty list means the record is valid.

    Do not re-write the rules here. Call the five functions above.
    """
    raise NotImplementedError("validate_record")

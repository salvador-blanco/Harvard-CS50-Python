import re
import sys

def main():
    hours_12h_format = input("Hours: ")
    hours_24h_format = convert(hours_12h_format)

    print(hours_24h_format)
    #9:00 AM to 5:00 PM"

def convert(s):
    is_valid_format = re.search(r"^([0-9]?[0-9]):?([0-5]?[0-9]?)? (AM|PM) to ([0-9]?[0-9]):?([0-5]?[0-9]?)? (PM|AM)", s)

    if bool(is_valid_format) == False:
        raise ValueError

    strt_am_or_pm = is_valid_format[3]
    end_am_or_pm = is_valid_format[6]

    strt_hrs = int(is_valid_format[1])
    end_hrs = int(is_valid_format[4])

    if is_valid_format[2]: #change to walrus operator
        strt_min = int(is_valid_format[2])
    else:
        strt_min = 0

    if is_valid_format[5]: #change to walrus operator
        end_min  = int(is_valid_format[5])
    else:
        end_min = 0

    if strt_hrs == 12 and strt_am_or_pm == "AM":
        strt_hrs -= 12
    if end_hrs == 12 and end_am_or_pm == "AM":
        end_hrs -= 12

    if strt_am_or_pm == "PM" and strt_hrs != 12:
        strt_hrs +=12
    if end_am_or_pm == "PM" and end_hrs !=12:
        end_hrs += 12

    return f"{strt_hrs:02d}:{strt_min:02d} to {end_hrs:02d}:{end_min:02d}"

if __name__ == "__main__":
    main()

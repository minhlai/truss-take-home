import csv
import argparse
from datetime import datetime, timedelta
import math

# argument parser for input and output files
parser = argparse.ArgumentParser()
parser.add_argument('infile', help='Input file to normalize')
parser.add_argument('outfile', help='Output file to write to')
args = parser.parse_args()

# parse string for time units and use int() and float() to round up seconds
def format_duration( str ):
    string_split = str.split(':')
    duration = 0
    duration += int(string_split[0]) * 60 * 60
    duration += int(string_split[1]) * 60
    duration += float(string_split[2])
    return duration

with open(args.infile, newline='', encoding='latin-1') as file_read:
    with open(args.outfile, 'w') as file_write:
        reader = csv.reader(file_read, delimiter=',', quotechar='"')

        # treat header specially. it does not have fields that need to be normalized
        header = next(reader)
        decoded_header = ", ".join(header)
        file_write.write(decoded_header + '\n')

        # start normalizing after header
        for row_idx, row in enumerate(reader):
            try:
                decoded_row = []
                # decode each column in row so we can get better debugging info
                for col_idx, col in enumerate(row):
                    decoded_row.append(bytes(col, 'latin-1').decode('utf-8', errors="strict"))

                # normalize timestamp
                try:
                    timestamp = decoded_row[0]
                    datetime_object = datetime.strptime(timestamp,"%m/%d/%y %I:%M:%S %p")
                    time_et = datetime_object + timedelta(hours=3)
                    decoded_row[0] = str(time_et)
                except ValueError as e:
                    print("Value Error on Row {0}. Invalid value in Timestamp.".format(row_idx))
                    continue

                # normalize address
                address = decoded_row[1]
                decoded_row[1] = '"' + address + '"'

                # normalize zipcode
                try:
                    zip = decoded_row[2]
                    int(zip)
                    decoded_row[2] = zip.zfill(5)
                except ValueError as e:
                    print("Value Error on Row {0}. Invalid value in Zipcode.".format(row_idx))
                    continue

                # normalize full name
                fullname = decoded_row[3]
                decoded_row[3] = fullname.upper()

                # normalize foo, bar, and total duration
                try:
                    foo_duration = decoded_row[4]
                    bar_duration = decoded_row[5]
                    foo_in_seconds = format_duration(foo_duration)
                    bar_in_seconds = format_duration(bar_duration)
                    decoded_row[4] = str(foo_in_seconds)
                    decoded_row[5] = str(bar_in_seconds)
                    decoded_row[6] = str(foo_in_seconds + bar_in_seconds)
                except ValueError as e:
                    print("Value Error on Row {0}. Invalid value in one of FooDuration or BarDuration.".format(row_idx))
                    continue

                # normalize notes
                notes = decoded_row[7]
                normalize_row = ', '.join(decoded_row)

                # write normalized row to outfile
                file_write.write(normalize_row + '\n')

            except UnicodeDecodeError as e:
                print("Unicode Decoding Error on Row {0}. Invalid unicode in {1}.".format(row_idx + 2, header[col_idx]))
            except IndexError as e:
                print("Something wrong with CSV file. Check that it is in valid CSV format.")
                break


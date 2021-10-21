# truss-take-home

## How to run
`python3 normalizer.py input_file output_file`

Apologies but I misread the note about reading from stdin, writing to stdout, and printing to stderr. I parse the input and output files as arguments, and print error messages to console. If I had more time after realizing this, I would have corrected it.

## Assumptions

1. Other than Notes, all other columns are non-empty
2. Column Headers are kept in consistent order and do not need to be normalized or have non-unicode characters.
3. Zip code not longer than 5 digits
4. Other unicode commas are not used
5. It's ok to put double quotes around all addresses
6. There are no tricky double quotes. Like odd number of quotes.

## **Cut for time/Should've dones:**

1. The aforementioned stdin, stdout, and stderr functionality
2. TotalDuration should have float precision set to higher of Foo and Bar duration
3. Validate argument parser input for filenames.
4. Test output CSVs in Excel

## Notes

1. Misread prompt. Got too focused on CSV Reader library and normalizing and did not focus on stdin function enough. Too late to pivot when I realized
2. Read file with latin-1 encoding because it uses single byte characters which means even non-unicode byte sequences would become one or multiple latin-1 characters
3. Convert latin-1 back to bytes and then decode to UTF-8. I do this because I did not want to get unicode errors while reading the file, or the row. I wanted a Cell specific unicode error
4. If headers are not consistent, I would use a dictionary and map the header title to a column index
5. If Zip Codes are longer than 5 digits, I would probably throw an error
6. If other unicode commas are used, my solution would not work because latin-1 and utf-8 have the same byte encoding for the standard comma but not other commas.
7. If columns other than notes can be emptym I would check for that and either error or continue
8. 1, 2, 3, and 4 byte unicode characters do not reuse x2C, the byte encoding for the standard comma
9. Adding a space after the commas breaks the CSV when there are commas inside double quotes
10. If I cannot insert double quotes, I would check for commas inside the string and insert double quotes if necessary
11. If there are odd number of quotes, I would have to err.

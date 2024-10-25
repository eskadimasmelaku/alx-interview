#!/usr/bin/python3
import sys

# Initialize counters and data structures
total_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
count = 0

def print_stats():
    """Print the current statistics of total file size and count of status codes."""
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

try:
    # Process each line from standard input
    for line in sys.stdin:
        parts = line.split()
        # Validate line format and update metrics if valid
        if len(parts) >= 7:
            file_size = parts[-1]
            status_code = parts[-2]
            if file_size.isdigit():
                total_size += int(file_size)
            if status_code in status_codes:
                status_codes[status_code] += 1
        count += 1
        # Print statistics after every 10 lines
        if count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # On keyboard interruption, print the statistics before exiting
    print_stats()
    raise
finally:
    # Always print statistics at the end
    print_stats()


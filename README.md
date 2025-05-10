# Most Active Cookie

This project is a Python-based program to process a cookie log file and return the most active cookies for a given date. It provides a command-line interface (CLI) to execute the program and includes unit tests for verifying correctness.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

## Overview

The "Most Active Cookie" program processes a log file in CSV format containing cookies and timestamps, and it identifies the most active cookies for a given date.

### Sample Input:

*cookie_log.csv*
```csv
cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00
```

### Features

- Process Cookie Log File: Parses a CSV file containing cookie identifiers and timestamps.

- Identify Most Active Cookie(s): For a given date, find the most frequently occurring cookie(s).

- Handles Multiple Cookies with Same Activity: If multiple cookies have the same frequency, all are returned.

- CLI Interface: A command-line interface to input the log file and target date.

- Unit Tests: Ensure correctness and accuracy of the functionality.


### Assumptions
- The input file contains cookie logs with the format: cookie,timestamp.

- The -d parameter for the date is given in UTC timezone format (e.g., 2018-12-09).

- The cookies in the log are sorted by timestamp (most recent first).

- The system has enough memory to process the entire log file.

### Requirements

Python: Version 3.6 or above

#### Libraries:

- argparse (for command-line argument parsing)

- unittest (for unit testing)

- pytest (optional for testing)

To install the required libraries, use:

```bash
pip install -r requirements.txt
```


## Usage
Running the Program
To find the most active cookies for a given date, run the following command:

```bash
python most_active_cookie/cli.py -f cookie_log.csv -d 2018-12-09
```

Expected Output:
```bash
AtY0laUfhglK3lC7
```
### Description:
-f: The log file (CSV format) containing cookies and timestamps.

-d: The target date for which the most active cookie(s) should be identified (in YYYY-MM-DD format).

## Unit Test Cases

The unit tests verify the following:

- Correct Cookie Identification: The most active cookie (AtY0laUfhglK3lC7) is correctly returned for the date 2018-12-09.
- Invalid Timestamp Handling: Rows with malformed timestamps are skipped and logged without affecting the result.
- No Matches Case: An empty result is returned when there are no cookies matching the given date.


You can also run individual tests with unittest:
```bash
python -m unittest discover tests
```

## Testing
You can run the tests with pytest to ensure everything is working correctly.

```bash
pytest
```

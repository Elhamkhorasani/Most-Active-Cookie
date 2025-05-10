import argparse
from cookie_counter import get_most_active_cookies

def parse_arguments():
    """
    Parse command line arguments for filename and date.
    """
    parser = argparse.ArgumentParser(description="Find the most active cookie(s) for a given day.")
    parser.add_argument("-f", "--filename", required=True, help="The cookie log file")
    parser.add_argument("-d", "--date", required=True, help="The date in UTC format (YYYY-MM-DD)")

    return parser.parse_args()

def main():
    # parse arguments
    args = parse_arguments()

    # call the core function to get most active cookies
    most_active_cookies = get_most_active_cookies(args.filename, args.date)

    # print results
    for cookie in most_active_cookies:
        print(cookie)

if __name__ == "__main__":
    main()

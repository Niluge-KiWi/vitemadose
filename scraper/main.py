import argparse
import sys
from scraper.scraper import scrape, scrape_debug


def main():  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", "-p", help="scrape platform. (eg: doctolib,keldoc or all)")
    parser.add_argument("--url", "-u", help="scrape one url")
    args = parser.parse_args()

    if args.url:
        scrape_debug(args.url)
        return
    platforms = []
    if args.platform and args.platform != 'all':
        platforms = args.platform.split(',')
    scrape(platforms=platforms)

if __name__ == "__main__":  # pragma: no cover
    main()

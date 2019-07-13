import requests, argparse, sys

parser = argparse.ArgumentParser(description="Python script to find a website status")
parser.add_argument('-u', '--url', help='Website URL', type=str, required=True)
args = parser.parse_args()

def url_check(url):
    try:
            site_ping = requests.head(url)
            if site_ping.status_code < 400:
                print("INFO: %s is OK" % (url))
                print("INFO: %s return http status code %s" % (url, site_ping.status_code))
                return True
            else:
                print("ERROR: %s return http status code %s" % (url, site_ping.status_code))
                return False
    except Exception as e:
        print("ERROR: %s return error %s" % (url, e))
        return False

output = url_check(args.url)
if not output:
    sys.exit(1)

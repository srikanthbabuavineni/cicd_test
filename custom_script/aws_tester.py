import boto3, argparse, sys

parser = argparse.ArgumentParser(description="Python script to find a AWS Keys")
parser.add_argument('-p', '--profile', help='Profile', type=str, default='default')
args = parser.parse_args()

def aws_check(profile):
    try:
            available_profiles = boto3.session.Session().available_profiles
            session = boto3.Session(profile_name=profile)
            client = session.client('s3')
            client.list_buckets()
            print("INFO: AWS profile is OK")
            print("INFO: Able to list S3 buckets using profile %s" % (profile))
            return True
    except Exception as e:
        print("ERROR: Uable to make AWS API call using %s profile\nERROR: AWS API call failed due to error %s" % (profile, e))
        print("WARNING: You might want to try different aws profile, available profiles are -")
        for i in available_profiles:
            print("\t- %s" % (i))
        return False

output = aws_check(args.profile)
if not output:
    sys.exit(1)

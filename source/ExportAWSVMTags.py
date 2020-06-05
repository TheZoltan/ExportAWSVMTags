import sys
import json
import boto3
Version = '1.0'

# Start here
def main():
    print('AWS to Azure Tag Copy Util   v', Version)

    # Re-create empty file if one already exists:
    json_awsvmtagsfile = open('getawstags.json', 'w+')
    json_awsvmtagsfile.close()


    # Get the tags from AWS
    getAWSTags()



def getAWSTags():
    ec2 = boto3.resource('ec2')

    print('Retrieving AWS Tags...')

    # Open file
    json_awsvmtagsfile = open('getawstags.json', 'a+')

    for instance in ec2.instances.all():
        print(instance.tags)

        json.dump(instance.tags, json_awsvmtagsfile)
        json_awsvmtagsfile.write('\n')

    # Close file
    json_awsvmtagsfile.close()



# Call main
if __name__ == '__main__':
    main()



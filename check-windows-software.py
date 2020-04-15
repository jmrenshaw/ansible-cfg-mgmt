import csv
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csvFile", help="Filename of input CSV file")
    parser.add_argument("softwareName", help="Name of software application to check")
    parser.add_argument("softwareVersion", help="Version of software application to check")
    args = parser.parse_args()

    with open(args.csvFile, 'rb') as f:
        input_csv = csv.DictReader(f)
        for row in input_csv:
            if args.softwareName==row['DisplayName'] and args.softwareVersion==row['DisplayVersion']:
                sys.exit(0)
    
    sys.exit(1)


'''
    if args.os == "linux":

        with open(args.csvFile, 'wb') as csvfile:
            fieldnames = ['package', 'version']
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvwriter.writeheader()
            for package in input_json:
                #print(package + " " + input_json[package][0]['version'])
                csvwriter.writerow({'package': package, 'version':input_json[package][0]['version']})

    elif args.os == "windows":

        with open(args.csvFile, 'wb') as csvfile:
            fieldnames = ['application', 'version']
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvwriter.writeheader()
            for application in input_json:
                csvwriter.writerow({'application': application, 'version':input_json[application]['version']
'''

    #print("JSON File = " + args.jsonFile)
    #print("CSV File = " + args.csvFile)

main()

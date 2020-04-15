import json
import csv
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("jsonFile", help="Filename of input JSON file")
    parser.add_argument("csvFile", help="Filename of output CSV file")
    parser.add_argument("os", help="Operating system - windows or linux")
    args = parser.parse_args()

    with open(args.jsonFile, 'r') as f:
        input_json = json.load(f)

    if args.os == "linux":

        with open(args.csvFile, 'wb') as csvfile:
            fieldnames = ['package', 'version']
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvwriter.writeheader()
            for package in input_json:
                #print(package + " " + input_json[package][0]['version'])
                csvwriter.writerow({'package': package, 'version':input_json[package][0]['version']})

main()

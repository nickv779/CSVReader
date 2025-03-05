import csv
import json
import argparse

# Col A = Algorithm Name, Col B = Whole Psuedocode Algorithm, Col C = Line-by-Line Psuedocode
# Col D = Code Mapped to Col C, Col E = Whole Code Algorithm

# WholeLinePsuedo.json = B to C
# LineByLine.json = C to D
# LineWholeCode.json = D to E
# WholeAlg.json = B to E

# json object
# {
#    "input": "input string",
#    "output": "output string",
# }

def csv_to_json(csv_path, json_path):
    with open(csv_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    
    with open(json_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    parser = argparse.ArgumentParser(description='Convert CSV to JSON.')
    parser.add_argument('csv_file', help='Path to the CSV file.')
    parser.add_argument('json_file', help='Path to the JSON file')

    args = parser.parse_args()

    csv_to_json(args.csv_file, args.json_file)

if __name__ == "__main__":
    main()

import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(csvFile) -> list[dict]:
    Array = []
    with open(csvFile) as f:
        i = 0
        for row in f:
            if i == 0:
                i += 1
                First_line = row
            else:
                line_list = First_line.replace('\n', '').split(',')
                row_list = row.replace('\n', '').split(',')
                item = dict(zip(line_list, row_list))
                Array.append(item)
    return Array

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

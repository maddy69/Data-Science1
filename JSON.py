import csv
import json
from collections import OrderedDict

fieldnames = ("first_name","last_name","company_name", "address", "city", "county", "state", "zip", "mobile_number",
              "email", "web")

entries = []
#the with statement is better since it handles closing your file properly after usage.
with open('customer_data_merged.csv', 'r') as csvfile:
    #python's standard dict is not guaranteeing any order,
    #but if you write into an OrderedDict, order of write operations will be kept in output.
    reader = csv.DictReader(csvfile, fieldnames)
    for row in reader:
        entry = OrderedDict()
        for field in fieldnames:
            entry[field] = row[field]
        entries.append(entry)

output = {
    "customers_data": entries
}

with open('customer_data_merged.json', 'w') as jsonfile:
    json.dump(output, jsonfile)
    jsonfile.write('\n')

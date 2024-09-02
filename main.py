import os 
import csv
import time
import json
from wiz_sdk import WizAPIClient
# Initialize a Wiz API Client.
wiz = WizAPIClient()

# Specify the query and variable file in environment variables
query_file = os.environ.get("WIZ_QUERY_FILE",'ccr.graphql')
variables_file = os.environ.get("WIZ_VARIABLES_FILE",'ccr-variables.json')

QUERY = open(query_file, "r").read()
print('{} loaded'.format(query_file))

VARIABLES = json.load(open(variables_file))
print('{} loaded'.format(variables_file))

# Execute the query.
results = wiz.query_all_pages(QUERY, VARIABLES)

# At this point fetching is done and all query results are stored in "results" variable
table_name = list(results.data.keys())[0]
print('Done fetching {}. Total records fetched: {}'.format(table_name, len(results)))

# Saving results in a csv format
print('Saving results to a file named "{}.csv" in the current directoy'.format(table_name))
field_names = results.data[table_name]['nodes'][0].keys()

with open('{}.csv'.format(table_name), 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    for node in results:
        writer.writerow(node)

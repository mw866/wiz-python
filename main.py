import os 
import csv
import argparse
import json

from wiz_sdk import WizAPIClient
# Initialize a Wiz API Client.
wiz = WizAPIClient()

# Set up argument parser
parser = argparse.ArgumentParser(description="Fetch data from Wiz API and save to CSV.")
parser.add_argument('--query', required=True, help='Path to the GraphQL query file.')
parser.add_argument('--variables', required=True, help='Path to the JSON variables file for the query.')
args = parser.parse_args()

with open(args.query, "r") as f:
    QUERY = f.read()
print('{} loaded'.format(args.query))

with open(args.variables, "r") as f:
    VARIABLES = json.load(f)
print('{} loaded'.format(args.variables))

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

import json
from haralyzer import HarParser, HarPage
from datetime import datetime

with open('10.2.8.177.har', 'r') as f:
    har_parser = HarParser(json.loads(f.read()))

data = har_parser.har_data
ws_entries = []
entries = []
dict_data = {}
for entry in har_parser.har_data["entries"]:
    if '_webSocketMessages' in entry.keys():
        ws_entries = entry['_webSocketMessages']
        break

for ws_entry in ws_entries:    
    if ws_entry['data'].startswith("{"):
        data = json.loads(ws_entry['data'])
        if data['type'] == 3:
            ws_entry['data'] = data
            entries.append(ws_entry)
dict_data['WS'] = entries
filename = "data_" + datetime.now().strftime("%m-%d-%Y_%H:%M:%S") + ".json"
with open(filename, 'w') as fp:
    json.dump(dict_data, fp)
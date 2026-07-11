# tool: csv_to_json
# description: Converts CSV text (with header row) to a JSON array of objects
# author: byteofhoney

# example: csv_to_json "name,age\nAlice,30" → '[{"name":"Alice","age":"30"}]'

import csv
import json
import io

def run(*args) -> str: 
    csv_text = args[0]
    if not csv_text:
        return "Error: no CSV text given"
    
    reader = csv.DictReader(io.StringIO(csv_text))
    return json.dumps(list(reader))
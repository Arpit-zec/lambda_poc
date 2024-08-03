import json
import pandas as pd

def handler(event, context):
    # Assume event contains JSON data
    data = event.get('data', [])

    # Convert JSON data to DataFrame
    df = pd.DataFrame(data)

    # Perform some transformation (example: convert to text)
    transformed_data = df.to_string(index=False)

    return {
        'statusCode': 200,
        'body': transformed_data
    }

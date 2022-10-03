import json


def parse_json(df):
    res = df.to_json(orient="records")
    parsed = json.loads(res)
    return parsed

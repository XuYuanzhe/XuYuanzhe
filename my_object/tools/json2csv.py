import json
import csv


def csv_json():
    with open("aaa.json", "r", encoding='utf-8') as f:
        lines = f.read().splitlines()

    sheet_data = []
    for line in lines:
        if line.startswith(':'):
            continue
        new_line = line.lstrip('"').rstrip('"')
        j = json.loads(new_line)
        # values = [j['_id'], j['_index'], j.get('_score', 'null'), s['AGE'], s['BIRTHDAY'], s['BPLACE'], s['HHPLACE'], s['IDNO'], s['IDTYPE'], s['QUERY_STRING'], s['RNAME'], s['SEX'], j['_type'], j['sort']]
        values = [['1', 'xyz', 'happy'], ['2', 'zsy', 'funny']]
        sheet_data.append(values)

    csv_fp = open("aaa.csv", "w", encoding='utf-8', newline='')
    writer = csv.writer(csv_fp)
    # writer.writerow(['_id', '_index', '_score', 'AGE', 'BIRTHDAY', 'BPLACE', 'HHPLACE', 'IDNO', 'IDTYPE', 'QUERY_STRING', 'RNAME', 'SEX', '_type', 'sort'])
    writer.writerow(['id', 'name', 'title', '...'])
    writer.writerows(sheet_data)
    csv_fp.close()


if __name__ == "__main__":
    csv_json()

import csv


def get_data_from_csv(file_path):
    data = []
    lines = csv.reader(open(file_path, 'rt', encoding='utf8'))
    headers = []
    is_read_header = False
    for line in lines:
        if not is_read_header:
            for col in line:
                headers.append(col)
            is_read_header = True
            continue

        d = {}
        col = 0
        for header in headers:
            d[header] = line[col]
            col = col + 1
        data.append(d)
    return data

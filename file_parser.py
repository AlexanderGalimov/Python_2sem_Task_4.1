def read_str(file):
    with open(file) as f:
        data = f.readline()
        f.close()
    return data


def write_str_to_file(data, file):
    f = open(file, 'w')
    f.write(data)
    f.close()

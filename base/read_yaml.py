import yaml


def read_yaml(filename, key):
    filepath = './data/' + filename
    with open(filepath, 'r', encoding='utf-8') as f:
        datas = yaml.safe_load(f)[key]
        # print(datas)
        arrs = []
        for data in datas.values():
            # arrs.append((data.get('username'), data.get('password'), data.get('ischecked'), data.get('toast')))
            arrs.append(data)
        return arrs


if __name__ == '__main__':
    res = read_yaml('test_login.yml', 'test_login')
    print(res)

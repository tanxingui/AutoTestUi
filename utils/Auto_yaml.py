import yaml
import pprint

from utils.Auto_path import testDatas_path


def get_yaml_data(yaml_file):
    with open(yaml_file, encoding='utf-8') as f:
        return yaml.safe_load(f.read())


if __name__ == '__main__':
    pprint.pprint(get_yaml_data(f"{testDatas_path}login_data.yaml"))

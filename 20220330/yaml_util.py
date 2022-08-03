import yaml


class YamlUtil:
    # 定义yaml文件路径参数，直接在类中使用参数
    def __init__(self, yaml_path):
        self.yaml_path = yaml_path

    # 读取 dict
    def read_yaml(self):
        with open(self.yaml_path, mode='r', encoding='utf-8') as f:
            yaml_data = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
            # 满加载方式
            return yaml_data

    # 写入
    # def write_yaml(self):


if __name__ == '__main__':
    print(YamlUtil('test.yaml').read_yaml())

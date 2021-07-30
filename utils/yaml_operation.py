import yaml




class yamlopertion:
    #@classmethod
    def read_yaml(self,yaml_path,node_name):  #读取yaml文件路径
        """

        :param yaml_path: yaml文件路径
        :param node_name:  获取数据节点名称
        :return:
        """
        with open(yaml_path,  "r",   encoding = "utf-8") as file:
            data = yaml.safe_load(file)  #安全加载yaml文件流， 或许文件内容
            #print(data)
            data_dict = data[node_name]
            #print(list(data_dict.values()))
            return list(data_dict.values())


if __name__ == '__main__':
    yamlopertion.read_yaml("self","../cp/api.yaml","testlogin")




from utils.yaml_operation import yamlopertion
from urllib.parse import urljoin
import requests
import pytest
import time
from utils.yaml_operation import yamlopertion

# print(send,'111')


# 拿到ias里的返回值
yc_data = yamlopertion.read_yaml(path_setting.YUCHAO_TEST_DATA)
print(yc_data)
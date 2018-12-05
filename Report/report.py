# 写测试报告
#
import time
#
from tools.HTMLTestRunner import HTMLTestRunner
#
import unittest
# 添加测试套件
suit = unittest.defaultTestLoader.discover("../test_fun/", pattern="test*.py")
# 构造动态时间戳， 注意日期格式
new_time = time.strftime("%Y-%m-%d-%H-%S-%M")

# 指定测试报告生成位置
path = "../Test_Report/"
# 拼接测试报告文件名
filename = path + new_time + " report.html"
with open(filename, "wb") as f:
    HTMLTestRunner(
        stream=f,
        verbosity=1,
        title="测试报告",
        description="接口自动化测试报告"

    ).run(suit)

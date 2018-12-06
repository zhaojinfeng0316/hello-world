# 导包
from ctypes import *
from Read_Data.read_txt import Read
# unittest测试框架
import unittest
#
import time
# 导入第三方工具HTMLTestRunnner 写测试报告
from tools.HTMLTestRunner import HTMLTestRunner
#
import sys
#
import re
# 实例化对象
txt = Read()
# 打印元素值
# print(txt.read()[0][0])
# 打印列表长度
# print(len(txt.read()))
# 统计列表长度
size = len(txt.read())
#
# print(txt.read()[0][0], int(txt.read()[0][1]), txt.read()[0][2])
# class Init(object):

# 载入dll
main_url = r"C:\Program Files\Passport Reader\Samples\Reading China Resident Identity Card\bin\IDCard.dll"

# second_url = r"C:\Program Files\Passport Reader\Samples\Reading China Resident Identity Card\bin"
fun_all = windll.LoadLibrary(main_url)


# class Bar(Structure):
#     __fields__ = [("count", c_int), ("values", POINTER(c_int))]
# bar = Bar()
# bar.values = (c_int * 3)(10)
# bar.count = 1

# 创建测试类
class Test(unittest.TestCase):
    # fixture
    # def setUp(self):
    #     pass
    # def tearDown(self):
    #     pass

    # 创建初始化SDK的测试用例
    # def test01_init(self):
    #     # 设置返回值类型
    #     # fun_all.InitIDCard.restype = c_int
    #     # 设置参数类型
    #     # fun_all.InitIDCard.argtypes = [c_wchar_p, c_int, main_url]
    #     # 获取返回值
    #     get_val = fun_all.InitIDCard("81805208212709351846", 1, second_url)
        # 第一个try 满足接口自动化测试需求
        # try:
        #     # 添加断言
        #     # 判断SDK初始化是否成功
        #     self.assertEqual(0, get_val)
        #     print("SDK初始化成功，实际返回值为：", get_val)

        # 第二个try 满足接口功能测试需求

            def test01_init(self):
                # 类型转换 定义入参
                InitIDCard = fun_all.InitIDCard
                InitIDCard.restype = c_int
                InitIDCard.argtypes[c_wchar_p, c_int, c_wchar_p]

               # 获取返回值
                for j in range(int(size)):

                    try:

                        # 类型转换并获取值
                        # user_id = c_wchar_p(txt.read()[j][0]).value
                        # print(user_id)
                        user_id = txt.read()[j][0]
                        # print(user_id)
                        # 类型转换并获取值
                        # init_dir = c_wchar_p(txt.read()[j][2]).value
                        # print(init_dir)
                        init_dir = txt.read()[j][2]
                        # print(init_dir)

                        get_val = InitIDCard(user_id, int(txt.read()[j][1]), init_dir)

                        # 参数化  分析定位类型转换问题  参数1和参数3  先判断参数3 再判断参数1  参数2取值正常
                        # get_val = fun_all.InitIDCard(
                        #     user_id, int(txt.read()[j][1]), init_dir)
                        # 添加断言
                        # 参数化 判断预期结果与实际结果的一致性
                        self.assertEqual(int(txt.read()[j][3]), get_val)
                        # 打印预期结果与实际结果
                        print(int(txt.read()[j][3]), get_val)
                        # 打印输出
                        print("实际返回值为：%d 第: %d次" % (get_val, j))


                    # 抛出断言异常
                    except AssertionError:
                        # print("SDK初始化失败，异常信息为：", sys.exc_info()[1])
                        # 捕获断言异常
                        raise
    # 关联
    # 设置识别的证件ID的测试用例
    # def test02_setcard(self):
        # 声明一个数组类型
        # type_int_array_2 = c_int * 2
        # 查看类型
        # print(type(type_int_array_2))
        # 统计数组大小
        # print(sizeof(type_int_array_2))
        # 实例化数组
        # new_arr = type_int_array_2()
        # 为数组赋值
        # type_int_array_2[1] = type_int_array_2(0)
        # 打印数组属性值
        # print(type_int_array_2[1])
        # 测试代码
        # aaa = (c_int * 1)()

        # 测试代码
        # print(bar.values[0])
        # 获取返回值
        # get_val = fun_all.SetIDCardID(2, bar.values[0], 1)
        # print(get_val)
        # try:
        #     self.assertEquals(0, get_val)
        #     print("成功设置识别的证件ID，实际返回值为：", get_val)
        # except AssertionError:
        #     raise


    # 卸载证件识别系统
    # def test03_revoke(self):
    #     try:
    #         fun_all.FreeIDCard()
    #         print("证件识别系统卸载成功")
    #     except Exception:





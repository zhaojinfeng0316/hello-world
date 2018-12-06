# 导包
from ctypes import *
#
# i = c_int(5)
#
# res = i.value
#
# print(res)

# 声明一个数组类型  Type[Union[c_int, c_long]]
type_int_array_2 = c_int * 2
# 查看类型
# print(type(type_int_array_2))
# 统计数组大小
# print(sizeof(type_int_array_2))
# 实例化数组
# new_arr = type_int_array_2()
# 为数组赋值
# type_int_array_2[1] = c_int(0)
# 打印数组属性值
# print(type_int_array_2[1])


# a = (c_int * 2)()
# new_a = cast(a, POINTER(c_int))
# print(new_a)

# class Bar(Structure):
#     __fields__ = [("count", c_int), ("values", POINTER(c_int))]
#
# bar = Bar()
# bar.values = (c_int * 3)(10)
# bar.count = 1
# print(bar.values[0])

# for i in range(bar.count):
#     print(bar.values[i])

# user_id = c_wchar_p("abced")
# print(user_id.value)

# 载入dll
main_url = r"C:\Program Files\Passport Reader\Samples\Reading China Resident Identity Card\bin\IDCard.dll"

second_url = r"C:\Program Files\Passport Reader\Samples\Reading China Resident Identity Card\bin"
fun_all = windll.LoadLibrary(main_url)

InitIDCard = fun_all.InitIDCard()

InitIDCard.argtypes(c_wchar_p, c_int, c_wchar_p)

InitIDCard()
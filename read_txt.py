# 封装数据读取模块
class Read():
    def read(self):
        # 打开文件
        with open("../Data/full_data.txt", "r", encoding="utf-8") as f:
            # 按行读取
            lines = f.readlines()
            # 空列表
            data_list = []
            # 将读取内容添加到列表
            for line in lines:
                data_list.append(line.strip().split(','))
            # 返回列表
            return data_list[1:]


if __name__ == '__main__':
    print(Read().read())

# import requests
#
# class google():
#     def __init__(self):
#
#         self.username='feiyabo@gmail.com'
#         self.pwd='ff@12570asdfghjkl'
#         self.baseurl='https://accounts.google.com/ServiceLogin/identifier?elo=1&flowName=GlifWebSignIn&flowEntry=AddSession'
#
#         self.stime='2019-03-15'
#         self.etime='2019-03-21'
#
#
#     def login(self):
#         login_data = dict(Email='feiyabo@gmail.com', password='1402Eighthhn')
#         url = self.baseurl
#         res = requests.get(url=url, data=login_data)
#         print(res)
#
#
# if __name__ == '__main__':
#     a=google
#     #a.login(1)
#
#
#
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
# print(fact(5))
#
# def sum(max):
#     if max <= 100 and max >= 0:
#         return max +sum(int(max) - 1)
#     else:
#         return 0
# print(sum(69.9))


class Data_test2():
    day = 0
    month = 0
    year = 0

    def __init__(self, year=0, month=0, day=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_date(cls, data_as_string):
        # 这里第一个参数是cls， 表示调用当前的类名

        year, month, day = map(int, data_as_string.split('-'))
        date1 = cls(year, month, day)  # 返回的是一个初始化后的类
        return date1

    def out_date(self):
        print("year :", self.year)
        print("month :", self.month)
        print("day :", self.day)
if __name__ == '__main__':



    # r = Data_test2.get_date("2020-3-1")
    #
    # print(r.out_date())
    #质数
    num = []
    i = 2
    for i in range(2,100):
        j = 2
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            num.append(i)
    print(num)
    #99乘法表
    for i in range(1,10):
        for j in range(1 , i+1):
            print('{}x{}={}\t'.format(j, i, j*i), end='')
        print()
    #水仙花数

    for i in range(100, 1000):
        m = i // 100  # 整除获得百位数
        n = (i % 100) // 10  # 十位数
        k = i % 10  # 个位数
        if m ** 3 + n ** 3 + k ** 3 == i:
            print(i)
    #冒泡排序
    def bubbleSort(nums):
        for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数
            for j in range(len(nums) - i - 1):  # ｊ为列表下标
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums


    nums = [5, 2, 45, 6, 8, 2, 1]

    print(bubbleSort(nums))
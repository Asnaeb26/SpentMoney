import datetime
# # from views import two_list
# from django.test import TestCase
# import unittest
#
#
# class Tests(unittest.TestCase):
#     def test_two_list(self):
#         result = two_list([2, 13, 5, 8], [6, 8, 2, 33])
#         self.assertTrue(result == [2, 8])
#
#     def test_two_list_del(self):
#         result = two_list_del([2, 13, 1], [6, 2])
#         self.assertTrue(result == [13, 1])
#
#
# def two_list(ls1, ls2):
#     ls3 = []
#     for i in ls1:
#         if i in ls2:
#             ls3.append(i)
#     return ls3
#
#
# def two_list_del(ls1, ls2):
#     ls3 = []
#     for i in ls1:
#         if i not in ls2:
#             ls3.append(i)
#     return ls3
#
#
# if __name__ == '__main__':
#     unittest.main()

class f():
    def f1():
        return ('Ну здарова')
    def f2():
        return ('Пшол нах')


def f2():
    text = f.f1() + ' отец'
    return text
def f3():
    text = f.f2() + ' отец'
    return text


# print(f2())
# print(f3())
d = 4
d1 = datetime.date(2008, 7, (d - 3))
# print(d1)
d2 = d1 + datetime.timedelta(days=25)
# print(d2)
# print(d1.strftime('%d - %B'))


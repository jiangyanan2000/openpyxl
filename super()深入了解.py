# class A:
#     def f1(self):
#         print("in A f1")
#
# class Foo(A):
#     def f1(self):
#         super().f1()
#         print("in  foo f1")
#
#
# class Bar(A):
#     def f1(self):
#         print("in Bar f1")
# class Info(Bar,Foo):
#     def f1(self):
#         super().f1()
#         print("in Info f1")
#
#
# obj = Info()
# obj.f1()
# print(Info.mro())

class A:
    def f1(self):
        print("in A")

class Foo(A):
    def f1(self):
        super().f1()
        print("in foo")
class BB(A):
    def f1(self):
        # super().f1()
        print("in bb")
class Bar(A):
    def f1(self):
        super().f1()
        print("in bar")
class Info(Foo,Bar,BB):
    def f1(self):
        super(Info,self).f1()
        print("in info f1")
obj = Info()
obj.f1()
print(Info.mro())
#super查找属性的顺序是先按照MRO查找，然后沿原路返回，执行函数

# import sys
# def s1():
#     print("s1")
# def s2():
#     print("s2")
#
# this_module = sys.modules[__name__]
# print(hasattr(this_module,"s1"))
# getattr(this_module,"s2")
# print(this_module)
# class New_int(int):
#     def __init__(self):
#         self.d = 100
#
#     def __len__(self):
#         return 555
#
# n = New_int()
# print(n.d)
# print(len(n))
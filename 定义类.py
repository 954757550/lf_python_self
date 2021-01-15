
class Person():
    #特征 对应人的特征
    #name = '大明'#类属性


    #行为 对应人的行为，实例方法
    #实例方法：在类的内部，使用def关键字来定义，第一次参数默认是self【名字标识可以是其他的名字，但这个位置必须被占用
    def __init__(self,name,sex,age):
        #self.name = input('输入姓名：') #实例属性
        # 在方法内部定义的【通过类似于self.变量名】变量，是实例属性
        self.name = name
        self.sex = sex
        self.age = age#实例属性的声明
        pass

    def eat(self,food):
        print(self.name + '喜欢吃' + food )
        pass
    def run(self): #实例方法
        print("run run run!!!!1")
        pass
pass
 # 对象是实实在在的一个东西，类的实例化，具象化
 #类是对象的抽象化，而对象是类的 一个实例
 #实例方法归于 类的实例所有
 #属性 ： 在类的内部定义的变量【类属性】

xm = Person('小明','女','19岁') #类的实例化
xp = Person('小鹏','男','18岁')
xm.eat('榴莲')
xp.eat('apple')
xm.run()
print("{}的年龄是{}".format(xm.name,xm.age))
print("{}的年龄是{}".format(xp.name,xp.age))
'''
__init__总结
1。python自带的额内置函数，具有特殊的函数，使用双下划线包起来的【魔术方法】
2。是一个初始化的方法，用来定义实例属性 和初始化数据的 ，在创建对象的时候自动调用，不用手动调用
3。利用传参的机制让我们定义功能更加强大并且方便的一类
'''
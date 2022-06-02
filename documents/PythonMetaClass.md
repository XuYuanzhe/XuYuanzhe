# Python元类

```python
class MyType(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('MyType __init__')

    def __new__(cls, *args, **kwargs):
        new_cls = super().__new__(cls, *args, **kwargs)
        print('MyType __new__')
        return new_cls

    def __call__(self, *args, **kwargs):
        # 1.调用自己的类 __new__ 去创建对象
        empty_object = self.__new__(self)

        # 2.调用自己的类 __init__ 去初始化对象
        self.__init__(empty_object, *args, **kwargs)
        print('MyType __call__')
        return empty_object


# 假设 Foo 是一个对象由 MyType 创建
class Foo(object, metaclass=MyType):
    def __init__(self, name):
        print('Foo __init__')
        self.name = name

    def __new__(cls, *args, **kwargs):
        new_cls = super().__new__(cls, *args, **kwargs)
        print('Foo __new__')
        return new_cls

    def __call__(self, *args, **kwargs):
        print('Foo __call__')


# __call__ 方法只有在 `对象()` 的是和会被调用，这里假设 Foo 是一个对象由 MyType 创建
f = Foo('Tom')
print('------分割线------')
# f 是一个对象由 Foo 创建
f()

```
output
```text
MyType __new__
MyType __init__
Foo __new__
Foo __init__
MyType __call__
------分割线------
Foo __call__
```
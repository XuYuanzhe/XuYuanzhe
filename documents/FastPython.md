# 让 Python 程序变慢的几个坏习惯

1 不要导入根模块
-----

在使用 Python 时，我们无法避免的一件事是导入模块，无论是内置模块还是第三方模块。有时，我们可能只需要该模块中的一个或几个函数或对象。 在这种情况下，我们应该尝试只导入我们需要的函数或对象，而不是导入根模块。

Use `from math import sqrt` instead of `import math`

2 避免使用点/点链
-----

使用 dot 非常直观。 在 Python 中访问对象的属性或函数。 大多数时候，没有问题。 但是，如果我们可以避免使用点甚至链接点，性能实际上会更好。

```python
my_list = [1, 2, 3]

# slow
my_list.append(4)

# fast
append = my_list.append
append(4)
```

3 不要使用 + 连接字符串
-----

字符串在 Python 中是不可变的。 因此，当我们使用"+"将多个字符串连接成一个长字符串时，每个子字符串都是单独操作的。具体来说，对于每个子字符串，它需要请求一个内存地址，然后将它与该内存地址中的原始字符串连接起来,这成为一种开销。
但是，当我们使用 join() 函数时，该函数事先知道所有子字符串，并且内存地址分配的长度适合最终连接的字符串。 因此，没有为每个子串分配内存的开销。
强烈建议尽可能使用 join() 函数。 但是，有时我们可能只想连接两个字符串。 或者，只是为了方便起见，我们想使用“+”。 在这些情况下，使用“+”号会带来更好的可读性和更少的代码长度。

```python
str_list = ['hello', 'world', '!']

# slow
def slow_foo(s_list):
    result = ''
    for s in s_list:
        result += ' ' + s
    return result[1:]

# fast
def fast_foo(s_list):
    return ' '.join(s_list)
```

4 不要使用临时变量进行价值交换
-----

在 Python 中，我们不必使用 temp 变量。Python 具有内置语法来实现此值交换。

```python
# slow
a = 1
b = 2
temp = a
a = b
b = temp

# fast
c = 1
d = 2
c, d = d, c
```

5 使用 If-Condition 短路
-----

"短路"评估存在于许多编程语言中，Python 也是如此。基本上，它指的是某些布尔运算符的行为，其中仅当第一个参数不足以确定整个表达式的值时才执行或评估第二个参数。
对列表进行过滤，找出所有名字以"C"开头，年龄大于等于30岁的人。

```python
my_dict = [
    {'name': 'Alice', 'age': 28},
    {'name': 'Bob', 'age': 23},
    {'name': 'Chris', 'age': 33},
    {'name': 'Chelsea', 'age': 2},
    {'name': 'Carol', 'age': 24}
]

# slow
def slow_foo():
    filtered_list = []
    for person in my_dict:
        if person['name'].startswith('C') and person['age'] >= 30:
            filtered_list.append(person)

# fast
def fast_foo():
    filtered_list = []
    for person in my_dict:
        if person['age'] >= 30 and person['name'].startswith('C'):
            filtered_list.append(person)
```

6 如果可以使用For循环就不要使用While循环
-----

Python 使用了很多 C 来提高性能，即 CPython。在循环语句方面，Python 中的 For-Loop 具有相对较少的步骤，其中更多的步骤作为 C 代码运行，而不是 While-Loop。

因此，当我们可以在 Python 中使用 For-Loop 时，我们不应该使用 while 循环。这不仅是因为 For-Loop 在 Python 中更优雅，而且性能更好。

Use `for i in range(10)` instead of `while i < 10`
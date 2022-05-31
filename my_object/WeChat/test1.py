import functools


# def decorator(fn):
#     context = 1
#
#     def wrapper(*args, **kwargs):
#         print("context", context)
#         return fn(*args, **kwargs)
#
#     return wrapper

# @decorator
# def func():
#     print("I am target")

def decorator_out(context):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print(context)
            return fn(*args, **kwargs)

        return wrapper

    return decorator


@decorator_out(3)
def test(*args, **kwargs):
    print(1)


test()

'''
def decorator(name):
    def outer(func):
        c = 1
        def inner(*args, **kwargs):
            nonlocal c
            c += 1
            print(f'before {name} {c}')
            result = func(*args, **kwargs)
            print('after')
            return result
        return inner
    return outer
'''
'''
Два декоратора
1. Выводит на экран время выполения функции
2. Количество ее вызов
*3. кеширует результат
'''
import time, sys
def check_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'time working: {(end - start):.2f}')
        return result
    return inner

def call_times(func):
    counter = 0
    def inner(*args, **kwargs):
        nonlocal counter
        counter +=1
        result = func(*args, **kwargs)
        print(f'call times: {counter}')
        return result
    return inner
def caching_result(func):
    cache = {}
    def inner(*args,**kwargs):
        nonlocal cache
        args_str = '_'.join(str(arg) for arg in args)
        kwargs_str = '_'.join(f'{key}={value}' for key, value in sorted(kwargs.items()))
        combined_str = f"{args_str}__{kwargs_str}" if kwargs_str else args_str
        if cache.get(combined_str):
            return cache[combined_str]
        result = func(*args, **kwargs)
        cache[combined_str] = result
        return result
    return inner
@check_time
@call_times
@caching_result
def sum_numbers(a, b):
    print('qweqwe')
    time.sleep(3)
    return a + b


if __name__ == '__main__':
    print(sum_numbers(1, 5))
    print(sum_numbers(1, 5))
    print(sum_numbers(1, 5))


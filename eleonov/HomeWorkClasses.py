import functools
import time


def memorized(func):

    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = args[1:]
        if key in inner.cache:
            inner.cacheable += 1
            inner.cache[key][1] += 1
        else:
            if len(inner.cache) == l.cache_limit:
                result = sorted(inner.cache.items(), key=lambda x: x[1][1])
                print("Deleted: ", result[0])
                del inner.cache[result[0][0]]
            with Timer() as t:
                result = func(*args)
                rt = t.running_time

            inner.cache[key] = []
            inner.cache[key].append(result)
            inner.cache[key].append(1)
            inner.cache[key].append(t.running_time)
            inner.noncacheable += 1
        inner.calculations += 1
        return inner.cache[key][0]
    inner.cache = {}
    inner.cacheable = 0
    inner.noncacheable = 0
    inner.calculations = 0
    inner.longest_calc = 0
    return inner


class Timer(object):
    def __enter__(self):
        self.starttime = time.time()
        return self

    def __exit__(self,  exc_type, exc_val, exc_tb):
        self.running_time = "{:.3f} sec".format(time.time() - self.starttime)
        return self.running_time


class CacheCalc:

    def __init__(self, init_cache_limit=50):
        self.cache_limit = init_cache_limit

    @memorized
    def sum_numbers(self, *args):
        return sum(args)

    def most_common_calc(self,cache):
        return sorted(cache.items(), key=lambda x: x[1][1], reverse=True)

    def longest_running(self,cache):
        result = sorted(cache.items(), key=lambda x: x[1][2])
        return result[0]

    def save_results(self,filename):
        with open(filename, "w") as f:
            f.write(str(self.most_common_calc(l.sum_numbers.cache)))
        pass

    def show_results(self):
        print('cacheble: ', self.sum_numbers.cacheable)
        print('noncacheble: ', self.sum_numbers.noncacheable)
        print('calculations: ', self.sum_numbers.calculations)
        print('cache: ', self.sum_numbers.cache)

l = CacheCalc(3)
print("cache limit: ", l.cache_limit)
l.sum_numbers(1, 7, 12, 56, 10)
for i in range(4):
    l.sum_numbers(2, 2, 3, 4, 5, 6, 7, 8, 9, 2, 2, 3, 4, 5, 6, 7, 8, 9, 2, 2, 3, 4, 5, 6, 7, 8, 9, 2, 2, 3, 4, 5, 6, 7, 8, 9)
for i in range(3):
    l.sum_numbers(3, 2, 3, 4, 5, 6, 7, 8)
for i in range(4):
    l.sum_numbers(4, 2, 3, 4, 5, 6, 7)
for i in range(5):
    l.sum_numbers(5,9,0,2,3,4,5,6,7)

l.show_results()
l.save_results('results.txt')
print("Most common calculation: ", l.most_common_calc(l.sum_numbers.cache))
print("Longest calculation: ", l.longest_running(l.sum_numbers.cache))


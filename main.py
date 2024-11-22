import time
def measure_time(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time
def test1():
    time.sleep(1)
    return "Test1 виконано"
def test2(n):
    total = 0
    for i in range(n):
        total += i
    return total
def test_measure_time():
    time_taken = measure_time(test1)
    print(f"Час виконання test1: {time_taken} секунд")
    time_taken = measure_time(test2, 1000000)
    print(f"Час виконання test2: {time_taken} секунд")
if __name__ == "__main__":
    test_measure_time()

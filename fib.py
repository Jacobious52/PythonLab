# calcuate fib nums recursively
# Benchmark for fib.* for n = 40
# Rust: 2.9s
# Python: 93.6s
# C/C++: 1.8s

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():
    n = 40
    for i in range(n):
        print('fib %s = %s' % (i, fib(i)))

if __name__ == '__main__':
    main()

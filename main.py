with open('numbers.txt') as f:
    data = list(map(int,f.readline().split()))

def min_(data=data):
    return min(data)

def max_(data=data):
    return max(data)

def sum_(data=data):
    return sum(data)

def mult_(data=data):
    result = 1
    for i in data:
        result *= i
    return result

def main():
    print(f'Минимальное число: {min_()}')
    print(f'Максимальное число: {max_()}')

    print(f'Сумма чисел: {sum_()}')
    print(f'Произведение чисел: {mult_()}')


if __name__ == '__main__':
    main()

def parity_01(data: int):
    result = 0
    while data:
        print('data & 1: ', data & 1)
        result ^= data & 1
        print('result: ', result)
        data = data >> 1
        print('data: ', data)
    return result

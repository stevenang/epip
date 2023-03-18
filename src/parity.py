
def parity_01(data: int):
    result = 0
    while data:
        #print('data: ', data)
        #print('data & 1: ', data & 1)
        result ^= data & 1
        #print('result: ', result)
        data = data >> 1
    return result

def parity_02(data: int):
    result = 0
    while data:
        #print('data: ', data)
        result ^= 1
        #print('result: ', result)
        data &= data -1
    return result

'''
def parity_03(data: int):
    mask_size = 16
    bit_mask = 0xFFFF
    return (
        PRECOMPUTED_PARITY[data >> (3 * mask_size)] ^
        PRECOMPUTED_PARITY[(data >> (2 * mask_size)) & bit_mask] ^
        PRECOMPUTED_PARITY[(data >> mask_size) & bit_mask] ^
        PRECOMPUTED_PARITY[data & bit_mask]
    )
'''
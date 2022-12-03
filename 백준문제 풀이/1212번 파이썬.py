num = input()
num = '0o'+num
int_num = int(num, 8)
bin_num = bin(int_num).replace('0b', '')
print(bin_num)

"""
print(f'{int(input(),8):b}')
"""

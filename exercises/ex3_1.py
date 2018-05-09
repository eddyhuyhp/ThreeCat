#!/usr/bin/env python3
def solve(input_data):
    '''Đầu vào: một số nguyên dương

    Đầu ra: số nguyên tạo bởi phần từ số 1 cuối cùng trở về bên
    phải - của dạng binary của số đầu vào.

    Ví dụ::

      input_data = 5 # (0101)
      output = 1

      input_data = 24 (11000)
      output = 1000

      input_data = 9 (1001)
      output = 1

    Hàm có sẵn: bin(10) == '0b1010'
    Hàm có sẵn tạo ra integer từ string: 69 == int('69')
    '''

    result = None
    a = bin(input_data)
    result = a[len(a)-a[::-1].find('1')-1:len(a)]


    return result


def main():
    i = input('Nhap vao so nguyen:')
    print(solve(int(i)))


if __name__ == "__main__":
    main()

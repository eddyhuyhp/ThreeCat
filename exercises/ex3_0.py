#!/usr/bin/env python3


def squared(input_data):
    '''Tính bình phương của số đầu vào

    Số đầu vào ở đây được chứa trong tên `input_data`,
    được cung cấp sẵn bởi bài tập. Học viên chỉ cần lo tính toán ra kết quả
    dựa trên `input_data` đã cho.
    '''
    result = None

    # Xoá dòng raise và Viết code vào đây set các giá trị phù hợp
    # Uncomment dòng sau để có kết quả đúng
    result = input_data ** 2
    return result

def main():
    a = input('Nhap so can binh phuong:')
    print(squared(int(a)))


if __name__ == "__main__":
    main()

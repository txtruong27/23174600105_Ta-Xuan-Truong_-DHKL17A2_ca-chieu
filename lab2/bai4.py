diem = float(input("Nhập điểm số của bạn: "))

if diem >= 0 and diem < 5:
    print("Điểm kém")
elif diem >= 5 and diem < 7:
    print("Điểm trung bình")
elif diem >= 7 and diem < 8.5:
    print("Điểm khá")
elif diem >= 8.5 and diem <= 10:
    print("Điểm tốt")
else:
    print("Điểm bạn nhập không hợp lệ.")
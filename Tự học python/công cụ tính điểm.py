k = float(input('Hệ số: '))
t = float(input('Điểm thi: '))
q = float(input('Điểm quá trình: '))
S = k*t +(1-k)*q
if S <= 4 :
    print('Điểm tổng kết: ', S)
    print('Bạn phải thi lại')
    Tnew = float(input('Điểm thi mới: '))
    Snew = min(7,max(k*Tnew+(1-k)*q, S))
    print('Điểm thi mới: ',Snew)
elif 4<= S <= 5.4:
    print('Điểm tổng kết: ',S)
    print('Bạn có thể học cải thiện điểm')
    ykien = bool(input('Bạn đã học cải thiện điểm chưa: (True/False) '))
    if ykien == True :
        Tnew = float(input('Điểm thi mới: '))
        Qnew = float(input('Điểm quá trình mới: '))
        Snew = max(k*Tnew + (1-k)*Qnew, 1/2*(k*Tnew + (1-k)*Qnew + S),4)
    print('Điểm thi mới: ', Snew)
else :
    print('Điểm tổng kết: ', S)

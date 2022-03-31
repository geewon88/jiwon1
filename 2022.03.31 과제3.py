#문제1
price_list=[32100,32150,32000,32500]
count=-1
for i in price_list:
    count+=1
    print(count,i)

#문제2
price_list1_2=[32100,32150,32000,32500]
count=90
for a in range(1,4):
    count+=10
    print(count, price_list1_2[a])


#문제3
for b in range(2002,2051,4):
    print('올림픽 개최년도: {}' .format(b))

#문제4
for c in range(0,10):
    print(float(c/10))

#문제5
ticker='btc_krw'
print(ticker.upper())

#문제6
file_name= '보고서.xlsx'
print(file_name.endswith('xlsx'))

#문제7
인사= 'hello world'
print(인사.split(' '))

#문제8
date='2020-05-01'
순서= date.split('-')
print('연도: {}'.format(순서[0]))
print('월: {}'.format(순서[1]))
print('일: {}'.format(순서[2]))

#문제9
상장주식수 = '5,969,782,550'
상장주식수_2= 상장주식수.replace(",","")
print(int(상장주식수_2))

#문제10
print('문제 7번과 동일합니다.')

#문제11
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#문제12
num = [1,2,3,4,5,6,7,8,9,10]
print(num[1:10:2])

#문제13
리스트 = [3, 6 ,23,44]
for d in 리스트:
    if d%3 == 0:
        print(d)

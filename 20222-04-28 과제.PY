import numpy as np

#중복된 원소 제거
c=[3,3,4,5,6,6,6,7,8,8,9]
new_c=[]
for i in c:
    if i not in new_c:
        new_c.append(i)
print(new_c)

#합집합
# 중복이 없는 경우 
A=['apple', 'melon', 'oreange']
B=['chicken', 'pig', 'cow']
C=A+B
print(C)

#중복이 있는 경우
A1=['apple', 'melon', 'oreange']
B1=['chicken', 'pig', 'cow','apple']
new_AB=[]
for i in A1:
    if i not in B1:
        new_AB.append(i)
new_AB=new_AB+B1
print(new_AB)

#교집합
a3=[1,2,3]
b3=[2,3,4,5,6]
c3=[]
for i in a3:
    if i in b3:
        c3.append(i)
print(c)

#차집합
#방법1
a4=[1,2,3]
b4=[2,3,4,5,6]
c4=[]
for i in a4:
    if i not in b3:
        c4.append(i)
print(c4)

#방법2
a4=[1,2,3]
b4=[2,3,4,5,6]
c4_2=a4+[]
for i in a4:
    if i in b4:
        c4_2.remove(i)
print(c4_2)

#여집합
#방법1
U5=[1,2,3,4,5]
a5=[1,2,3]
a5_com = []
for i in U5:
    if i not in a5:
        a5_com.append(i)
print(a5_com)

#방법2
U5=[1,2,3,4,5]
a5=[1,2,3]
rest=U5+[]
for i in U5:
    if i in a5:
        rest.remove(i)
print(rest)

#소수 알아보기
print('')
print('')
print('소수알아보기 문제입니다')
print('')
a6=int(input('숫자를 입력해주세요'))
print('')

b6=True
for i in range(2,a6):
    if a6%i==0:
        b6=False
if b6 == True:
    print('{}는 소수입니다'.format(a6))
else:
    print('{}는 소수가 아닙니다.'.format(a6))

#약수 찾기
print('')
print('')
print('약수 찾기 문제입니다')
print('')
a7=int(input('숫자를 입력해주세요'))
print('')
factor2=[]
for i in range(1,a7+1):
    if a7%i==0:
        factor2.append(i) 
print('{}의 약수는 {}입니다.'.format(a7,factor2))

#최대 공약수와 최대 공배수 구하기
print('')
print('')
print('최대공약수와 최대공배수를 구하는 문제입니다')
print('')
a8=int(input('첫번째 숫자를 입력해주세요'))
print('')
a8_factors=[]
b8=int(input('두번째 숫자를 입력해주세요'))
print('')
b8_factors=[]
for i in range(1,a8+1):
    if a8%i==0:
        a8_factors.append(i)
for i in range(1,b8+1):
    if b8%i==0:
        b8_factors.append(i)

fators8=[]
for i in a8_factors:
    if i in b8_factors:
        fators8.append(i)
fators8_max=max(fators8)
print('두수의 최대공약수는 {}이다'.format(fators8_max))
ab8=a8*b8
LCM=int(ab8/fators8_max)
print('두수의 최대공배수는 {}이다'.format(LCM))





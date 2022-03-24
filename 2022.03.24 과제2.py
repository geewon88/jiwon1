#1번
letters = 'python'
print('첫번째 문자는 {}, 세번째 문자는 {} 입니다'. format(letters[0],letters[2]))

#2번
string='PYTHON'
print('PYTHON을 거꾸로 출력하면 {} 입니다.'.format(string[::-1]))

# #3번
url=input('url 주소 알려주세요')
index=url.split('.')
print('도메인은 {}입니다'.format(index[1]))

#4번
file_name='보고서.xlsx'
print(file_name.endswith('xlsx')) #xlsx로 끝나므로 True가 출력됨

#5번
file_name2='2020_보고서.xlsx'
print(file_name2.startswith('2020')) #2020으로 시작되므로 True가 출력됨

# #6번
score=int(input('학점 알려주세요'))
if 81<=score<=100:
    print('학점은 A입니다.')
elif 61<=score<=81:
    print('학점은 B입니다.')
elif 41<=score<=60:
    print('학점은 C입니다.')
elif 21<=score<=40:
    print('학점은 D입니다.')
else:
    print('학점은 E입니다.')

#7번
cook=['피자','김밥','만두','양념치킨','족발','피자','김치만두','쫄면','소시지','라면','팥빙수','김치전']
print('리스트에 저장된 데이터의 개수는 {}개 입니다'.format(len(cook)))

#8번
list=['Microoft','Google','Naver', 'Kakao', 'SAMSUNG','LG']
warn_investment_list=[x.lower() for x in list]
investment=input('투자 종목이 뭐예요?')
lower=investment.lower()
if lower==warn_investment_list[0]:
    print('투자 경고 종목이 아닙니다')
elif lower==warn_investment_list[1]:
     print('투자 경고 종목이 아닙니다')
elif lower==warn_investment_list[2]:
     print('투자 경고 종목이 아닙니다')
elif lower==warn_investment_list[3]:
     print('투자 경고 종목이 아닙니다')
elif lower==warn_investment_list[4]:
     print('투자 경고 종목이 아닙니다')
elif lower==warn_investment_list[5]:
     print('투자 경고 종목이 아닙니다')
else:
    print('투자 경고입니다.') 

#9번
리스트=[100, 200, 300]
for i in 리스트:
    print(i)

#10번
리스트2=['sk하이닉스','삼성전다','LG전자']
for i in 리스트2:
    print('문자열의 길이는 {}개 입니다'.format(len(i)))
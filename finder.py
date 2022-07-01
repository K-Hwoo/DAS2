
f = open('it_data.txt', 'r')
lines = f.readlines() # data_IT_.csv 파일의 id가 리스트로 저장 되어있음
 # 에러나서 튕겼을 시 아래 문구 추가
 # lines = lines[이어갈 부분 id의 리스트 인덱스 : ]
f.close()
print(lines.index('90067\n'))
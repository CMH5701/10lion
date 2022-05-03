#메뉴 정하기
import time
import random
lunch = ["학식", "토마토", "맷돌", "배달","우가본"]
#while True:
    #item = input("음식을 추가 해주세요: ")
    #lunch.append(item)
    #print(lunch)
while True:
    print(lunch)
    item = input("음식을 추가 해주세요 : ")
    if(item == "q"):
        print("메뉴")
        break
    else:
        lunch.append(item)
set_lunch = set(lunch)#원소를 집합으로 변경
while True:
    print(set_lunch)
    item = input("음식을 삭제해주세요 : ")
    if(item == "q"):
        break
    else:
        set_lunch = set_lunch - set([item])#리스트로 변경후[] 집합으로 변경()와 set추가
print(set_lunch, "중에서 선택합니다.")        
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
print(random.choice(list(set_lunch)))
import sys
print("리스트 원소 개수 입력:")
list_size = int(sys.stdin.readline().rstrip())
i = 0
list_entity=list(map(int,input().split(",")))
#print(list_entity) 
int_target = int(sys.stdin.readline().rstrip())
print("두 수의 합이",int_target,"인 원소 쌍")

for x in range(len(list_entity)):
    for y in range(x+1,len(list_entity)):
        if(list_entity[x]+list_entity[y]==int_target):
            print(x+1,"번째와 ",y+1,"번째 원소")
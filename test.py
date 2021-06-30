a,b=map(int,input().split())
target=[list(map(int,input().split())) for i in range(b)]
print(target)
board=[list(map(int,input().split())) for i in range(a)]
answer=[]
for i in range(b):
    x1,y1=target[i][0],target[i][1]
    x2,y2=target[i][2],target[i][3]
    temp=0
    for m in range(x1,x2+1):
        for n in range(y1,y2+1):
            if m-1>=a or n-1>=a:
                continue
            print(m-1,n-1)
            temp+=board[m-1][n-1]
    answer.append(temp)
print(answer)
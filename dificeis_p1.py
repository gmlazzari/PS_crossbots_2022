n = input("")

for i in range(n):
    mina = input("")
    dima =  0
    count = 0
    for j in range(len(mina)):
        if(mina[j] == '<'):
            count += 1
        elif(mina[j] == '>' and count > 0):
            count -= 1
            dima += 1
               
print(dima)
                

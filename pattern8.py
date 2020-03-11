def pattern8():
    for i in range(7,1,-1):
        for j in range(1,i-1):
            print(j,end='\t')
            for k in range(5,1,-1):
                print('*',end='\t')
        print("\n")            
pattern8()

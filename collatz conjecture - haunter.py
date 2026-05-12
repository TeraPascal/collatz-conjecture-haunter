while True:
    print("\n-------------------------------\n\n.\n..\n...\n..\n.\n")
    
    def collatzseries(lis):
        while lis[len(lis)-1] != 1:
            last = lis[len(lis)-1]
            if last % 2 == 0:
                lis.append(last/2)
            else :
                lis.append(last*3+1)
        return(len(lis)-1)
                              
    limit = int(input('maximum number of the fact check range for collatz conjecture :\n  >  '))
    print()

    for n in range(limit):
        n = [n+1]
        serieslen = collatzseries(n)
        print(f"the length of collatz series for number {n[0]} is {serieslen} \n")
            
        

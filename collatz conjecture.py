while True:
    print("\n-------------------------------\n\n.\n..\n...\n..\n.\n")
    
    series = [int(input('num :\n  >  '))]
    print()

    while series[len(series)-1] != 1:
        last = series[len(series)-1]
        if last % 2 == 0:
            series.append(last/2)
        else :
            series.append(last*3+1)
            
    print(f"the collatz series for the given number has {len(series)-1} arrays and the arrays are as follwos:\n  > {series}")
        
        

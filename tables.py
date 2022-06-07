for i in range(1,11):
    for j in range(1,11):
        x="{} x {} ={}".format(j,str(i).zfill(2),str(j*i).zfill(2))
        print(x, end="  ")
    print()

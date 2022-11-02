x=1534236469
x_revers=int(str(abs(x))[::-1])
if x>=0 and x_revers<2**31:
    print(x_revers)
elif x<0 and x_revers<2**31:
    print(-1 * x_revers)
else:
    print(0)
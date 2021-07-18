H,M = map(int,input().split())
if(H!=0):
    H=H*60
earlytime = H+M-45
result_hour=earlytime//60
if (earlytime//60 <0):
    result_hour=24+earlytime//60
else:
    result_hour=earlytime//60
result_min=earlytime%60

print(result_hour,result_min)

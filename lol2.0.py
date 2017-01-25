f=open('zdf-win.txt','r')
vovels="уеёыаоэяию"
bukvi="брн"#буквы данные в условии
result=[]
ok=bukvi+vovels
slovo=f.readline()
while (slovo!=''):
    a=1
    slovo=slovo[:-1]
    for simvol in slovo:
        if not(simvol in ok):
            a=0
    if a==1 and len(slovo)>5:
        result.append(slovo)
    slovo=f.readline()
        
result.sort()
print(result)
f.close()
           
a=int(input())            

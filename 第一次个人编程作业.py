def 输入():
    str=input()
    s=str.split()
    if len(s)>0:
        if s[0]=='整数':
            a[0]=s[1]
        elif s[0]=='看看' or s[0]=='如果':
            a[0]=s[1]
        else:
            a[0]=s[0]
        return s
    else:
        return None

def 转换(s):
    if len(s)<=2:
        s[1]=s[1]
    elif s[2]=='零':
        s[2]=0
    elif s[2]=='一':
        s[2]=1
    elif s[2]=='二':
        s[2]=2
    elif s[2]=='三':
        s[2]=3
    elif s[2]=='四':
        s[2]=4
    elif s[2]=='五':
        s[2]=5
    elif s[2]=='六':
        s[2]=6
    elif s[2]=='七':
        s[2]=7
    elif s[2]=='八':
        s[2]=8
    elif s[2]=='九':
        s[2]=9
    elif s[2]=='十':
        s[2]=10
    elif s[3]=='零':
        s[3]=0
    elif s[3]=='一':
        s[3]=1
    elif s[3]=='二':
        s[3]=2
    elif s[3]=='三':
        s[3]=3
    elif s[3]=='四':
        s[3]=4
    elif s[3]=='五':
        s[3]=5
    elif s[3]=='六':
        s[3]=6
    elif s[3]=='七':
        s[3]=7
    elif s[3]=='八':
        s[3]=8
    elif s[3]=='九':
        s[3]=9
    elif s[3]=='十':
        s[3]=10
    return s

def 转换2():
    if a[1]==0:
        a[3]='零'
    elif a[1]==1:
        a[3]='一'
    elif a[1]==2:
        a[3]='二'
    elif a[1]==3:
        a[3]='三'
    elif a[1]==4:
        a[3]='四'
    elif a[1]==5:
        a[3]='五'
    elif a[1]==6:
        a[3]='六'
    elif a[1]==7:
        a[3]='七'
    elif a[1]==8:
        a[3]='八'
    elif a[1]==9:
        a[3]='九'
    elif a[1]==10:
        a[3]='十'
    return s

def 使用(s):
    if (s[0]=='整数') and (s[2]=='等于'):
        a[0]=s[1]
#         print(a[0])
        a[1]=s[3]
#         print(a[1])
    if s[0]==a[0]:
        if s[1]=='减少':
            a[1]=a[1]-s[2]
#             print(a[1])
        elif s[1]=='增加':
            a[1]=a[1]+s[2]
#             print(a[1])
    if s[0]=='看看':
        转换2()
        print(a[3])
    if s[0]=='如果':
        if s[2]=='大于':
            if a[1]>s[3]:
                s[6]=s[6].strip('“').strip('”')
                print(s[6])
            else:
                s[9]=s[9].strip('“').strip('”')
                print(s[9])

a=['',0,0,'']
while(1):
    s=输入()
    if s!=None:
        s=转换(s)
        使用(s)
    else:
        print('结束')
        break
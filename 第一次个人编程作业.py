def 输入():
    global bls
    global i
    str=input()
    s=str.split()
    if len(s)>0:
        return s
    else:
        return None

def 转换中的小函数(s,k,w):
    x=0
    for i in range(w,len(s[k])):
        if s[k][i]=='一':
            x=x+1
        elif s[k][i]=='二':
            x=x+2
        elif s[k][i]=='三':
            x=x+3
        elif s[k][i]=='四':
            x=x+4
        elif s[k][i]=='五':
            x=x+5
        elif s[k][i]=='六':
            x=x+6
        elif s[k][i]=='七':
            x=x+7
        elif s[k][i]=='八':
            x=x+8
        elif s[k][i]=='九':
            x=x+9
        elif s[k][i]=='十':
            if i==w:
                x=(x+1)*10
            else:
                x=x*10
        elif s[k][i]=='百' or s[k][i]=='千' or s[k][i]=='万':
            if i+3<len(s[k]):
                if (s[k][i]=='万' and s[k][i+2]=='千') or (s[k][i]=='千' and s[k][i+2]=='百') or (s[k][i]=='百' and s[k][i+2]=='十'):
                    x=x*10
                elif (s[k][i]=='万' and s[k][i+2]=='百') or (s[k][i]=='万' and s[k][i+3]=='百') or (s[k][i]=='千' and s[k][i+2]=='十') or (s[k][i]=='千' and s[k][i+3]=='十'):
                    x=x*100
                elif (s[k][i]=='万' and s[k][i+2]=='十') or (s[k][i]=='万' and s[k][i+3]=='十'):
                    x=x*1000
            elif s[k][i]=='万' and i+5>=len(s[k]):
                x=x*10000
            elif s[k][i]=='千' and i+4>=len(s[k]):
                x=x*1000
            elif s[k][i]=='百' and i+3>=len(s[k]):
                x=x*100
    return x

def 汉字转数字(s):
    x=0
    if len(s)<=2:
        s[1]=s[1]
    elif s[0]=='整数' or s[0]=='如果':
        k=3
        if s[3][0]=='负':
            w=1
            x=转换中的小函数(s,k,w)
            x=x*(-1)
        else:
            if s[3]=='零':
                x=0
            else:
                w=0
                x=转换中的小函数(s,k,w)
        s[3]=x
    elif s[1]=='减少' or s[1]=='增加':
        k=2
        if s[2][0]=='负':
            w=1
            x=转换中的小函数(s,k,w)
            x=x*(-1)
        else:
            if s[2]=='零':
                x=0
            else:
                w=0
                x=转换中的小函数(s,k,w)
        s[2]=x
    return s

def 数字转汉字(i):
    a[i][3]=''
    j=0
    if a[i][1]<=10 and a[i][1]>=0:
        if a[i][1]==0:
            a[i][3]='零'
        elif a[i][1]==1:
            a[i][3]='一'
        elif a[i][1]==2:
            a[i][3]='二'
        elif a[i][1]==3:
            a[i][3]='三'
        elif a[i][1]==4:
            a[i][3]='四'
        elif a[i][1]==5:
            a[i][3]='五'
        elif a[i][1]==6:
            a[i][3]='六'
        elif a[i][1]==7:
            a[i][3]='七'
        elif a[i][1]==8:
            a[i][3]='八'
        elif a[i][1]==9:
            a[i][3]='九'
        elif a[i][1]==10:
            a[i][3]='十'
    elif a[i][1]>10:
        b=a[i][1]
        for j in range(10):
            if b%10==1:
                a[i][3]=''.join(['一',a[i][3]])
            elif b%10==2:
                a[i][3]=''.join(['二',a[i][3]])
            elif b%10==3:
                a[i][3]=''.join(['三',a[i][3]])
            elif b%10==4:
                a[i][3]=''.join(['四',a[i][3]])
            elif b%10==5:
                a[i][3]=''.join(['五',a[i][3]])
            elif b%10==6:
                a[i][3]=''.join(['六',a[i][3]])
            elif b%10==7:
                a[i][3]=''.join(['七',a[i][3]])
            elif b%10==8:
                a[i][3]=''.join(['八',a[i][3]])
            elif b%10==9:
                a[i][3]=''.join(['九',a[i][3]])
            b=int(b/10)
            if b==0:
                break
            elif b!=0:
                if b%10!=0:
                    if j==0:
                        a[i][3]=''.join(['十',a[i][3]])
                    elif j==1:
                        a[i][3]=''.join(['百',a[i][3]])
                    elif j==2:
                        a[i][3]=''.join(['千',a[i][3]])
                    elif j==3:
                        a[i][3]=''.join(['万',a[i][3]])
                    elif j==4:
                        a[i][3]=''.join(['十',a[i][3]])
                    elif j==5:
                        a[i][3]=''.join(['百',a[i][3]])
                    elif j==6:
                        a[i][3]=''.join(['千',a[i][3]])
                    elif j==7:
                        a[i][3]=''.join(['亿',a[i][3]])
                    elif j==8:
                        a[i][3]=''.join(['十',a[i][3]])
                    elif j==9:
                        a[i][3]=''.join(['百',a[i][3]])
    elif a[i][1]<0:
        b=a[i][1]*(-1)
        for j in range(10):
            if b%10==1:
                a[i][3]=''.join(['一',a[i][3]])
            elif b%10==2:
                a[i][3]=''.join(['二',a[i][3]])
            elif b%10==3:
                a[i][3]=''.join(['三',a[i][3]])
            elif b%10==4:
                a[i][3]=''.join(['四',a[i][3]])
            elif b%10==5:
                a[i][3]=''.join(['五',a[i][3]])
            elif b%10==6:
                a[i][3]=''.join(['六',a[i][3]])
            elif b%10==7:
                a[i][3]=''.join(['七',a[i][3]])
            elif b%10==8:
                a[i][3]=''.join(['八',a[i][3]])
            elif b%10==9:
                a[i][3]=''.join(['九',a[i][3]])
            b=int(b/10)
            if b==0:
                a[i][3]=''.join(['负',a[i][3]])
                break
            elif b!=0:
                if b%10!=0:
                    if j==0:
                        a[i][3]=''.join(['十',a[i][3]])
                    elif j==1:
                        a[i][3]=''.join(['百',a[i][3]])
                    elif j==2:
                        a[i][3]=''.join(['千',a[i][3]])
                    elif j==3:
                        a[i][3]=''.join(['万',a[i][3]])
                    elif j==4:
                        a[i][3]=''.join(['十',a[i][3]])
                    elif j==5:
                        a[i][3]=''.join(['百',a[i][3]])
                    elif j==6:
                        a[i][3]=''.join(['千',a[i][3]])
                    elif j==7:
                        a[i][3]=''.join(['亿',a[i][3]])
                    elif j==8:
                        a[i][3]=''.join(['十',a[i][3]])
                    elif j==9:
                        a[i][3]=''.join(['百',a[i][3]])
                        
def 定义变量(s):
    global i,bls
    if (s[0]=='整数') and (s[2]=='等于'):
        if bls==0:
            a[bls][0]=s[1]
            a[bls][1]=s[3]
            bls=bls+1
        else:
            for i in range(bls):
                if a[i][0]==s[1]:
                    a[i][1]=s[3]
                    break
            if (i+1)>=bls:
                if a[i][0]!=s[1]:
                    a[i+1][0]=s[1]
                    a[i+1][1]=s[3]
                    bls=bls+1
        i=0
        
def 加减法(s):
    global i
    if s[1]=='减少':
        for i in range(bls):
            if s[0]==a[i][0]:
                a[i][1]=a[i][1]-s[2]
        if i>=bls:
            print('没有这个变量')
        i=0
    elif s[1]=='增加':
        for i in range(bls):
            if s[0]==a[i][0]:
                a[i][1]=a[i][1]+s[2]
        if i>=bls:
            print('没有这个变量')
        i=0
        
def 打印(s):
    global i
    if s[0]=='看看':
        for i in range(bls):
            if s[1]==a[i][0]:
                数字转汉字(i)
                print(a[i][3])
        if i>=bls:
            print('没有这个变量')
            i=0
            
def 如果则(k,s):
    if s[k]=='看看':
        s[k+1]=s[k+1].strip('“').strip('”')
        print(s[k+1])
    elif s[k+1]=='增加' or s[k+1]=='减少':
        for j in range(3):
            b[j]=s[j+k]
        汉字转数字(b)
        加减法(b)
    elif s[k]=='无':
        k=k
        
def 使用(s):
    global bls
    global i
    i=0
    定义变量(s)
    加减法(s)
    打印(s)
    if s[0]=='如果':
        if s[2]=='大于':
            for i in range(bls):
                if s[1]==a[i][0]:
                    if a[i][1]>s[3]:
                        k=5
                        如果则(k,s)
                            
                    else:
                        k=8
                        如果则(k,s)
            if i>=bls:
                print('没有这个变量')
            i=0
        elif s[2]=='小于':
            for i in range(bls):
                if s[1]==a[i][0]:
                    if a[i][1]<s[3]:
                        k=5
                        如果则(k,s)
                    else:
                        k=8
                        如果则(k,s)
            if i>=bls:
                print('没有这个变量')
            i=0
        elif s[2]=='等于':
            for i in range(bls):
                if s[1]==a[i][0]:
                    if a[i][0]==s[3]:
                        k=5
                        如果则(k,s)
                    else:
                        k=8
                        如果则(k,s)
            if i>=bls:
                print('没有这个变量')
            i=0
            
a=[['',0,0,''],['',0,0,''],['',0,0,''],['',0,0,''],['',0,0,''],['',0,0,''],        # a[0,1,2,3]
   ['',0,0,''],['',0,0,''],['',0,0,''],['',0,0,''],['',0,0,''],['',0,0,''],        # a[0]是变量名,a[1]是输入的阿拉伯数字,
   ['',0,0,''],['',0,0,''],['',0,0,''],['',0,0,''],['',0,0,''],['',0,0,'']]        # a[2]是加减的数字,a[3]是输入的汉字数字
bls=0    #变量数
i=0
b=['','','']     #加减法用的,和加减法的输入语句格式相同,b[0]是变量名,b[1]是增加或减少,b[2]是汉字数字

def main():
    print('变量定义：整数 （变量名） 等于 （数字）')
    print('运算（加法）：（变量名） 增加 （数字')
    print('运算（减法）：（变量名） 减少 （数字）')
    print('输出：看看 （变量名） or 看看 “（字符串内容）')
    print('选择：如果 （判断语句） 则 （操作语句） 否则 （操作语句）')
    print('若否则后没有任何操作使用（无）来进行填充（参考样例2）。')
    print('回车结束')
    print('------------------------------------------------------------')
    while(1):
        s=输入()
        if s!=None:
            s=汉字转数字(s)
            使用(s)
        else:
            print('结束')
            break
            
main()
import pandas as pd  #for importing csv files and creating Dataframe.
l_up=[]              #for storing days with higher closing price then opening price.
l_down=[]            #for storing days with lower closing price then opening price.
l_year=[]            #for storing years.
per_up=[]            #To store percentage increase in price for a year.
per_down=[]          #To store percentage decrease in price for a year.
l_total=[]           #To store no. of days when stock mrket was open in a year.
for j in range(2003,2019):
    data = pd.read_csv(str(j)+".csv")       #importing CSV files
    l=[]
    for i in range(len(data.index)):        #comparing each day's opening and closing price
        if(data.loc[i,"Open"]>data.loc[i,"Close"]):
            v=-1
        else:
            v=1
        l.append(v)
    l_up.append(l.count(1))
    per_up.append((l.count(1)/len(l))*100) #Total=len(l)
    per_down.append((l.count(-1)/len(l))*100) #Total=len(l)
    l_total.append(len(l))
    l_down.append(l.count(-1))
    l_year.append(j)
df = pd.DataFrame(l_year,columns=["Year"])  #for creating dataframe
df.insert(1,"Up",l_up, True)
df.insert(2,"%age(up)",per_up, True)
df.insert(3,"Down",l_down, True)
df.insert(4,"%age(down)",per_down, True)
df.insert(5,"Total",l_total, True)


df.loc[16] = ['Total', sum(l_up), sum(l_up)/sum(l_total)*100, sum(l_down),sum(l_down)/sum(l_total)*100,sum(l_total)]

df     #for vizualizing the created dataframe

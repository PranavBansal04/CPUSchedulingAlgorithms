from tkinter import *



def rindex(mylist, myvalue):
    return len(mylist) - mylist[::-1].index(myvalue) - 1

root=Tk()
root.title("CPU SCHEDULING")

bgpic = PhotoImage(file="bgpic.png")
bglabel = Label(root,image=bgpic)
bglabel.place(anchor=CENTER,relx=0.5,rely=0.43)
def get_input():
    print(1)
def GanttOutput(GanttChart):
    firstLine = "|"
    aboveLine = "_"
    underLine = ""
    secondLine = "0"
    for i in range(0, len(GanttChart)):
        firstLine = firstLine + "P" + str(GanttChart[i]) + "|"
        if i<10:
            secondLine = secondLine + "   " + str((i+1))
        else:
            secondLine = secondLine +"  "+str((i+1))
    for i in range(1, len(firstLine)-6):
        aboveLine += "_"
    underLine += " ".join("‾")*(round(len(firstLine)*1.5))
    return aboveLine + "\n" + firstLine + "\n" + underLine + "\n" + secondLine

def f1():
    win1=Tk()
    win1.title("First Come First Serve")
    Label(win1,text="Enter Number of Processes : ",fg='black',bg='white',font=('Arial',15,'bold')).place(relx=0.37,rely=0.1,anchor=CENTER)
    e1=Entry(win1,bg='white',fg='black',font=('Arial',15),relief=SUNKEN)
    e1.place(height=25,width=40,relx=0.48,rely=0.1,anchor=CENTER)
    def get_f1():
        if(e1.get()=='' or e1.get()==" "):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Enter data!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        elif(e1.get().isnumeric()==False):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Please enter positive numeric data!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        elif(int(e1.get())<=0):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Please enter a value gerater than 0!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        else:
            def FCFS(n,ea):
                per=[]
                tt=sum(ea)
                for p in ea:
                    per.append(round((p/tt)*100))
                firstline=''.join("-")*100
                lastline=''.join("-")*100
                middleline="|"
                process=1
                for j in per:
                    for k in range((j//2)-1):
                        middleline+=" "
                    middleline+="P"+str(process)
                    process+=1
                    for k in range((j//2)-1):
                        middleline+=" "
                    middleline+="| "
                line4="\n\nWaiting Time : \n\n"
                sa=[]
                s=0
                p=1
                for i in ea:
                   line4+="P "+str(p)+":  "+str(s)+"\n"
                   sa.append(s)
                   s+=i
                   
                   p+=1   
                waitingtime=sum(sa)/n
                string = firstline+"\n"+middleline+"\n"+lastline+"\n"+line4
                return string,waitingtime

            Label(win1,text="Enter Burst Time(sec) : ",fg='black',bg='white',font=('Arial',12,'bold')).place(relx=0.39,rely=0.23,anchor=CENTER)
            times=[]
            n=int(e1.get())
            for i in range(n):
                Label(win1,text="Process "+str((i+1))+": ",fg='black',bg='white',font=('Arial',10,'bold')).place(relx=0.39,rely=0.25+(0.01*(i+1)*3),anchor=CENTER)
                ee=Entry(win1,bg='white',fg='black',relief=SUNKEN)
                ee.place(width=30,relx=0.43,rely=0.25+(0.01*(i+1)*3),anchor=CENTER)
                ry=0.25+(0.01*(i+1)*3)
                times.append(ee)

            def get_f11():
                ea1=[]
                for k in times:
                    ea1.append(k.get())
                flag=0
                for i in ea1:
                    if(i.isnumeric()==False):
                        flag+=1
                if("" in ea1 or " " in ea1 or flag>0):
                    temp=Tk()
                    temp.title('Prompt')
                    temp.configure(background='white')
                    Label(temp,text='Enter positive numeric data!',bg='white').pack()
                    Button(temp,text='OK',command=temp.destroy).pack()
                    temp.mainloop()
                else:
                    ea=[]
                    for i in ea1:
                        ea.append(int(i))
                    string,waitingtime = FCFS(n,ea)
                    small=0
                    big=0
                    for i in ea:
                        small+=i
                        big+=small
                    turnaround=big/len(ea)
                    gfig=Tk()
                    gfig.title("Gantt Chart")
                    Label(gfig,text="Gantt Chart : ",fg='black',bg='white',font=('Arial',15,'bold')).place(relx=0.1,rely=0.1,anchor=CENTER)
                    Label(gfig,text=string,bg='white',font=('Arial',12)).place(relx=0.25,rely=0.3,anchor=CENTER)
                    Label(gfig,text="Average Waiting Time = "+str(round(waitingtime,3)),bg='white',font=('Arial',13,"bold")).place(relx=0.12,rely=0.5,anchor=CENTER)
                    Label(gfig,text="Average TurnAround Time = "+str(round(turnaround,3)),bg='white',font=('Arial',13,"bold")).place(relx=0.12,rely=0.54,anchor=CENTER)
                    Button(gfig,text="Close",bg="white",command=gfig.destroy).place(relx=0.2,rely=0.7,anchor=CENTER)
                    gfig.geometry('1500x1500')
                    gfig.configure(background='white')
                    gfig.mainloop()

            Button(win1,text='Enter',font=('verdana',11,),fg='black',bg='white',command=get_f11).place(width=45,relx=0.43,rely=ry+0.05,anchor=CENTER)
            
    Button(win1,text='Enter',font=('verdana',11,),fg='black',bg='white',command=get_f1).place(width=45,relx=0.48,rely=0.15,anchor=CENTER)
    
    
    Button(win1,text='Close',font=('verdana',11,'bold'),fg='red',bg='white',command=win1.destroy).place(relx=0.46,rely=0.77,anchor=CENTER)
    win1.geometry('1500x1500')
    win1.configure(background='white')
    win1.mainloop()


def f2():
    win1=Tk()
    win1.title("Shortest Job First(Non Preemptive)")
    Label(win1,text="Enter Number of Processes : ",fg='black',bg='white',font=('Arial',15,'bold')).place(relx=0.37,rely=0.1,anchor=CENTER)
    e1=Entry(win1,bg='white',fg='black',font=('Arial',15),relief=SUNKEN)
    e1.place(height=25,width=40,relx=0.48,rely=0.1,anchor=CENTER)
    def get_f2():
        if(e1.get()=='' or e1.get()==" "):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Enter data!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        elif(e1.get().isnumeric()==False):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Please enter positive numeric data!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        elif(int(e1.get())<=0):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Please enter a value gerater than 0!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        else:
            def FCFS(NumOfProcesses, BurstTimeList):
                waitingTime = 0
                GanttChart = []
                for i in range(0, NumOfProcesses):
                    for j in range(0, BurstTimeList[i][1]):
                        GanttChart.append(BurstTimeList[i][0])
                    waitingTime += BurstTimeList[i][1]*(NumOfProcesses-i-1)
                waitingTime /= NumOfProcesses
                return GanttChart, waitingTime
            def SJFNonPreemptive(NumOfProcesses, BurstTimeList):
                swapList = []
                for i in range(0, NumOfProcesses):
                    c = i
                    for j in range(i+1, NumOfProcesses):
                        if BurstTimeList[j][1]<BurstTimeList[c][1]:
                            c = j
                    if c != i:
                        swapList         = BurstTimeList[c]
                        BurstTimeList[c] = BurstTimeList[i]
                        BurstTimeList[i] = swapList
                return FCFS(NumOfProcesses, BurstTimeList)

            Label(win1,text="Enter Burst Time(sec) : ",fg='black',bg='white',font=('Arial',12,'bold')).place(relx=0.39,rely=0.23,anchor=CENTER)
            times=[]
            n=int(e1.get())
            for i in range(n):
                Label(win1,text="Process "+str((i+1))+": ",fg='black',bg='white',font=('Arial',10,'bold')).place(relx=0.39,rely=0.25+(0.01*(i+1)*3),anchor=CENTER)
                ee=Entry(win1,bg='white',fg='black',relief=SUNKEN)
                ee.place(width=30,relx=0.43,rely=0.25+(0.01*(i+1)*3),anchor=CENTER)
                ry=0.25+(0.01*(i+1)*3)
                times.append(ee)

            def get_f22():
                ea1=[]
                for k in times:
                    ea1.append(k.get())
                flag=0
                for i in ea1:
                    if(i.isnumeric()==False):
                        flag+=1
                if("" in ea1 or " " in ea1 or flag>0):
                    temp=Tk()
                    temp.title('Prompt')
                    temp.configure(background='white')
                    Label(temp,text='Enter positive numeric data!',bg='white').pack()
                    Button(temp,text='OK',command=temp.destroy).pack()
                    temp.mainloop()
                else:
                    ea=[]
                    c=1
                    for k in times:
                        tl=[]
                        tl.append(c)
                        c+=1
                        tl.append(int(k.get()))
                        ea.append(tl)
                    

                    GanttChart, waitingTime = SJFNonPreemptive(n, ea)
                    big=0
                    small=0
                    for i in range(n):
                        small+=ea[i][1]
                        big+=small
                    turnaround=big/len(ea)
                    gfig=Tk()
                    gfig.title("Gantt Chart")
                    Label(gfig,text="Gantt Chart : ",fg='black',bg='white',font=('Arial',15,'bold')).place(relx=0.1,rely=0.1,anchor=CENTER)
                    Label(gfig,text=GanttOutput(GanttChart),bg='white',font=('Arial',12)).place(relx=0.25,rely=0.3,anchor=CENTER)
                    Label(gfig,text="Average Waiting Time = "+str(round(waitingTime,3)),bg='white',font=('Arial',13,"bold")).place(relx=0.12,rely=0.5,anchor=CENTER)
                    Label(gfig,text="Average TurnAround Time = "+str(round(turnaround,3)),bg='white',font=('Arial',13,"bold")).place(relx=0.12,rely=0.54,anchor=CENTER)
                    Button(gfig,text="Close",bg="white",command=gfig.destroy).place(relx=0.2,rely=0.7,anchor=CENTER)
                    gfig.geometry('1500x1500')
                    gfig.configure(background='white')
                    gfig.mainloop()

            Button(win1,text='Enter',font=('verdana',11,),fg='black',bg='white',command=get_f22).place(width=45,relx=0.43,rely=ry+0.05,anchor=CENTER)
            
    Button(win1,text='Enter',font=('verdana',11,),fg='black',bg='white',command=get_f2).place(width=45,relx=0.48,rely=0.15,anchor=CENTER)
    
    
    Button(win1,text='Close',font=('verdana',11,'bold'),fg='red',bg='white',command=win1.destroy).place(relx=0.46,rely=0.77,anchor=CENTER)
    win1.geometry('1500x1500')
    win1.configure(background='white')
    win1.mainloop()


def f3():
    win1=Tk()
    win1.title("Shortest Job First(Preemptive)")
    Label(win1,text="Enter Number of Processes : ",fg='black',bg='white',font=('Arial',15,'bold')).place(relx=0.37,rely=0.1,anchor=CENTER)
    e1=Entry(win1,bg='white',fg='black',font=('Arial',15),relief=SUNKEN)
    e1.place(height=25,width=40,relx=0.48,rely=0.1,anchor=CENTER)
    def get_f3():
        if(e1.get()=='' or e1.get()==" "):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Enter data!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        elif(e1.get().isnumeric()==False):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Please enter positive numeric data!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        elif(int(e1.get())<=0):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Please enter a value gerater than 0!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        else:
            def SJFPreemptive(NumOfProcesses, BurstTimeList):
                ArrivalTime = []
                ArrivalStatus = []
                waitingTime = 0
                totalTime = 0
                GanttChart = []
                for i in range(0, NumOfProcesses):
                    ArrivalTime.append(BurstTimeList[i][2])
                    ArrivalStatus.append(False)
                    waitingTime -= (BurstTimeList[i][1]+BurstTimeList[i][2])
                    totalTime += BurstTimeList[i][1]
                smallestIndex = 0
                smallestValue = totalTime
                for i in range(0, totalTime):
                    smallestValue = totalTime
                    for j in range(0, NumOfProcesses):
                        if i == ArrivalTime[j]:
                            ArrivalStatus[j] = True
                    for j in range(0, NumOfProcesses):
                        if ArrivalStatus[j] and BurstTimeList[j][1] < smallestValue and BurstTimeList[j][1] != 0:
                            smallestValue = BurstTimeList[j][1]
                            smallestIndex = j
                    GanttChart.append(smallestIndex+1)
                    BurstTimeList[smallestIndex][1] -= 1
                    if BurstTimeList[smallestIndex][1] == 0:
                        waitingTime += (i+1)
                waitingTime /= NumOfProcesses
                
                return GanttChart, waitingTime

            Label(win1,text="Burst Time(sec) ",fg='black',bg='white',font=('Arial',10,'bold')).place(relx=0.39,rely=0.23,anchor=CENTER)
            Label(win1,text="Arrival Time(sec) ",fg='black',bg='white',font=('Arial',10,'bold')).place(relx=0.48,rely=0.23,anchor=CENTER)
            times=[]
            atime=[]
            n=int(e1.get())
            for i in range(n):
                Label(win1,text="Process "+str((i+1))+": ",fg='black',bg='white',font=('Arial',10,'bold')).place(relx=0.34,rely=0.25+(0.01*(i+1)*3),anchor=CENTER)
                ee=Entry(win1,bg='white',fg='black',relief=SUNKEN)
                ee.place(width=30,relx=0.40,rely=0.25+(0.01*(i+1)*3),anchor=CENTER)
                ee2=Entry(win1,bg='white',fg='black',relief=SUNKEN)
                ee2.place(width=30,relx=0.48,rely=0.25+(0.01*(i+1)*3),anchor=CENTER)
                ry=0.25+(0.01*(i+1)*3)
                times.append(ee)
                atime.append(ee2)

            def get_f33():
                ea1=[]
                ea2=[]
                for k in times:
                    ea1.append(k.get())
                for k in atime:
                    ea2.append(k.get())
                flag1=0
                flag2=0
                for i in ea1:
                    if(i.isnumeric()==False):
                        flag1+=1
                for i in ea2:
                    if(i.isnumeric()==False):
                        flag2+=1
                if("" in ea1 or " " in ea1 or flag1>0 or flag2>0):
                    temp=Tk()
                    temp.title('Prompt')
                    temp.configure(background='white')
                    Label(temp,text='Enter positive numeric data!',bg='white').pack()
                    Button(temp,text='OK',command=temp.destroy).pack()
                    temp.mainloop()
                else: 
                    ea=[]
                    c=1
                    at=[]
                    for k in range(len(times)):
                        tl=[]
                        tl.append(c)
                        c+=1
                        tl.append(int(times[k].get()))
                        tl.append(int(atime[k].get()))
                        at.append(int(atime[k].get()))
                        ea.append(tl)
                    

                    GanttChart, waitingTime = SJFPreemptive(n, ea)
                    ct=[]
                    for q in range(1,n+1):
                        ct.append(rindex(GanttChart,q)+1)
                    turna=[]
                    for i in range(len(at)):
                        turna.append(ct[i]-at[i])
                    turnaround=sum(turna)/len(ea)
                    gfig=Tk()
                    gfig.title("Gantt Chart")
                    Label(gfig,text="Gantt Chart : ",fg='black',bg='white',font=('Arial',15,'bold')).place(relx=0.1,rely=0.1,anchor=CENTER)
                    Label(gfig,text=GanttOutput(GanttChart),bg='white',font=('Arial',12)).place(relx=0.25,rely=0.3,anchor=CENTER)
                    Label(gfig,text="Average Waiting Time = "+str(round(waitingTime,3)),bg='white',font=('Arial',13,"bold")).place(relx=0.12,rely=0.5,anchor=CENTER)
                    Label(gfig,text="Average TurnAround Time = "+str(round(turnaround,3)),bg='white',font=('Arial',13,"bold")).place(relx=0.12,rely=0.54,anchor=CENTER)
                    Button(gfig,text="Close",bg="white",command=gfig.destroy).place(relx=0.2,rely=0.7,anchor=CENTER)
                    gfig.geometry('1500x1500')
                    gfig.configure(background='white')
                    gfig.mainloop()

            Button(win1,text='Enter',font=('verdana',11,),fg='black',bg='white',command=get_f33).place(width=45,relx=0.43,rely=ry+0.08,anchor=CENTER)
            
    Button(win1,text='Enter',font=('verdana',11,),fg='black',bg='white',command=get_f3).place(width=45,relx=0.48,rely=0.15,anchor=CENTER)
    
    
    Button(win1,text='Close',font=('verdana',11,'bold'),fg='red',bg='white',command=win1.destroy).place(relx=0.46,rely=0.77,anchor=CENTER)
    win1.geometry('1500x1500')
    win1.configure(background='white')
    win1.mainloop()

def f4():
    win1=Tk()
    win1.title("Priority(Non Preemptive)")
    Label(win1,text="Enter Number of Processes : ",fg='black',bg='white',font=('Arial',15,'bold')).place(relx=0.37,rely=0.1,anchor=CENTER)
    e1=Entry(win1,bg='white',fg='black',font=('Arial',15),relief=SUNKEN)
    e1.place(height=25,width=40,relx=0.48,rely=0.1,anchor=CENTER)
    def get_f4():
        if(e1.get()=='' or e1.get()==" "):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Enter data!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        elif(e1.get().isnumeric()==False):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Please enter positive numeric data!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        elif(int(e1.get())<=0):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Please enter a value gerater than 0!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        else:
            def FCFS(NumOfProcesses, BurstTimeList):
                waitingTime = 0
                GanttChart = []
                for i in range(0, NumOfProcesses):
                    for j in range(0, BurstTimeList[i][1]):
                        GanttChart.append(BurstTimeList[i][0])
                    waitingTime += BurstTimeList[i][1]*(NumOfProcesses-i-1)
                waitingTime /= NumOfProcesses
                return GanttChart, waitingTime
            def PriorityNonPreemptive(NumOfProcesses, BurstTimeList):
                swapList = []
                for i in range(0, NumOfProcesses):
                    c = i
                    for j in range(i+1, NumOfProcesses):
                        if BurstTimeList[j][2]<BurstTimeList[c][2]:
                            c = j
                    if c != i:
                        swapList         = BurstTimeList[c]
                        BurstTimeList[c] = BurstTimeList[i]
                        BurstTimeList[i] = swapList
                return FCFS(NumOfProcesses, BurstTimeList)

            Label(win1,text="Burst Time(sec) ",fg='black',bg='white',font=('Arial',10,'bold')).place(relx=0.39,rely=0.23,anchor=CENTER)
            Label(win1,text="Priority",fg='black',bg='white',font=('Arial',10,'bold')).place(relx=0.48,rely=0.23,anchor=CENTER)
            times=[]
            priority=[]
            n=int(e1.get())
            for i in range(n):
                Label(win1,text="Process "+str((i+1))+": ",fg='black',bg='white',font=('Arial',10,'bold')).place(relx=0.34,rely=0.25+(0.01*(i+1)*3),anchor=CENTER)
                ee=Entry(win1,bg='white',fg='black',relief=SUNKEN)
                ee.place(width=30,relx=0.40,rely=0.25+(0.01*(i+1)*3),anchor=CENTER)
                ee2=Entry(win1,bg='white',fg='black',relief=SUNKEN)
                ee2.place(width=30,relx=0.48,rely=0.25+(0.01*(i+1)*3),anchor=CENTER)
                ry=0.25+(0.01*(i+1)*3)
                times.append(ee)
                priority.append(ee2)

            def get_f44():
                ea1=[]
                ea2=[]
                for k in times:
                    ea1.append(k.get())
                for k in priority:
                    ea2.append(k.get())
                flag1=0
                flag2=0
                for i in ea1:
                    if(i.isnumeric()==False):
                        flag1+=1
                for i in ea2:
                    if(i.isnumeric()==False):
                        flag2+=1
                if("" in ea1 or " " in ea1 or "" in ea2 or " " in ea2 or flag1>0 or flag2>0):
                    temp=Tk()
                    temp.title('Prompt')
                    temp.configure(background='white')
                    Label(temp,text='Enter positive numeric data!',bg='white').pack()
                    Button(temp,text='OK',command=temp.destroy).pack()
                    temp.mainloop()
                else: 
                    ea=[]
                    c=1
                    at=[]
                    for k in range(len(times)):
                        tl=[]
                        tl.append(c)
                        c+=1
                        tl.append(int(times[k].get()))
                        tl.append(int(priority[k].get()))
                        at.append(int(priority[k].get()))
                        ea.append(tl)
                    

                    GanttChart, waitingTime = PriorityNonPreemptive(n, ea)
                    ct=[]
                    for q in range(1,n+1):
                        ct.append(rindex(GanttChart,q)+1)
                    turna=[]
                    turnaround=sum(ct)/len(ea)
                    gfig=Tk()
                    gfig.title("Gantt Chart")
                    Label(gfig,text="Gantt Chart : ",fg='black',bg='white',font=('Arial',15,'bold')).place(relx=0.1,rely=0.1,anchor=CENTER)
                    Label(gfig,text=GanttOutput(GanttChart),bg='white',font=('Arial',12)).place(relx=0.25,rely=0.3,anchor=CENTER)
                    Label(gfig,text="Average Waiting Time = "+str(round(waitingTime,3)),bg='white',font=('Arial',13,"bold")).place(relx=0.12,rely=0.5,anchor=CENTER)
                    Label(gfig,text="Average TurnAround Time = "+str(round(turnaround,3)),bg='white',font=('Arial',13,"bold")).place(relx=0.12,rely=0.54,anchor=CENTER)
                    Button(gfig,text="Close",bg="white",command=gfig.destroy).place(relx=0.2,rely=0.7,anchor=CENTER)
                    gfig.geometry('1500x1500')
                    gfig.configure(background='white')
                    gfig.mainloop()

            Button(win1,text='Enter',font=('verdana',11,),fg='black',bg='white',command=get_f44).place(width=45,relx=0.43,rely=ry+0.08,anchor=CENTER)
            
    Button(win1,text='Enter',font=('verdana',11,),fg='black',bg='white',command=get_f4).place(width=45,relx=0.48,rely=0.15,anchor=CENTER)
    
    
    Button(win1,text='Close',font=('verdana',11,'bold'),fg='red',bg='white',command=win1.destroy).place(relx=0.46,rely=0.77,anchor=CENTER)
    win1.geometry('1500x1500')
    win1.configure(background='white')
    win1.mainloop()


def f5():
    win1=Tk()
    win1.title("Priority Preemptive")
    Label(win1,text="Enter Number of Processes : ",fg='black',bg='white',font=('Arial',15,'bold')).place(relx=0.37,rely=0.1,anchor=CENTER)
    e1=Entry(win1,bg='white',fg='black',font=('Arial',15),relief=SUNKEN)
    e1.place(height=25,width=40,relx=0.48,rely=0.1,anchor=CENTER)
    def get_f5():
        if(e1.get()=='' or e1.get()==" "):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Enter data!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        elif(e1.get().isnumeric()==False):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Please enter positive numeric data!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        elif(int(e1.get())<=0):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Please enter a value gerater than 0!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        else:
            def PriorityPreemptive(NumOfProcesses, BurstTimeList):
                ArrivalTime = []
                ArrivalStatus = []
                waitingTime = 0
                totalTime = 0
                GanttChart = []
                for i in range(0, NumOfProcesses):
                    ArrivalTime.append(BurstTimeList[i][2])
                    ArrivalStatus.append(False)
                    waitingTime -= (BurstTimeList[i][1]+BurstTimeList[i][2])
                    totalTime += BurstTimeList[i][1]
                smallestIndex = 0
                smallestValue = 30
                for i in range(0, totalTime):
                    smallestValue = totalTime
                    for j in range(0, NumOfProcesses):
                        if i == ArrivalTime[j]:
                            ArrivalStatus[j] = True
                    for j in range(0, NumOfProcesses):
                        if ArrivalStatus[j] and BurstTimeList[j][3] < smallestValue and BurstTimeList[j][1] != 0:
                            smallestValue = BurstTimeList[j][3]
                            smallestIndex = j
                    GanttChart.append(smallestIndex+1)
                    BurstTimeList[smallestIndex][1] -= 1
                    if BurstTimeList[smallestIndex][1] == 0:
                        waitingTime += (i+1)
                waitingTime /= NumOfProcesses
                return GanttChart, waitingTime

            Label(win1,text="Burst Time(sec) ",fg='black',bg='white',font=('Arial',10,'bold')).place(relx=0.39,rely=0.23,anchor=CENTER)
            Label(win1,text="Arrival Time(sec) ",fg='black',bg='white',font=('Arial',10,'bold')).place(relx=0.48,rely=0.23,anchor=CENTER)
            Label(win1,text="Priority",fg='black',bg='white',font=('Arial',10,'bold')).place(relx=0.56,rely=0.23,anchor=CENTER)
            times=[]
            atime=[]
            priority=[]
            n=int(e1.get())
            for i in range(n):
                Label(win1,text="Process "+str((i+1))+": ",fg='black',bg='white',font=('Arial',10,'bold')).place(relx=0.34,rely=0.25+(0.01*(i+1)*3),anchor=CENTER)
                ee=Entry(win1,bg='white',fg='black',relief=SUNKEN)
                ee.place(width=30,relx=0.40,rely=0.25+(0.01*(i+1)*3),anchor=CENTER)
                ee2=Entry(win1,bg='white',fg='black',relief=SUNKEN)
                ee2.place(width=30,relx=0.48,rely=0.25+(0.01*(i+1)*3),anchor=CENTER)
                ee3=Entry(win1,bg='white',fg='black',relief=SUNKEN)
                ee3.place(width=30,relx=0.56,rely=0.25+(0.01*(i+1)*3),anchor=CENTER)
                ry=0.25+(0.01*(i+1)*3)
                times.append(ee)
                atime.append(ee2)
                priority.append(ee3)

            def get_f55():
                ea1=[]
                ea2=[]
                ea3=[]
                for k in times:
                    ea1.append(k.get())
                for k in atime:
                    ea2.append(k.get())
                for k in priority:
                    ea3.append(k.get())
                flag1=0
                flag2=0
                flag3=0
                for i in ea1:
                    if(i.isnumeric()==False):
                        flag1+=1
                for i in ea2:
                    if(i.isnumeric()==False):
                        flag2+=1
                for i in ea3:
                    if(i.isnumeric()==False):
                        flag3+=1
                if("" in ea1 or " " in ea1 or "" in ea2 or " " in ea2 or "" in ea3 or " " in ea3 or flag1>0 or flag2>0 or flag3>0):
                    temp=Tk()
                    temp.title('Prompt')
                    temp.configure(background='white')
                    Label(temp,text='Enter positive numeric data!',bg='white').pack()
                    Button(temp,text='OK',command=temp.destroy).pack()
                    temp.mainloop()
                else: 
                    ea=[]
                    c=1
                    at=[]
                    for k in range(len(times)):
                        tl=[]
                        tl.append(c)
                        c+=1
                        tl.append(int(times[k].get()))
                        tl.append(int(atime[k].get()))
                        tl.append(int(priority[k].get()))
                        at.append(int(atime[k].get()))
                        ea.append(tl)
                    

                    GanttChart, waitingTime = PriorityPreemptive(n, ea)
                    ct=[]
                    for q in range(1,n+1):
                        ct.append(rindex(GanttChart,q)+1)
                    turna=[]
                    for i in range(len(at)):
                        turna.append(ct[i]-at[i])
                    turnaround=sum(turna)/len(ea)
                    gfig=Tk()
                    gfig.title("Gantt Chart")
                    Label(gfig,text="Gantt Chart : ",fg='black',bg='white',font=('Arial',15,'bold')).place(relx=0.1,rely=0.1,anchor=CENTER)
                    Label(gfig,text=GanttOutput(GanttChart),bg='white',font=('Arial',12)).place(relx=0.25,rely=0.3,anchor=CENTER)
                    Label(gfig,text="Average Waiting Time = "+str(round(waitingTime,3)),bg='white',font=('Arial',13,"bold")).place(relx=0.12,rely=0.5,anchor=CENTER)
                    Label(gfig,text="Average TurnAround Time = "+str(round(turnaround,3)),bg='white',font=('Arial',13,"bold")).place(relx=0.12,rely=0.54,anchor=CENTER)
                    Button(gfig,text="Close",bg="white",command=gfig.destroy).place(relx=0.2,rely=0.7,anchor=CENTER)
                    gfig.geometry('1500x1500')
                    gfig.configure(background='white')
                    gfig.mainloop()

            Button(win1,text='Enter',font=('verdana',11,),fg='black',bg='white',command=get_f55).place(width=45,relx=0.43,rely=ry+0.08,anchor=CENTER)
            
    Button(win1,text='Enter',font=('verdana',11,),fg='black',bg='white',command=get_f5).place(width=45,relx=0.48,rely=0.15,anchor=CENTER)
    
    
    Button(win1,text='Close',font=('verdana',11,'bold'),fg='red',bg='white',command=win1.destroy).place(relx=0.46,rely=0.77,anchor=CENTER)
    win1.geometry('1500x1500')
    win1.configure(background='white')
    win1.mainloop()


def f6():
    win1=Tk()
    win1.title("ROUND ROBIN")
    Label(win1,text="Enter Number of Processes : ",fg='black',bg='white',font=('Arial',15,'bold')).place(relx=0.37,rely=0.1,anchor=CENTER)
    e1=Entry(win1,bg='white',fg='black',font=('Arial',15),relief=SUNKEN)
    e1.place(height=25,width=40,relx=0.48,rely=0.1,anchor=CENTER)

    Label(win1,text="Time Quantum(sec) : ",fg='black',bg='white',font=('Arial',12,'bold')).place(relx=0.58,rely=0.1,anchor=CENTER)
    e4=Entry(win1,bg='white',fg='black',relief=SUNKEN)
    e4.place(width=30,relx=0.66,rely=0.1,anchor=CENTER)
    def get_f6():
        if(e1.get()=='' or e1.get()==" "):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Enter data!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        elif(e1.get().isnumeric()==False):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Please enter positive numeric data!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        elif(int(e1.get())<=0):
            temp=Tk()
            temp.title('Prompt')
            temp.configure(background='white')
            Label(temp,text='Please enter a value gerater than 0!',bg='white').pack()
            Button(temp,text='OK',command=temp.destroy).pack()
            temp.mainloop()
        else:
            def RoundRobin(NumOfProcesses, BurstTimeList, TimeQuantum):
                waitingTime = 0
                GanttChart = []
                myLen = 0
                for i in range(0, NumOfProcesses):
                    waitingTime -= BurstTimeList[i][1]
                i = 0
                NumOfZeroes = 0
                while True:
                    if(BurstTimeList[i][1]==0):
                        i = (i+1)%NumOfProcesses
                        continue
                    if BurstTimeList[i][1]>TimeQuantum:
                        BurstTimeList[i][1] -= TimeQuantum
                        myLen += TimeQuantum
                        for j in range(0, TimeQuantum):
                            GanttChart.append(BurstTimeList[i][0])
                    else:
                        myLen += BurstTimeList[i][1]
                        for j in range(0, BurstTimeList[i][1]):
                            GanttChart.append(BurstTimeList[i][0])
                        BurstTimeList[i][1] = 0
                        NumOfZeroes += 1
                        waitingTime += myLen
                    if NumOfZeroes == NumOfProcesses:
                        break
                    i = (i+1)%NumOfProcesses
                waitingTime /= NumOfProcesses
                return GanttChart, waitingTime

            Label(win1,text="Burst Time(sec) ",fg='black',bg='white',font=('Arial',10,'bold')).place(relx=0.39,rely=0.23,anchor=CENTER)
            times=[]
            n=int(e1.get())
            for i in range(n):
                Label(win1,text="Process "+str((i+1))+": ",fg='black',bg='white',font=('Arial',10,'bold')).place(relx=0.34,rely=0.25+(0.01*(i+1)*3),anchor=CENTER)
                ee=Entry(win1,bg='white',fg='black',relief=SUNKEN)
                ee.place(width=30,relx=0.40,rely=0.25+(0.01*(i+1)*3),anchor=CENTER)
                ry=0.25+(0.01*(i+1)*3)
                times.append(ee)
                

            def get_f66():
                ea1=[]                
                for k in times:
                    ea1.append(k.get())   
                flag1=0
                for i in ea1:
                    if(i.isnumeric()==False):
                        flag1+=1
                
                if("" in ea1 or " " in ea1 or flag1>0 or e4.get()==" " or e4.get==""):
                    temp=Tk()
                    temp.title('Prompt')
                    temp.configure(background='white')
                    Label(temp,text='Enter positive numeric data!',bg='white').pack()
                    Button(temp,text='OK',command=temp.destroy).pack()
                    temp.mainloop()
                else: 
                    ea=[]
                    c=1
                    at=[]
                    for k in range(len(times)):
                        tl=[]
                        tl.append(c)
                        c+=1
                        tl.append(int(times[k].get()))
                        ea.append(tl)
                    
                    time_quantum=int(e4.get())
                    GanttChart, waitingTime = RoundRobin(n, ea,time_quantum)
                    ct=[]
                    for q in range(1,n+1):
                        ct.append(rindex(GanttChart,q)+1)
                    turna=[]
                    turnaround=sum(ct)/len(ea)
                    gfig=Tk()
                    gfig.title("Gantt Chart")
                    Label(gfig,text="Gantt Chart : ",fg='black',bg='white',font=('Arial',15,'bold')).place(relx=0.1,rely=0.1,anchor=CENTER)
                    Label(gfig,text=GanttOutput(GanttChart),bg='white',font=('Arial',12)).place(relx=0.25,rely=0.3,anchor=CENTER)
                    Label(gfig,text="Average Waiting Time = "+str(round(waitingTime,3)),bg='white',font=('Arial',13,"bold")).place(relx=0.12,rely=0.5,anchor=CENTER)
                    Label(gfig,text="Average TurnAround Time = "+str(round(turnaround,3)),bg='white',font=('Arial',13,"bold")).place(relx=0.12,rely=0.54,anchor=CENTER)
                    Button(gfig,text="Close",bg="white",command=gfig.destroy).place(relx=0.2,rely=0.7,anchor=CENTER)
                    gfig.geometry('1500x1500')
                    gfig.configure(background='white')
                    gfig.mainloop()

         
            
            
            Button(win1,text='Enter',font=('verdana',11,),fg='black',bg='white',command=get_f66).place(width=45,relx=0.43,rely=ry+0.08,anchor=CENTER)
       
    Button(win1,text='Enter',font=('verdana',11,),fg='black',bg='white',command=get_f6).place(width=45,relx=0.48,rely=0.15,anchor=CENTER)
    
    
    Button(win1,text='Close',font=('verdana',11,'bold'),fg='red',bg='white',command=win1.destroy).place(relx=0.46,rely=0.77,anchor=CENTER)
    win1.geometry('1500x1500')
    win1.configure(background='white')
    win1.mainloop()
    

    
b1=Button(root,text='FCFS',font=('MS Sans serif',14,'bold'),fg='navy blue',bg='white',command=f1,relief=RAISED).place(width=260,relx=0.46,rely=0.25,anchor=CENTER)
b2=Button(root,text='SJF (Non Preemptive)',font=('MS Sans serif',14,'bold'),fg='navy blue',bg='white',command=f2,relief=RAISED).place(width=260,relx=0.46,rely=0.31,anchor=CENTER)
b3=Button(root,text='SJF (Preemptive)',font=('MS Sans serif',14,'bold'),fg='navy blue',bg='white',command=f3,relief=RAISED).place(width=260,relx=0.46,rely=0.37,anchor=CENTER)
b4=Button(root,text='Priority (Non Preemptive)',font=('MS Sans serif',14,'bold'),fg='navy blue',bg='white',command=f4,relief=RAISED).place(width=260,relx=0.46,rely=0.43,anchor=CENTER)
b5=Button(root,text='Priority (Preemptive)',font=('MS Sans serif',14,'bold'),fg='navy blue',bg='white',command=f5,relief=RAISED).place(width=260,relx=0.46,rely=0.49,anchor=CENTER)
b6=Button(root,text='Round Robin',font=('MS Sans serif',14,'bold'),fg='navy blue',bg='white',command=f6,relief=RAISED).place(width=260,relx=0.46,rely=0.55,anchor=CENTER)
b7=Button(root,text='Multilevel Queue',font=('MS Sans serif',14,'bold'),fg='navy blue',bg='white',command=get_input,relief=RAISED).place(width=260,relx=0.46,rely=0.61,anchor=CENTER)
b8=Button(root,text='Multilevel Feedback Queue',font=('MS Sans serif',14,'bold'),fg='navy blue',bg='white',command=get_input,relief=RAISED).place(width=260,relx=0.46,rely=0.67,anchor=CENTER)







def quitroot():
    qroot=Tk()
    qroot.configure(background='white')
    Label(qroot,text='Are You Sure You Want To Exit ?',fg='red',bg='white',font=('Times',12,'bold')).pack(side=TOP)
    Button(qroot,text='NO',fg='blue',bg='white',command=qroot.destroy).pack(side=BOTTOM)
    def destroyall():
        qroot.destroy()
        root.destroy()
    Button(qroot,text='YES',fg='blue',bg='white',command=destroyall).pack(side=BOTTOM)
    qroot.mainloop()

b=Button(root,text='Exit',font=('verdana',11,'bold'),fg='red',bg='white',command=quitroot).place(relx=0.46,rely=0.77,anchor=CENTER)
root.geometry('1500x1500')
root.configure(background='white')
root.mainloop()


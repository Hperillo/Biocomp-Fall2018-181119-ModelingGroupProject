#Lotka-Volterra Model
import pandas
import scipy
import scipy.integrate as spint
from plotnine import *
def lotkaSim(y,t0,b,H,a,P,e,s):
    H=y[0]
    P=y[1]
    dHdt=((b*H)-(a*P*H))
    dPdt=((e*a*P*H)-(s*P))
    return [dHdt,dPdt]
# Model Simulation- Ideal Parameters
times=range(0,100)
y0=[25,5]
params=(0.5,25,0.02,5,0.1,0.2)
sim=spint.odeint(func=lotkaSim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"t":times,"Herbivore":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Herbivore"))+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

#Changing b parameter simulation
factor=[0.25,.333,.5,1,2,3,4]
y=[]
for f in factor:
    b=.5
    y=[b*f]
    print "b=",y
    for i in y:
        times=range(0,100)
        y0=[25,5]
        params=(i,25,0.02,5,0.1,0.2)
        sim=spint.odeint(func=lotkaSim,y0=y0,t=times,args=params)
        simDF=pandas.DataFrame({"t":times,"Herbivore":sim[:,0],"Predator":sim[:,1]})
        a=ggplot(simDF,aes(x="t",y="Herbivore"))+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()
        print(a)

#Changing a parameter simulation 
factor=[0.25,.333,.5,1,2,3,4]
y=[]
for f in factor:
    a=.02
    y=[a*f]
    print "a=",y
    for i in y:
        times=range(0,100)
        y0=[25,5]
        params=(.5,25,i,5,0.1,0.2)
        sim=spint.odeint(func=lotkaSim,y0=y0,t=times,args=params)
        simDF=pandas.DataFrame({"t":times,"Herbivore":sim[:,0],"Predator":sim[:,1]})
        a=ggplot(simDF,aes(x="t",y="Herbivore"))+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()
        print(a)
        
#Changing e parameter simulation 
factor=[0.25,.333,.5,1,2,3,4]
y=[]
for f in factor:
    e=.1
    y=[e*f]
    print "e=",y
    for i in y:
        times=range(0,100)
        y0=[25,5]
        params=(.5,25,.02,5,i,0.2)
        sim=spint.odeint(func=lotkaSim,y0=y0,t=times,args=params)
        simDF=pandas.DataFrame({"t":times,"Herbivore":sim[:,0],"Predator":sim[:,1]})
        a=ggplot(simDF,aes(x="t",y="Herbivore"))+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()
        print(a)

#Changing s parameter simulation 
factor=[0.25,.333,.5,1,2,3,4]
y=[]
for f in factor:
    s=.2
    y=[s*f]
    print "e=",y
    for i in y:
        times=range(0,100)
        y0=[25,5]
        params=(.5,25,0.02,5,0.1,i)
        sim=spint.odeint(func=lotkaSim,y0=y0,t=times,args=params)
        simDF=pandas.DataFrame({"t":times,"Herbivore":sim[:,0],"Predator":sim[:,1]})
        a=ggplot(simDF,aes(x="t",y="Herbivore"))+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()
        print(a)





















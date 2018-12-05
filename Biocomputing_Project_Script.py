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

#Rosenzweig-MacArthur Model 
#Install packages
import pandas as pd
import numpy as np
import scipy
from scipy.optimize import minimize
import scipy.integrate as spint
from scipy.stats import norm
from scipy.stats import chi2
from scipy import stats
from plotnine import *

#Creating model and parameters
def rosenmacSim(y,t,b,e,s,w,d,a):
# "unpack" lists containing state variables (y)
    H=y[0]
    P=y[1]
#Calculate change in state variables with time, give parameter values and current value of state variables
    dHdt=(b*H*(1-(a*H)))-(w*P*(H/(d+H)))
    dPdt=(e*w*P*(H/(d+H)))-(s*P)
#Return list containing change in state variables with time
    return [dHdt, dPdt]

#Define parameters, initial values for state variables, and time steps
params=(0.8,0.07,0.2,5,400,0.001)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Changing b parameter simulation
factor=[0.25,.333,.5,1,2,3,4]
y=[]
for f in factor:
    b=.8
    y=[b*f]
    print "b=",y
    for i in y:
        params=(i,0.07,0.2,5,400,0.001)
        y0=[500,120]
        times=range(0,500)
        sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
        simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
        a=ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")
        print (a)

#Changing e parameter simulation 
factor=[0.25,.333,.5,1,2,3,4]
y=[]
for f in factor:
    e=.07
    y=[e*f]
    print "e=",y
    for i in y:
        params=(.8,i,0.2,5,400,0.001)
        y0=[500,120]
        times=range(0,500)
        sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
        simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
        a=ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")
        print (a)

#Changing s parameter simulation 
factor=[0.25,.333,.5,1,2,3,4]
y=[]
for f in factor:
    s=.2
    y=[s*f]
    print "s=",y
    for i in y:
        params=(.8,0.07,i,5,400,0.001)
        y0=[500,120]
        times=range(0,500)
        sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
        simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
        a=ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")
        print (a)
        
#Changing w parameter simulation 
factor=[0.25,.333,.5,1,2,3,4]
y=[]
for f in factor:
    w=5
    y=[w*f]
    print "w=",y
    for i in y:
        params=(.8,0.07,0.2,i,400,0.001)
        y0=[500,120]
        times=range(0,500)
        sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
        simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
        a=ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")
        print (a)

#Changing d parameter simulation 
factor=[0.25,.333,.5,1,2,3,4]
y=[]
for f in factor:
    d=400
    y=[d*f]
    print "d=",y
    for i in y:
        params=(.8,0.07,0.2,5,i,0.001)
        y0=[500,120]
        times=range(0,500)
        sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
        simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
        a=ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")
        print (a)

#Changing a parameter simulation 
factor=[0.25,.333,.5,1,2,3,4]
y=[]
for f in factor:
    a=.001
    y=[a*f]
    print "a=",y
    for i in y:
        params=(.8,0.07,0.2,5,400,i)
        y0=[500,120]
        times=range(0,500)
        sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
        simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
        a=ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")
        print (a)

#Paradox of Enrichment a=0.0125
params=(0.8,0.07,0.2,5,400,0.0125)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")
#Paradox of Enrichment a=0.0009
params=(0.8,0.07,0.2,5,400,0.0009)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")
#Paradox of Enrichment a=0.0006
params=(0.8,0.07,0.2,5,400,0.0006)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")
#Paradox of Enrichment a=0.0005
params=(0.8,0.07,0.2,5,400,0.0005)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")




















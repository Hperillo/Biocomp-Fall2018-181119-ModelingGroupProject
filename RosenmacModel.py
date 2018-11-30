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
! pip install scikit-misc

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
params=(0.8,0.07,0.2,5,400,0.0005
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")


#Define parameters, initial values for state variables, and time steps
params=(0.8,0.07,0.2,5,400,0.001)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Increase b parameter by x4
params=(3.2,0.07,0.2,5,400,0.001)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Decrease b parameter by x2
params=(0.4,0.07,0.2,5,400,0.001)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Increase e parameter by x2
params=(0.8,0.14,0.2,5,400,0.001)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Decrease e parameter by x2
params=(0.8,0.035,0.2,5,400,0.001)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Increase s parameter by x2 
params=(0.8,0.07,0.4,5,400,0.001)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Decrease s parameter by x2
params=(0.8,0.07,0.1,5,400,0.001)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Increase w parameter by x2 
params=(0.8,0.07,0.2,10,400,0.001)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Decrease w parameter by x2
params=(0.8,0.07,0.2,2.5,400,0.001)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Increase d parameter by x2 
params=(0.8,0.07,0.2,5,800,0.001)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Decrease d parameter by x2
params=(0.8,0.07,0.2,5,200,0.001)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Increase a parameter by x2
params=(0.8,0.07,0.2,5,400,0.002)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Decrease a parameter by x2 
params=(0.8,0.07,0.2,5,400,0.0005)
y0=[500,120]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")





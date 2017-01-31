

#optical load

def AOmega(freq): return (3.0e8/(freq*1.0e9))**2
def hvkT_cmb(freq): return 6.626e-34*freq*1.0e9/(1.38e-23*2.726)

def Q_cmb(freq,w,e_opt,AOmega,hvkT_cmb):
    import numpy as np
    return (w*e_opt*AOmega)*((1000000000000*6.626e-34*(freq*1000000000)**4)/(3.0e8**2))*(1/(np.exp(hvkT_cmb)-1))

def Q_atmos(freq,w,e_opt,AOmega,Atmos,T_atmos,ZA):
    import numpy as np
    Input = w*e_opt*AOmega
    Angle = 1/np.sin(ZA*np.pi/180)
    BlackBody = ((1000000000000*6.626e-34*(freq*1000000000)**4)/(300000000**2))*(1/(np.exp(6.626e-34*freq*1000000000/(1.38e-23*T_atmos))-1))
    return Input*Atmos*Angle*BlackBody

def Q_else(freq,w,e_opt,AOmega,eps,T):
    import numpy as np
    Input = w*e_opt*AOmega
    BlackBody = ((1000000000000*6.626e-34*(freq*1000000000)**4)/(300000000**2))*(1/(np.exp(6.626e-34*freq*1000000000/(1.38e-23*T))-1))
    return Input*eps*BlackBody

def Trj(freq,Q_tot,w,e_opt,AOmega):                              #Rayleigh–Jeans temperature
    Input = w*e_opt*AOmega
    return Q_tot/(Input*((1000000000000*(freq*1000000000)**3)/(300000000**2))*1.38e-23)

def rPTrj(Q,T):                         #the ratio between Q_tot and Trj
    return Q/T

def ThetaT(Q_CMB,hvkT_cmb):
    import numpy as np
    return (Q_CMB/2.74)*hvkT_cmb*np.exp(hvkT_cmb)/(np.exp(hvkT_cmb)-1)

#dust
def x(freq,T_2):
    return 6.626E-34*freq*1000000000/(1.38E-23*T_2)

def nln_cmb(freq,T_2,X):
    import numpy as np
    return (6.626E-34*((freq*1000000000)**4)/((300000000)**2))*X*np.exp(X)/(T_2*((np.exp(X)-1)**2))

def nln_dust(freq,beta_dust,T_dust):
    import numpy as np
    return (freq**beta_dust)*(6.626E-34*((freq*1000000000)**4)/((300000000)**2))/(np.exp(6.626E-34*freq*1000000000/(1.38E-23*T_dust))-1) #nln(dust)/nln(cmb)=1/(NED/NET)

#synchrotron
def NES_NET(hvkT_cmb,freq,beta):
    import numpy as np
    return (hvkT_cmb*hvkT_cmb*np.exp(hvkT_cmb)/((np.exp(hvkT_cmb)-1)**2))/(100000*(freq**beta))

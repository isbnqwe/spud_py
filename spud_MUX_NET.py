#MUX and NET calculation
def Psat(SF,Q):
    return SF*Q

def P(Psat,Q_tot):
    return Psat-Q_tot

def rT(Tc,T0):
    return Tc/T0

def t(rT):
    return 1-1/rT

def G0(Psat,beta,T0,Tc):
    return Psat*(1+beta)/(T0*(((Tc/T0)**(1+beta))-1))

def Gc(G0,rT,beta):
    return G0*rT**beta

def f(beta,t):
    return ((beta+1)/(2*beta+3))*((1-t)**(3+2*beta)-1)/((1-t)**(beta+1)-1)

def Ldc(alpha,P,Gc,Tc):
    return alpha*P/(Gc*Tc)

def I0(P,Rop):
    import numpy as np
    return np.sqrt(P/Rop)

def CG(C0,Tc,T0,gamma,Gc):
    return 1000000*(C0*(Tc/T0)**gamma)/Gc

def tau_el(LsN,Rl,R0,beta):
    return LsN/(Rl+R0*(1+beta))

def tau_1(C0,Tc,T0,gamma,Gc,Ldc):
    return 1000000*(C0*(Tc/T0)**gamma)/(Gc*(1-Ldc))

def tau_mi(tau_el,tau_1,Rop,Ldc,beta1,L_SqdNyq,CG):
    import numpy as np
    return 1/(0.5/tau_el+0.5/tau_1-0.5*np.sqrt((((1/tau_el)-(1/tau_1))**2)-4*Rop*Ldc*(2+beta1)/(L_SqdNyq*CG)))

def tau_pl(tau_el,tau_1,Rop,Ldc,beta1,L_SqdNyq,CG):
    import numpy as np
    return 1/(0.5/tau_el+0.5/tau_1+0.5*np.sqrt((((1/tau_el)-(1/tau_1))**2)-4*Rop*Ldc*(2+beta1)/(L_SqdNyq*CG)))

def V_bias(Rop,P):
    import numpy as np
    return np.sqrt(Rop*P)

def Pshunt(V_bias,Rop,Rs_vs_Rop):
    return V_bias**2/(Rop*Rs_vs_Rop)

def Sdc(I0,Rop,beta1,tau_pl,tau_mi,tau_1):
    return -(1/(I0*Rop*(2+beta1)))*(1-(tau_pl/tau_1))*(1-(tau_mi/tau_1))

def F_nyq(Rdyn,Lstray,Nmux):
    import numpy
    return 1000*(Rdyn/(2*numpy.pi*Lstray*2*Nmux))

def tau(C0,rT,gamma,Gc,Ldc):
    return 1000*(C0*rT**gamma)/(Gc*(1+Ldc))

def MSF(tau_el,tau_1,Rop,Ldc,beta1,L_SqdNyq,CG):                      #MUX stability factor
    return (((1/tau_el)-(1/tau_1))**2)/(4*Rop*Ldc*(2+beta1)/(L_SqdNyq*CG))

def Lcrit(Rop,CG,Ldc,beta1,Rs_vs_Rop):
    import numpy as np
    return ((Rop*CG)/((Ldc-1)**2))*(Ldc*(3+beta1-Rs_vs_Rop)+(1+beta1+Rs_vs_Rop)-2*np.sqrt(Ldc*(2+beta1)*(Ldc*(1-Rs_vs_Rop)+(1+beta1+Rs_vs_Rop))))


#NEP
def NEPphonon(f,Gc,Tc):
    import numpy as np
    return np.sqrt(f*4*1.38E-23*Gc*0.000000000001*Tc**2)

def NEPJohnson(Nos_ExcJ,Tc,Rop,I0,Ldc):
    import numpy as np
    return 0.000001*Nos_ExcJ*np.sqrt(4*1.38E-23*Tc*Rop)*I0/Ldc

def NEPshunt(I0,Ldc,T0,Rs_vs_Rop,Rop):
    import numpy as np
    return 0.000001*I0*((Ldc-1)/Ldc)*np.sqrt(4*1.38E-23*T0*Rs_vs_Rop*Rop)

def NEPshot(freq,Q):
    import numpy as np
    return np.sqrt(2*6.626E-34*freq*1000000000*Q*0.000000000001)

def NEPbose(Q,freq,w):
    import numpy as np
    return np.sqrt(2)*Q*0.000000000001/np.sqrt(freq*1000000000*w)

def NEPtot(NEPphonon,NEPJohnson,NEPshunt,NEPshot,NEPbose):
    import numpy as np
    return np.sqrt(NEPphonon**2+NEPJohnson**2+NEPshunt**2+NEPshot**2+NEPbose**2)

def SQUID_ALIAS(Nmux,No = 1001):
    SQD_sum = 0
    for i in range(1,No):
        SQD_sum = SQD_sum+1.0/(i**2+Nmux**2)
    return SQD_sum

def det_ALIAS(NEPphonon,NEPshot,NEPbose,NEPJohnson,NEPshunt,F_nyq,CG,tau_1,tau_mi,tau_pl,No = 11):
    import numpy as np
    det_sum = 0
    for i in range(1,No):
        ph_shot_bose = NEPphonon**2+NEPshot**2+NEPbose**2
        Johnson = (NEPJohnson**2)*(1+(4*np.pi*i*0.001*F_nyq*CG)**2)
        shunt = (NEPshunt**2)*(1+(4*np.pi*i*0.001*F_nyq*tau_1)**2)
        factor = ((1+(4*np.pi*i*0.001*F_nyq*tau_mi)**2)*(1+(4*np.pi*i*0.001*F_nyq*tau_pl)**2))
        tot = (ph_shot_bose+Johnson+shunt)/factor
        det_sum = det_sum + tot
    return det_sum

def NEPdet(NEPphonon,NEPJohnson,NEPshunt,NEPshot,NEPbose,det_sum):
    import numpy as np
    return np.sqrt(NEPphonon**2+NEPJohnson**2+NEPshunt**2+NEPshot**2+NEPbose**2+2*det_sum)

def NEPsq(In_Sqd,Nmux,SQD_sum,Sdc):
    import numpy as np
    return 0.000000000000000001*In_Sqd*np.sqrt(1+2*Nmux*SQD_sum)/np.absolute(Sdc)

def NEPtot_MUXED(NEPsq,NEPdet):
    import numpy as np
    return np.sqrt(NEPsq**2+NEPdet**2)


#NET
def NETbolo(NEPtot_MUXED,ThetaT):
    import numpy as np
    return 1000000*np.sqrt(0.5)*NEPtot_MUXED/(ThetaT*0.000000000001)

def NETfp(NETbolo,Num_pixels):
    import numpy as np
    return NETbolo/np.sqrt(2*Num_pixels)

def NE_DUST(NEPtot_MUXED,Q_DUST,Num_pixels):
    import numpy as np
    return 48140000000000000*NEPtot_MUXED/(Q_DUST*np.sqrt(2*Num_pixels))


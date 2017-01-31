
def Freq(freq):
    if freq == 35:
        return 35
    elif freq == 40:
        return 40
    else:
        return 0

#Temperature
def T_atmos(freq):
    if freq == 35:
        return 220.0
    elif freq == 40:
        return 220.0
    else:
        return 0

def T_WFB(freq):
    if freq == 35:
        return 220.0
    elif freq == 40:
        return 220.0
    else:
        return 0

def T_Blk1(freq):
    if freq == 35:
        return 150.0
    elif freq == 40:
        return 150.0
    else:
        return 0

def T_Blk2(freq):
    if freq == 35:
        return 70.0
    elif freq == 40:
        return 70.0
    else:
        return 0

def T_Blk3(freq):
    if freq == 35:
        return 30.0
    elif freq == 40:
        return 30.0
    else:
        return 0

def T_Wp(freq):
    if freq == 35:
        return 6.0
    elif freq == 40:
        return 6.0
    else:
        return 0

def T_Ls(freq):
    if freq == 35:
        return 4.0
    elif freq == 40:
        return 4.0
    else:
        return 0

def T_dust(freq):
    if freq == 35:
        return 18.7
    elif freq == 40:
        return 18.7
    else:
        return 0

#parameters for optical load
    
def w(freq):           #bandwidth
    if freq == 35:
        return 0.25
    elif freq == 40:
        return 0.25
    else:
        return 0
def e_opt(freq):
    if freq == 35:
        return 0.30 #optical efficiency
    elif freq == 40:
        return 0.30
    else:
        return 0
def ZA(freq):
    if freq == 35:
        return 50 #Zenith Angle
    elif freq == 40:
        return 50
    else:
        return 0
def Atmos(freq):
    if freq == 35:
        return 3.40e-2 #Atmosphere
    elif freq == 40:
        return 3.40e-2
    else:
        return 0
def WFB(freq):
    if freq == 35:
        return 0.010 #Window+FB
    elif freq == 40:
        return 0.010
    else:
        return 0
def Blocker1(freq):
    if freq == 35:
        return 0.010
    elif freq == 40:
        return 0.010
    else:
        return 0
def Blocker2(freq):
    if freq == 35:
        return 0.010
    elif freq == 40:
        return 0.010
    else:
        return 0
def Blocker3(freq):
    if freq == 35:
        return 0.010
    elif freq == 40:
        return 0.010
    else:
        return 0
def Waveplate(freq):
    if freq == 35:
        return 0.000
    elif freq == 40:
        return 0.000
    else:
        return 0
def Lenses(freq):
    if freq == 35:
        return 0.100
    elif freq == 40:
        return 0.100
    else:
        return 0
def WP_cycles_FWHM(freq):
    if freq == 35:
        return 4
    elif freq == 40:
        return 4
    else:
        return 0

#parameters for MUX and NET calculation
def Freqx(freq):
    if freq == 35:
        return 35  # /GHz Frequency
    elif freq == 40:
        return 40
    else:
        return 0
def Num_pixels(freq):
    if freq == 35:
        return 36  # Number of pixels
    elif freq == 40:
        return 36
    else:
        return 0
def T0(freq):
    if freq == 35:
        return 0.250  # K
    elif freq == 40:
        return 0.250
    else:
        return 0
def Tc(freq):
    if freq == 35:
        return 0.520  # K
    elif freq == 40:
        return 0.520
    else:
        return 0
def C0(freq):
    if freq == 35:
        return 1.0  # /pJ/k
    elif freq == 40:
        return 1.0
    else:
        return 0
def SF(freq):
    if freq == 35:
        return 2.0  # Safe Fraction
    elif freq == 40:
        return 2.0
    else:
        return 0
def Rop(freq):
    if freq == 35:
        return 0.030  # /Ohms
    elif freq == 40:
        return 0.030
    else:
        return 0
def L_SqdNyq(freq):
    if freq == 35:
        return 1.35  # /uH L(squid + nyquist)
    elif freq == 40:
        return 1.35
    else:
        return 0
def In_Sqd(freq):
    if freq == 35:
        return 3.00  # pA/rtHz
    elif freq == 40:
        return 3.00
    else:
        return 0
def Rdyn(freq):
    if freq == 35:
        return 4.0  # /Ohms (SQUID dyanmic R)
    elif freq == 40:
        return 4.0
    else:
        return 0
def Nmux(freq):
    if freq == 35:
        return 33
    elif freq == 40:
        return 33
    else:
        return 0
def L_Wire(freq):
    if freq == 35:
        return 0.3  # /uH/m L(wire) (2nd stage - SA)
    elif freq == 40:
        return 0.3
    else:
        return 0
def Rs_vs_Rop(freq):
    if freq == 35:
        return 0.10  # Rs/Rop
    elif freq == 40:
        return 0.10
    else:
        return 0
def Nos_ExcJ(freq):
    if freq == 35:
        return 1.0  # Excess Johnson noise
    elif freq == 40:
        return 1.0
    else:
        return 0
def alpha(freq):
    if freq == 35:
        return 100.0
    elif freq == 40:
        return 100.0
    else:
        return 0
def beta(freq):
    if freq == 35:
        return 2.0
    elif freq == 40:
        return 2.0
    else:
        return 0
def beta1(freq):
    if freq == 35:
        return 0.0
    elif freq == 40:
        return 0.0
    else:
        return 0

def gamma(freq):
    if freq == 35:
        return 1.0
    elif freq == 40:
        return 1.0
    else:
        return 0


    #dust

def T_2(freq):
    if freq == 35:
        return 2.72548
    elif freq == 40:
        return 2.72548
    else:
        return 0

def beta_dust(freq):
    if freq == 35:
        return 1.65
    elif freq == 40:
        return 1.65
    else:
        return 0

    #synchrotron
def beta_sync(freq):
    if freq == 35:
        return -3.3
    elif freq == 40:
        return -3.3
    else:
        return 0





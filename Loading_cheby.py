def Q_atm(freq_center,ripple_dB = 0.5,poles = 3):

    import numpy as np
    import Pars_spud


    #freq_center = 35.0  # 250? 
    bw = Pars_spud.w(freq_center)
    
    Ripple = np.sqrt((10**(ripple_dB/20))**2-1)

    e_opt = Pars_spud.e_opt(freq_center)
    SF = Pars_spud.SF(freq_center)
    Tc = Pars_spud.Tc(freq_center)
    beta = Pars_spud.beta(freq_center)
    ZA = Pars_spud.ZA(freq_center)
    WFB = Pars_spud.WFB(freq_center)
    Blk1 = Pars_spud.Blocker1(freq_center)
    Blk1 = Pars_spud.Blocker2(freq_center)
    Blk1 = Pars_spud.Blocker3(freq_center)
    beta_dust = Pars_spud.beta_dust(freq_center)

    T_atmos = Pars_spud.T_atmos(freq_center)
    T_WFB = Pars_spud.T_WFB(freq_center)
    T_Blk1 = Pars_spud.T_Blk1(freq_center)
    T_Blk2 = Pars_spud.T_Blk2(freq_center)
    T_Blk3 = Pars_spud.T_Blk3(freq_center)
    T_Wp = Pars_spud.T_Wp(freq_center)
    T_Ls = Pars_spud.T_Ls(freq_center)
    T_dust = Pars_spud.T_dust(freq_center)


    v,Tatm,Trj = np.loadtxt('Loading_cheby.txt', skiprows=1, unpack=True)

    row = [0 for i in range(5000)]
    for i in range(0,5000):
        row[i] = i+2

    adj_freq = [0 for i in range(5000)]
    for i in range(0,5000):
        adj_freq[i] = (v[i]/freq_center-freq_center/v[i])/bw

    w = 11
    h = 5000
    chebyM = [[0 for x in range(w)] for y in range(h)]
    for y in range(0,5000):
        chebyM[y][0] = 1+0*adj_freq[y]
        chebyM[y][1] = adj_freq[y]
        chebyM[y][2] = 2*adj_freq[y]*chebyM[y][1]-chebyM[y][0]
        chebyM[y][3] = 2*adj_freq[y]*chebyM[y][2]-chebyM[y][1]
        chebyM[y][4] = 2*adj_freq[y]*chebyM[y][3]-chebyM[y][2]
        chebyM[y][5] = 2*adj_freq[y]*chebyM[y][4]-chebyM[y][3]
        chebyM[y][6] = 2*adj_freq[y]*chebyM[y][5]-chebyM[y][4]
        chebyM[y][7] = 2*adj_freq[y]*chebyM[y][6]-chebyM[y][5]
        chebyM[y][8] = 2*adj_freq[y]*chebyM[y][7]-chebyM[y][6]
        chebyM[y][9] = 2*adj_freq[y]*chebyM[y][8]-chebyM[y][7]
        chebyM[y][10] = 2*adj_freq[y]*chebyM[y][9]-chebyM[y][8]

    trans = [0 for i in range(5000)]
    for i in range(5000):
        trans[i] = 1.0/np.sqrt(1.0+(Ripple*chebyM[i][poles])**2)

    power_trans = [0 for i in range(5000)]
    for i in range(5000):
        power_trans[i] = trans[i]**2

    power_trans_dB = [0 for i in range(5000)]
    for i in range(5000):
        power_trans_dB[i] = 10*np.log10(power_trans[i])

    Tdv = [0 for i in range(4999)]
    for i in range(4999):
        Tdv[i] = power_trans[i]*(v[i+1]-v[i])

    vTdv = [0 for i in range(4999)]
    for i in range(4999):
        vTdv[i] = v[i]*power_trans[i]*(v[i+1]-v[i])

    T2dv = [0 for i in range(4999)]
    for i in range(4999):
        T2dv[i] = power_trans[i]*power_trans[i]*(v[i+1]-v[i])

    dQatm = [0 for i in range(4999)]
    Qatm = 0
    for i in range(4999):
        dQatm[i] = power_trans[i]*e_opt*1.38E-23*Trj[i]*(v[i+1]-v[i])*1E+21/np.sin(ZA*np.pi/180)
        Qatm = Qatm+dQatm[i]

    return Qatm

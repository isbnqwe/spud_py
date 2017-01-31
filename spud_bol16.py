import numpy as np
import Pars_spud
import spud_Optical_Loading
import Loading_cheby
import spud_MUX_NET

freq = 35

#check the input freqency
Freq = Pars_spud.Freq(freq)
if not Freq:
    print("****************************")
    print("*End calculation and check.*")
    print("****************************")
else:
    print("*************************************************")
    print("Frequency : {0:d} GHz".format(freq))
    print("*************************************************")
    
    #a few reference temperatures
    T_atmos = Pars_spud.T_atmos(Freq)
    T_WFB = Pars_spud.T_WFB(Freq)
    T_Blk1 = Pars_spud.T_Blk1(Freq)
    T_Blk2 = Pars_spud.T_Blk2(Freq)
    T_Blk3 = Pars_spud.T_Blk3(Freq)
    T_Wp = Pars_spud.T_Wp(Freq)
    T_Ls = Pars_spud.T_Ls(Freq)

    #import parameters for optical load
    w = Pars_spud.w(Freq)
    e_opt = Pars_spud.e_opt(Freq)
    ZA = Pars_spud.ZA(Freq)
    Atmos = Pars_spud.Atmos(Freq)
    WFB = Pars_spud.WFB(Freq)
    Blk1 = Pars_spud.Blocker1(Freq)
    Blk2 = Pars_spud.Blocker2(Freq)
    Blk3 = Pars_spud.Blocker3(Freq)
    Wp = Pars_spud.Waveplate(Freq)   
    Ls = Pars_spud.Lenses(Freq)
    WP_cycles_FWHM = Pars_spud.WP_cycles_FWHM(Freq)

    #import parameters for MUX and NET
    Freqx = Pars_spud.Freqx(Freq)
    Num_pixels = Pars_spud.Num_pixels(Freq)
    T0 = Pars_spud.T0(Freq)
    Tc = Pars_spud.Tc(Freq)
    C0 = Pars_spud.C0(Freq)
    SF = Pars_spud.SF(Freq)
    Rop = Pars_spud.Rop(Freq)
    L_SqdNyq = Pars_spud.L_SqdNyq(Freq)
    In_Sqd = Pars_spud.In_Sqd(Freq)
    Rdyn = Pars_spud.Rdyn(Freq)
    Nmux = Pars_spud.Nmux(Freq)
    L_Wire = Pars_spud.L_Wire(Freq)
    Rs_vs_Rop = Pars_spud.Rs_vs_Rop(Freq)
    Nos_ExcJ = Pars_spud.Nos_ExcJ(Freq)
    alpha = Pars_spud.alpha(Freq) #logarithmic temperature sensitivity[1]
    beta = Pars_spud.beta(Freq) #thermal conductance exponent[1]
    beta1 = Pars_spud.beta1(Freq) #logarithmic current sensitivity[1]
    gamma = Pars_spud.gamma(Freq)

    #dust
    T_Dust = Pars_spud.T_dust(Freq)
    T_2 = Pars_spud.T_2(Freq)
    beta_dust = Pars_spud.beta_dust(Freq)       

    #Synchrotron
    beta_sync = Pars_spud.beta_sync(Freq)

    #optical load
    
    Q_cmb = spud_Optical_Loading.Q_cmb(Freq,w,e_opt,spud_Optical_Loading.AOmega(freq),spud_Optical_Loading.hvkT_cmb(freq))
    Q_WFB = spud_Optical_Loading.Q_else(Freq,w,e_opt,spud_Optical_Loading.AOmega(freq),WFB,T_WFB)
    Q_Blk1 = spud_Optical_Loading.Q_else(Freq,w,e_opt,spud_Optical_Loading.AOmega(freq),Blk1,T_Blk1)
    Q_Blk2 = spud_Optical_Loading.Q_else(Freq,w,e_opt,spud_Optical_Loading.AOmega(freq),Blk2,T_Blk2)
    Q_Blk3 = spud_Optical_Loading.Q_else(Freq,w,e_opt,spud_Optical_Loading.AOmega(freq),Blk3,T_Blk3)
    Q_Wp = spud_Optical_Loading.Q_else(Freq,w,e_opt,spud_Optical_Loading.AOmega(freq),Wp,T_Wp)
    Q_Ls = spud_Optical_Loading.Q_else(Freq,w,e_opt,spud_Optical_Loading.AOmega(freq),Ls,T_Ls)
    
    Q_atmos = Loading_cheby.Q_atm(Freq,0.5,3) #ripple_dB = 0.5, cheby_poles = 3

    #total energy
    Q_tot = Q_cmb+Q_atmos+Q_WFB+Q_Blk1+Q_Blk2+Q_Blk3+Q_Wp+Q_Ls

    #Other useful Quants
    ThetaT = spud_Optical_Loading.ThetaT(Q_cmb,spud_Optical_Loading.hvkT_cmb(freq))
    
    #print("*************************************************")
    #print("Total energy : Q_tot = {0:.3f} pW".format(Q_tot))
    #print("*************************************************")

    #rayleigh–Jeans temperature
    Trj = spud_Optical_Loading.Trj(freq,Q_tot,w,e_opt,spud_Optical_Loading.AOmega(freq))
    #print("*************************************************")
    #print("rayleigh–Jeans temperature : Trj = {0:.3f} K".format(Trj))
    #print("*************************************************")

    rPTrj = spud_Optical_Loading.rPTrj(Q_tot,Trj)

    #MUX and NET calculation
    
    Psat = spud_MUX_NET.Psat(SF,Q_tot)
    P = spud_MUX_NET.P(Psat,Q_tot)
    rT = spud_MUX_NET.rT(Tc,T0)
    t = spud_MUX_NET.t(rT)
    G0 = spud_MUX_NET.G0(Psat,beta,T0,Tc)
    Gc = spud_MUX_NET.Gc(G0,rT,beta)
    f = spud_MUX_NET.f(beta,t)
    Ldc = spud_MUX_NET.Ldc(alpha,P,Gc,Tc)
    I0 = spud_MUX_NET.I0(P,Rop)
    Lstray = 0.64 #/uH, this value is only for flight loading conditions
    CG = spud_MUX_NET.CG(C0,Tc,T0,gamma,Gc)
    tau_el = spud_MUX_NET.tau_el(L_SqdNyq,Rop*Rs_vs_Rop,Rop,beta1)
    tau_1 = spud_MUX_NET.tau_1(C0,Tc,T0,gamma,Gc,Ldc)
    tau_mi = spud_MUX_NET.tau_mi(tau_el,tau_1,Rop,Ldc,beta1,L_SqdNyq,CG)
    tau_pl = spud_MUX_NET.tau_pl(tau_el,tau_1,Rop,Ldc,beta1,L_SqdNyq,CG)
    V_bias = spud_MUX_NET.V_bias(Rop,P)
    Pshunt = spud_MUX_NET.Pshunt(V_bias,Rop,Rs_vs_Rop)
    Sdc = spud_MUX_NET.Sdc(I0,Rop,beta1,tau_pl,tau_mi,tau_1)
    F_nyq = spud_MUX_NET.F_nyq(Rdyn,Lstray,Nmux)
    tau = spud_MUX_NET.tau(C0,rT,gamma,Gc,Ldc)
    MSF = spud_MUX_NET.MSF(tau_el,tau_1,Rop,Ldc,beta1,L_SqdNyq,CG)#MUX stability factor
    Lcrit = spud_MUX_NET.Lcrit(Rop,CG,Ldc,beta1,Rs_vs_Rop)

    #NET
    NEPphonon = spud_MUX_NET.NEPphonon(f,Gc,Tc)
    NEPJohnson = spud_MUX_NET.NEPJohnson(Nos_ExcJ,Tc,Rop,I0,Ldc)
    NEPshunt = spud_MUX_NET.NEPshunt(I0,Ldc,T0,Rs_vs_Rop,Rop)
    NEPshot = spud_MUX_NET.NEPshot(Freq,Q_tot)
    NEPbose = spud_MUX_NET.NEPbose(Q_tot,Freq,w)
    NEPtot = spud_MUX_NET.NEPtot(NEPphonon,NEPJohnson,NEPshunt,NEPshot,NEPbose)

    SQD_sum = Nmux*spud_MUX_NET.SQUID_ALIAS(Nmux)
    det_sum = spud_MUX_NET.det_ALIAS(NEPphonon,NEPshot,NEPbose,NEPJohnson,NEPshunt,F_nyq,CG,tau_1,tau_mi,tau_pl)
    
    NEPdet = spud_MUX_NET.NEPdet(NEPphonon,NEPJohnson,NEPshunt,NEPshot,NEPbose,det_sum)
    NEPsq = spud_MUX_NET.NEPsq(In_Sqd,Nmux,SQD_sum,Sdc)
    NEPtot_MUXED = spud_MUX_NET.NEPtot_MUXED(NEPsq,NEPdet)

    MUX_penalty = NEPtot_MUXED/NEPtot

    NETbolo = spud_MUX_NET.NETbolo(NEPtot_MUXED,ThetaT)
    NETfp = spud_MUX_NET.NETfp(NETbolo,Num_pixels)
    

    TrjSAT = Trj*SF

        #NET_DUST
    ddust_dcmb = (spud_Optical_Loading.nln_dust(Freq,beta_dust,T_Dust)/spud_Optical_Loading.nln_dust(150,beta_dust,T_Dust))/(spud_Optical_Loading.nln_cmb(Freq,T_2,spud_Optical_Loading.x(Freq,T_2))/spud_Optical_Loading.nln_cmb(150,T_2,spud_Optical_Loading.x(150,T_2)))
    Q_DUST = Q_cmb*ddust_dcmb
    NEDbolo = NETbolo/ddust_dcmb
    NED_fp = NEDbolo/np.sqrt(2*Num_pixels)

        #Synchrotron
    NES_NET = spud_Optical_Loading.NES_NET(spud_Optical_Loading.hvkT_cmb(Freq),Freq,beta_sync)/spud_Optical_Loading.NES_NET(spud_Optical_Loading.hvkT_cmb(150),150,beta_sync)
    ##I have add a normalization factor to NES_NET here.
    Q_Sync = Q_cmb/NES_NET
    NESbolo = NETbolo*NES_NET
    NES_fp = NESbolo/np.sqrt(2*Num_pixels)
    ##Dust model and synchrotron model are very similar to each other. Here DUST comes from Jamie's SPUDsheet, while SYNC comes from
    ##Lorentz's MIDEX. After carefully check, they are realy alike (one can check the dust model in both these sheet). ddust_dcmb=
    ##ddust_dcmb=1/(NED/NET)
    
    
    db_freq = (1000.0/(2*np.pi*tau))
    WP_mod_freq = db_freq/2
    scan_rate = (90/Freq)/(WP_cycles_FWHM/WP_mod_freq)
    spin_rate = 1/(6*np.cos(ZA*np.pi/180)/scan_rate)

    
    f = open('/Users/Cheng/Documents/BICEP/Freq_Cal/spud_py/output/{0:d}GHzResult.txt'.format(Freq),'w')
    f.write('Q(atmos) = {0:.3f}\n'.format(Q_atmos))
    f.write('Q(cmb) = {0:.3f}\n'.format(Q_cmb))
    f.write('Q(WFB) = {0:.3f}\n'.format(Q_WFB))
    f.write('Q(Blocker1) = {0:.3f}\n'.format(Q_Blk1))
    f.write('Q(Blocker2) = {0:.3f}\n'.format(Q_Blk2))
    f.write('Q(Blocker3) = {0:.3f}\n'.format(Q_Blk3))
    f.write('Q(Waveplate) = {0:.3f}\n'.format(Q_Wp))
    f.write('Q(Lens) = {0:.3f}\n'.format(Q_Ls))
    f.write('Q(Total) = {0:.3f}\n'.format(Q_tot))

    f.write('Trj = {0:.3f}\n'.format(Trj))

    f.write('NET(bolo) = {0:.3f}\n'.format(NETbolo))
    f.write('NET(fp) = {0:.3f}\n'.format(NETfp))
    f.write('NET(dust_fp) = {0:.3f}\n'.format(NED_fp))
    f.write('NET(sync_fp) = {0:.3f}\n'.format(NES_fp))
    
    f.close()
    
    #print(db_freq,WP_mod_freq,scan_rate,spin_rate)



#=================**Reference**======================#
# [1] in the Chapter “Thermal Equilibrium Calorimeters – An Intro- duction” by McCammon

#=================**BLOG**=====================#
#[170130][1135] Correct the dust model. Now dust model in this code is same with Jamie's spudsheet. 

    

import numpy as np
from math import exp
from math import log
from gcubed.base_equations import BaseEquations


class Equations(BaseEquations):

    # Equation block 1

    def x1l_14(self):
        self.x1l[14] = 0
    # Equation block 2

    def z1l_154(self):
        self.z1l[154] = self.z1r[12]+self.z1r[62]+self.exo[28]+self.z1r[44]+self.z1r[36]+(  self.z1r[26] +self.z1r[28])

    def z1l_155(self):
        self.z1l[155] = self.z1r[13]+self.z1r[63]+self.exo[30]+self.z1r[45]+self.z1r[37]+(  self.z1r[27] +self.z1r[29])
    # Equation block 3

    def z1l_156(self):
        self.z1l[156] = self.z1r[14]+self.z1r[64]+self.exo[29]+self.z1r[46]+self.z1r[38]+(  self.z1r[138] +self.z1r[140])

    def z1l_157(self):
        self.z1l[157] = self.z1r[15]+self.z1r[65]+self.exo[31]+self.z1r[47]+self.z1r[39]+(  self.z1r[139] +self.z1r[141])
    # Equation block 4

    def z1l_80(self):
        self.z1l[80] = (1-self.par[52])*self.z1r[154]*exp(self.z1r[226]-self.z1r[172])**self.par[216]

    def z1l_81(self):
        self.z1l[81] = (1-self.par[53])*self.z1r[155]*exp(self.z1r[227]-self.z1r[173])**self.par[217]

    def z1l_82(self):
        self.z1l[82] = (1-self.par[54])*self.z1r[156]*exp(self.z1r[228]-self.z1r[174])**self.par[218]

    def z1l_83(self):
        self.z1l[83] = (1-self.par[55])*self.z1r[157]*exp(self.z1r[229]-self.z1r[175])**self.par[219]
    # Equation block 5

    def z1l_160(self):
        self.z1l[160] = self.x1r[14]+self.z1r[234]-self.x1r[14]

    def z1l_161(self):
        self.z1l[161] = self.x1r[15]+self.z1r[235]-self.x1r[14]

    def z1l_164(self):
        self.z1l[164] = self.x1r[14]+self.z1r[236]-self.x1r[14]

    def z1l_165(self):
        self.z1l[165] = self.x1r[15]+self.z1r[237]-self.x1r[14]

    def z1l_162(self):
        self.z1l[162] = self.x1r[14]+self.z1r[234]-self.x1r[15]

    def z1l_163(self):
        self.z1l[163] = self.x1r[15]+self.z1r[235]-self.x1r[15]

    def z1l_166(self):
        self.z1l[166] = self.x1r[14]+self.z1r[236]-self.x1r[15]

    def z1l_167(self):
        self.z1l[167] = self.x1r[15]+self.z1r[237]-self.x1r[15]
    # Equation block 6

    def z1l_72(self):
        self.z1l[72] = self.par[66]*self.z1r[80]*(self.exo[0]+(1+(self.exo[118]+self.exo[134])*self.par[192]+self.exo[114]*self.par[138])*exp(self.z1r[160]-self.z1r[172]))**(-self.par[228])+self.exo[18]

    def z1l_73(self):
        self.z1l[73] = self.par[67]*self.z1r[80]*(self.exo[1]+(1+(self.exo[119]+self.exo[134])*self.par[193]+self.exo[114]*self.par[139])*exp(self.z1r[161]-self.z1r[172]))**(-self.par[228])+self.exo[19]

    def z1l_76(self):
        self.z1l[76] = self.par[70]*self.z1r[82]*(self.exo[4]+(1+(self.exo[122]+self.exo[136])*self.par[192]+self.exo[116]*self.par[138])*exp(self.z1r[164]-self.z1r[174]))**(-self.par[230])+self.exo[22]

    def z1l_77(self):
        self.z1l[77] = self.par[71]*self.z1r[82]*(self.exo[5]+(1+(self.exo[123]+self.exo[136])*self.par[193]+self.exo[116]*self.par[139])*exp(self.z1r[165]-self.z1r[174]))**(-self.par[230])+self.exo[23]

    def z1l_74(self):
        self.z1l[74] = self.par[68]*self.z1r[81]*(self.exo[2]+(1+(self.exo[120]+self.exo[135])*self.par[194]+self.exo[115]*self.par[140])*exp(self.z1r[162]-self.z1r[173]))**(-self.par[229])+self.exo[20]

    def z1l_75(self):
        self.z1l[75] = self.par[69]*self.z1r[81]*(self.exo[3]+(1+(self.exo[121]+self.exo[135])*self.par[195]+self.exo[115]*self.par[141])*exp(self.z1r[163]-self.z1r[173]))**(-self.par[229])+self.exo[21]

    def z1l_78(self):
        self.z1l[78] = self.par[72]*self.z1r[83]*(self.exo[6]+(1+(self.exo[124]+self.exo[137])*self.par[194]+self.exo[117]*self.par[140])*exp(self.z1r[166]-self.z1r[175]))**(-self.par[231])+self.exo[24]

    def z1l_79(self):
        self.z1l[79] = self.par[73]*self.z1r[83]*(self.exo[7]+(1+(self.exo[125]+self.exo[137])*self.par[195]+self.exo[117]*self.par[141])*exp(self.z1r[167]-self.z1r[175]))**(-self.par[231])+self.exo[25]
    # Equation block 7

    def z1l_168(self):
        self.z1l[168] = log((  self.z1r[72]*exp(self.z1r[160]) +self.z1r[73]*exp(self.z1r[161]))/self.z1r[80])

    def z1l_170(self):
        self.z1l[170] = log((  self.z1r[76]*exp(self.z1r[164]) +self.z1r[77]*exp(self.z1r[165]))/self.z1r[82])

    def z1l_169(self):
        self.z1l[169] = log((  self.z1r[74]*exp(self.z1r[162]) +self.z1r[75]*exp(self.z1r[163]))/self.z1r[81])

    def z1l_171(self):
        self.z1l[171] = log((  self.z1r[78]*exp(self.z1r[166]) +self.z1r[79]*exp(self.z1r[167]))/self.z1r[83])
    # Equation block 8

    def z1l_84(self):
        self.z1l[84] = (  exp(self.z1r[168])*self.z1r[80] +exp(self.z1r[170])*self.z1r[82])/exp(self.z1r[208])

    def z1l_85(self):
        self.z1l[85] = (  exp(self.z1r[169])*self.z1r[81] +exp(self.z1r[171])*self.z1r[83])/exp(self.z1r[209])
    # Equation block 9

    def z1l_40(self):
        self.z1l[40] = (  exp(self.z1r[234])*self.z1r[36] +exp(self.z1r[236])*self.z1r[38])/exp(self.z1r[210])

    def z1l_41(self):
        self.z1l[41] = (  exp(self.z1r[235])*self.z1r[37] +exp(self.z1r[237])*self.z1r[39])/exp(self.z1r[211])
    # Equation block 10

    def z1l_36(self):
        self.z1l[36] = (  self.z1r[72] +self.z1r[74])

    def z1l_37(self):
        self.z1l[37] = (  self.z1r[73] +self.z1r[75])

    def z1l_38(self):
        self.z1l[38] = (  self.z1r[76] +self.z1r[78])

    def z1l_39(self):
        self.z1l[39] = (  self.z1r[77] +self.z1r[79])
    # Equation block 11

    def z1l_234(self):
        self.z1l[234] = log((1+self.exo[110])*exp(self.z1r[226]))

    def z1l_235(self):
        self.z1l[235] = log((1+self.exo[111])*exp(self.z1r[227]))

    def z1l_236(self):
        self.z1l[236] = log((1+self.exo[112])*exp(self.z1r[228]))

    def z1l_237(self):
        self.z1l[237] = log((1+self.exo[113])*exp(self.z1r[229]))
    # Equation block 12

    def z1l_146(self):
        self.z1l[146] = self.par[52]*self.z1r[154]*exp(self.z1r[226]-self.z1r[184])**self.par[216]

    def z1l_147(self):
        self.z1l[147] = self.par[53]*self.z1r[155]*exp(self.z1r[227]-self.z1r[185])**self.par[217]

    def z1l_148(self):
        self.z1l[148] = self.par[54]*self.z1r[156]*exp(self.z1r[228]-self.z1r[186])**self.par[218]

    def z1l_149(self):
        self.z1l[149] = self.par[55]*self.z1r[157]*exp(self.z1r[229]-self.z1r[187])**self.par[219]
    # Equation block 13

    def z1l_150(self):
        self.z1l[150] = (  self.par[146]*self.z1r[146] +self.par[150]*self.z1r[148])

    def z1l_152(self):
        self.z1l[152] = (  self.par[148]*self.z1r[146] +self.par[152]*self.z1r[148])

    def z1l_151(self):
        self.z1l[151] = (  self.par[147]*self.z1r[147] +self.par[151]*self.z1r[149])

    def z1l_153(self):
        self.z1l[153] = (  self.par[149]*self.z1r[147] +self.par[153]*self.z1r[149])
    # Equation block 14

    def z1l_122(self):
        self.z1l[122] = exp(self.exo[86]+self.exo[94])**(self.par[240]-1)*self.par[88]*self.z1r[150]*exp(self.z1r[222]-self.z1r[292])**self.par[240]

    def z1l_124(self):
        self.z1l[124] = exp(self.exo[87]+self.exo[96])**(self.par[242]-1)*self.par[90]*self.z1r[152]*exp(self.z1r[224]-self.z1r[294])**self.par[242]

    def z1l_123(self):
        self.z1l[123] = exp(self.exo[88]+self.exo[95])**(self.par[241]-1)*self.par[89]*self.z1r[151]*exp(self.z1r[223]-self.z1r[293])**self.par[241]

    def z1l_125(self):
        self.z1l[125] = exp(self.exo[89]+self.exo[97])**(self.par[243]-1)*self.par[91]*self.z1r[153]*exp(self.z1r[225]-self.z1r[295])**self.par[243]
    # Equation block 15

    def z1l_30(self):
        self.z1l[30] = exp(self.exo[68]+self.exo[94])**(self.par[240]-1)*self.par[92]*self.z1r[150]*exp(self.z1r[222]-self.z1r[188])**self.par[240]

    def z1l_32(self):
        self.z1l[32] = exp(self.exo[70]+self.exo[96])**(self.par[242]-1)*self.par[94]*self.z1r[152]*exp(self.z1r[224]-self.z1r[190])**self.par[242]

    def z1l_31(self):
        self.z1l[31] = exp(self.exo[69]+self.exo[95])**(self.par[241]-1)*self.par[93]*self.z1r[151]*exp(self.z1r[223]-self.z1r[189])**self.par[241]

    def z1l_33(self):
        self.z1l[33] = exp(self.exo[71]+self.exo[97])**(self.par[243]-1)*self.par[95]*self.z1r[153]*exp(self.z1r[225]-self.z1r[191])**self.par[243]
    # Equation block 16

    def z1l_142(self):
        self.z1l[142] = exp(self.exo[94])**(self.par[240]-1)*self.par[96]*self.z1r[150]*exp(self.z1r[222]-self.z1r[176])**self.par[240]

    def z1l_144(self):
        self.z1l[144] = exp(self.exo[96])**(self.par[242]-1)*self.par[98]*self.z1r[152]*exp(self.z1r[224]-self.z1r[178])**self.par[242]

    def z1l_143(self):
        self.z1l[143] = exp(self.exo[95])**(self.par[241]-1)*self.par[97]*self.z1r[151]*exp(self.z1r[223]-self.z1r[177])**self.par[241]

    def z1l_145(self):
        self.z1l[145] = exp(self.exo[97])**(self.par[243]-1)*self.par[99]*self.z1r[153]*exp(self.z1r[225]-self.z1r[179])**self.par[243]
    # Equation block 17

    def z1l_68(self):
        self.z1l[68] = exp(self.exo[90]+self.exo[98])**(self.par[246]-1)*self.par[118]*self.z1r[106]*exp(self.z1r[206]-self.yxr[38])**self.par[246]

    def z1l_69(self):
        self.z1l[69] = exp(self.exo[91]+self.exo[99])**(self.par[247]-1)*self.par[119]*self.z1r[107]*exp(self.z1r[207]-self.yxr[39])**self.par[247]
    # Equation block 18

    def z1l_66(self):
        self.z1l[66] = exp(self.exo[98])**(self.par[246]-1)*self.par[120]*self.z1r[106]*exp(self.z1r[206]-self.z1r[204])**self.par[246]

    def z1l_67(self):
        self.z1l[67] = exp(self.exo[99])**(self.par[247]-1)*self.par[121]*self.z1r[107]*exp(self.z1r[207]-self.z1r[205])**self.par[247]
    # Equation block 19

    def z1l_70(self):
        self.z1l[70] = exp(self.exo[98])**(self.par[246]-1)*self.par[122]*self.z1r[106]*exp(self.z1r[206]-self.z1r[220])**self.par[246]

    def z1l_71(self):
        self.z1l[71] = exp(self.exo[99])**(self.par[247]-1)*self.par[123]*self.z1r[107]*exp(self.z1r[207]-self.z1r[221])**self.par[247]
    # Equation block 20

    def z1l_62(self):
        self.z1l[62] = self.par[64]*self.z1r[66]*exp(self.z1r[204]-self.z1r[238])**self.par[226]

    def z1l_63(self):
        self.z1l[63] = self.par[65]*self.z1r[67]*exp(self.z1r[205]-self.z1r[239])**self.par[227]
    # Equation block 21

    def z1l_64(self):
        self.z1l[64] = self.par[82]*self.z1r[70]*exp(self.z1r[220]-self.z1r[240])**self.par[238]

    def z1l_65(self):
        self.z1l[65] = self.par[83]*self.z1r[71]*exp(self.z1r[221]-self.z1r[241])**self.par[239]
    # Equation block 22

    def z1l_126(self):
        self.z1l[126] = self.z1r[68]+self.z1r[8]+self.exo[14]+(  self.z1r[122] +self.z1r[124])

    def z1l_127(self):
        self.z1l[127] = self.z1r[69]+self.z1r[9]+self.exo[15]+(  self.z1r[123] +self.z1r[125])
    # Equation block 23

    def z1l_226(self):
        self.z1l[226] = self.par[18]*(self.par[52]*self.z1r[184]+(1-self.par[52])*self.z1r[172])+((1-self.par[18])*log(self.par[52]*exp(self.z1r[184])**(1-self.par[216])+(1-self.par[52])*exp(self.z1r[172])**(1-self.par[216])))/(1-self.par[216]*(1-self.par[18]))

    def z1l_227(self):
        self.z1l[227] = self.par[19]*(self.par[53]*self.z1r[185]+(1-self.par[53])*self.z1r[173])+((1-self.par[19])*log(self.par[53]*exp(self.z1r[185])**(1-self.par[217])+(1-self.par[53])*exp(self.z1r[173])**(1-self.par[217])))/(1-self.par[217]*(1-self.par[19]))

    def z1l_228(self):
        self.z1l[228] = self.par[20]*(self.par[54]*self.z1r[186]+(1-self.par[54])*self.z1r[174])+((1-self.par[20])*log(self.par[54]*exp(self.z1r[186])**(1-self.par[218])+(1-self.par[54])*exp(self.z1r[174])**(1-self.par[218])))/(1-self.par[218]*(1-self.par[20]))

    def z1l_229(self):
        self.z1l[229] = self.par[21]*(self.par[55]*self.z1r[187]+(1-self.par[55])*self.z1r[175])+((1-self.par[21])*log(self.par[55]*exp(self.z1r[187])**(1-self.par[219])+(1-self.par[55])*exp(self.z1r[175])**(1-self.par[219])))/(1-self.par[219]*(1-self.par[21]))
    # Equation block 24

    def z1l_238(self):
        self.z1l[238] = log(1+self.exo[102])+self.z1r[226]

    def z1l_239(self):
        self.z1l[239] = log(1+self.exo[103])+self.z1r[227]

    def z1l_240(self):
        self.z1l[240] = log(1+self.exo[104])+self.z1r[228]

    def z1l_241(self):
        self.z1l[241] = log(1+self.exo[105])+self.z1r[229]
    # Equation block 25

    def z1l_172(self):
        self.z1l[172] = 0.0+self.par[30]*(  self.par[66]*log(self.exo[0]+(1+(self.exo[118]+self.exo[134])*self.par[192]+self.exo[114]*self.par[138])*exp(self.z1r[160])) +self.par[67]*log(self.exo[1]+(1+(self.exo[119]+self.exo[134])*self.par[193]+self.exo[114]*self.par[139])*exp(self.z1r[161])))+((1-self.par[30])*log((  self.par[66]*(self.exo[0]+(1+(self.exo[118]+self.exo[134])*self.par[192]+self.exo[114]*self.par[138])*exp(self.z1r[160]))**(1-self.par[228]) +self.par[67]*(self.exo[1]+(1+(self.exo[119]+self.exo[134])*self.par[193]+self.exo[114]*self.par[139])*exp(self.z1r[161]))**(1-self.par[228]))))/(1-self.par[228]*(1-self.par[30]))

    def z1l_174(self):
        self.z1l[174] = 0.0+self.par[32]*(  self.par[70]*log(self.exo[4]+(1+(self.exo[122]+self.exo[136])*self.par[192]+self.exo[116]*self.par[138])*exp(self.z1r[164])) +self.par[71]*log(self.exo[5]+(1+(self.exo[123]+self.exo[136])*self.par[193]+self.exo[116]*self.par[139])*exp(self.z1r[165])))+((1-self.par[32])*log((  self.par[70]*(self.exo[4]+(1+(self.exo[122]+self.exo[136])*self.par[192]+self.exo[116]*self.par[138])*exp(self.z1r[164]))**(1-self.par[230]) +self.par[71]*(self.exo[5]+(1+(self.exo[123]+self.exo[136])*self.par[193]+self.exo[116]*self.par[139])*exp(self.z1r[165]))**(1-self.par[230]))))/(1-self.par[230]*(1-self.par[32]))

    def z1l_173(self):
        self.z1l[173] = 0.0+self.par[31]*(  self.par[68]*log(self.exo[2]+(1+(self.exo[120]+self.exo[135])*self.par[194]+self.exo[115]*self.par[140])*exp(self.z1r[162])) +self.par[69]*log(self.exo[3]+(1+(self.exo[121]+self.exo[135])*self.par[195]+self.exo[115]*self.par[141])*exp(self.z1r[163])))+((1-self.par[31])*log((  self.par[68]*(self.exo[2]+(1+(self.exo[120]+self.exo[135])*self.par[194]+self.exo[115]*self.par[140])*exp(self.z1r[162]))**(1-self.par[229]) +self.par[69]*(self.exo[3]+(1+(self.exo[121]+self.exo[135])*self.par[195]+self.exo[115]*self.par[141])*exp(self.z1r[163]))**(1-self.par[229]))))/(1-self.par[229]*(1-self.par[31]))

    def z1l_175(self):
        self.z1l[175] = 0.0+self.par[33]*(  self.par[72]*log(self.exo[6]+(1+(self.exo[124]+self.exo[137])*self.par[194]+self.exo[117]*self.par[140])*exp(self.z1r[166])) +self.par[73]*log(self.exo[7]+(1+(self.exo[125]+self.exo[137])*self.par[195]+self.exo[117]*self.par[141])*exp(self.z1r[167])))+((1-self.par[33])*log((  self.par[72]*(self.exo[6]+(1+(self.exo[124]+self.exo[137])*self.par[194]+self.exo[117]*self.par[140])*exp(self.z1r[166]))**(1-self.par[231]) +self.par[73]*(self.exo[7]+(1+(self.exo[125]+self.exo[137])*self.par[195]+self.exo[117]*self.par[141])*exp(self.z1r[167]))**(1-self.par[231]))))/(1-self.par[231]*(1-self.par[33]))
    # Equation block 26

    def z1l_208(self):
        self.z1l[208] = (  self.par[208]*self.z1r[168] +self.par[210]*self.z1r[170])

    def z1l_209(self):
        self.z1l[209] = (  self.par[209]*self.z1r[169] +self.par[211]*self.z1r[171])
    # Equation block 27

    def z1l_204(self):
        self.z1l[204] = self.par[28]*(  self.par[64]*self.z1r[238])+((1-self.par[28])*log((  self.par[64]*exp(self.z1r[238])**(1-self.par[226]))))/(1-self.par[226]*(1-self.par[28]))

    def z1l_205(self):
        self.z1l[205] = self.par[29]*(  self.par[65]*self.z1r[239])+((1-self.par[29])*log((  self.par[65]*exp(self.z1r[239])**(1-self.par[227]))))/(1-self.par[227]*(1-self.par[29]))
    # Equation block 28

    def z1l_220(self):
        self.z1l[220] = self.par[40]*(  self.par[82]*self.z1r[240])+((1-self.par[40])*log((  self.par[82]*exp(self.z1r[240])**(1-self.par[238]))))/(1-self.par[238]*(1-self.par[40]))

    def z1l_221(self):
        self.z1l[221] = self.par[41]*(  self.par[83]*self.z1r[241])+((1-self.par[41])*log((  self.par[83]*exp(self.z1r[241])**(1-self.par[239]))))/(1-self.par[239]*(1-self.par[41]))
    # Equation block 29

    def z1l_184(self):
        self.z1l[184] = log(exp((  self.par[146]*self.z1r[222] +self.par[148]*self.z1r[224])))

    def z1l_185(self):
        self.z1l[185] = log(exp((  self.par[147]*self.z1r[223] +self.par[149]*self.z1r[225])))

    def z1l_186(self):
        self.z1l[186] = log(exp((  self.par[150]*self.z1r[222] +self.par[152]*self.z1r[224])))

    def z1l_187(self):
        self.z1l[187] = log(exp((  self.par[151]*self.z1r[223] +self.par[153]*self.z1r[225])))
    # Equation block 30

    def z1l_222(self):
        self.z1l[222] = self.par[42]*(self.par[84]*self.z1r[212]+self.par[88]*self.z1r[292]+self.par[92]*self.z1r[188]+self.par[96]*self.z1r[176]-self.par[88]*self.exo[86]-self.par[84]*self.exo[74]-self.par[92]*self.exo[68])+((1-self.par[42])*log(self.par[84]*exp(self.z1r[212]-self.exo[74])**(1-self.par[240])+self.par[88]*exp(self.z1r[292]-self.exo[86])**(1-self.par[240])+self.par[92]*exp(self.z1r[188]-self.exo[68])**(1-self.par[240])+self.par[96]*exp(self.z1r[176])**(1-self.par[240])))/(1-self.par[240]*(1-self.par[42]))-self.exo[94]

    def z1l_224(self):
        self.z1l[224] = self.par[44]*(self.par[86]*self.z1r[214]+self.par[90]*self.z1r[294]+self.par[94]*self.z1r[190]+self.par[98]*self.z1r[178]-self.par[90]*self.exo[87]-self.par[86]*self.exo[76]-self.par[94]*self.exo[70])+((1-self.par[44])*log(self.par[86]*exp(self.z1r[214]-self.exo[76])**(1-self.par[242])+self.par[90]*exp(self.z1r[294]-self.exo[87])**(1-self.par[242])+self.par[94]*exp(self.z1r[190]-self.exo[70])**(1-self.par[242])+self.par[98]*exp(self.z1r[178])**(1-self.par[242])))/(1-self.par[242]*(1-self.par[44]))-self.exo[96]

    def z1l_223(self):
        self.z1l[223] = self.par[43]*(self.par[85]*self.z1r[213]+self.par[89]*self.z1r[293]+self.par[93]*self.z1r[189]+self.par[97]*self.z1r[177]-self.par[89]*self.exo[88]-self.par[85]*self.exo[75]-self.par[93]*self.exo[69])+((1-self.par[43])*log(self.par[85]*exp(self.z1r[213]-self.exo[75])**(1-self.par[241])+self.par[89]*exp(self.z1r[293]-self.exo[88])**(1-self.par[241])+self.par[93]*exp(self.z1r[189]-self.exo[69])**(1-self.par[241])+self.par[97]*exp(self.z1r[177])**(1-self.par[241])))/(1-self.par[241]*(1-self.par[43]))-self.exo[95]

    def z1l_225(self):
        self.z1l[225] = self.par[45]*(self.par[87]*self.z1r[215]+self.par[91]*self.z1r[295]+self.par[95]*self.z1r[191]+self.par[99]*self.z1r[179]-self.par[91]*self.exo[89]-self.par[87]*self.exo[77]-self.par[95]*self.exo[71])+((1-self.par[45])*log(self.par[87]*exp(self.z1r[215]-self.exo[77])**(1-self.par[243])+self.par[91]*exp(self.z1r[295]-self.exo[89])**(1-self.par[243])+self.par[95]*exp(self.z1r[191]-self.exo[71])**(1-self.par[243])+self.par[99]*exp(self.z1r[179])**(1-self.par[243])))/(1-self.par[243]*(1-self.par[45]))-self.exo[97]
    # Equation block 31

    def z1l_206(self):
        self.z1l[206] = self.par[48]*(self.par[116]*self.z1r[216]+self.par[118]*self.yxr[38]+self.par[120]*self.z1r[204]+self.par[122]*self.z1r[220]-self.par[118]*self.exo[90])+((1-self.par[48])*log(self.par[116]*exp(self.z1r[216])**(1-self.par[246])+self.par[118]*exp(self.yxr[38]-self.exo[90])**(1-self.par[246])+self.par[120]*exp(self.z1r[204])**(1-self.par[246])+self.par[122]*exp(self.z1r[220])**(1-self.par[246])))/(1-self.par[246]*(1-self.par[48]))-self.exo[98]

    def z1l_207(self):
        self.z1l[207] = self.par[49]*(self.par[117]*self.z1r[217]+self.par[119]*self.yxr[39]+self.par[121]*self.z1r[205]+self.par[123]*self.z1r[221]-self.par[119]*self.exo[91])+((1-self.par[49])*log(self.par[117]*exp(self.z1r[217])**(1-self.par[247])+self.par[119]*exp(self.yxr[39]-self.exo[91])**(1-self.par[247])+self.par[121]*exp(self.z1r[205])**(1-self.par[247])+self.par[123]*exp(self.z1r[221])**(1-self.par[247])))/(1-self.par[247]*(1-self.par[49]))-self.exo[99]
    # Equation block 32

    def z1l_212(self):
        self.z1l[212] = self.z1r[222]+log((self.par[84]*self.z1r[150])/self.yxr[6])/self.par[240]+((self.exo[94]+self.exo[74])*(self.par[240]-1))/self.par[240]

    def z1l_214(self):
        self.z1l[214] = self.z1r[224]+log((self.par[86]*self.z1r[152])/self.yxr[8])/self.par[242]+((self.exo[96]+self.exo[76])*(self.par[242]-1))/self.par[242]

    def z1l_213(self):
        self.z1l[213] = self.z1r[223]+log((self.par[85]*self.z1r[151])/self.yxr[7])/self.par[241]+((self.exo[95]+self.exo[75])*(self.par[241]-1))/self.par[241]

    def z1l_215(self):
        self.z1l[215] = self.z1r[225]+log((self.par[87]*self.z1r[153])/self.yxr[9])/self.par[243]+((self.exo[97]+self.exo[77])*(self.par[243]-1))/self.par[243]
    # Equation block 33

    def z1l_216(self):
        self.z1l[216] = self.z1r[206]+log((self.par[116]*self.z1r[106])/self.yxr[10])/self.par[246]+(self.exo[98]*(self.par[246]-1))/self.par[246]

    def z1l_217(self):
        self.z1l[217] = self.z1r[207]+log((self.par[117]*self.z1r[107])/self.yxr[11])/self.par[247]+(self.exo[99]*(self.par[247]-1))/self.par[247]
    # Equation block 34

    def z1l_218(self):
        self.z1l[218] = self.zer[2]+log((self.par[108]*self.z1r[16])/self.yxr[12])/self.par[244]+(self.exo[100]*(self.par[244]-1))/self.par[244]

    def z1l_219(self):
        self.z1l[219] = self.zer[3]+log((self.par[109]*self.z1r[17])/self.yxr[13])/self.par[245]+(self.exo[101]*(self.par[245]-1))/self.par[245]
    # Equation block 35

    def x1l_38(self):
        self.x1l[38] = self.yxr[38]+self.par[252]*(self.exz[2]-self.zer[2]+self.exo[46])+(1-self.par[252])*(self.zer[2]-self.yxr[24])+self.par[254]*(log(self.z1r[126])-log(self.exo[32]))

    def x1l_39(self):
        self.x1l[39] = self.yxr[39]+self.par[253]*(self.exz[3]-self.zer[3]+self.exo[47])+(1-self.par[253])*(self.zer[3]-self.yxr[25])+self.par[255]*(log(self.z1r[127])-log(self.exo[33]))
    # Equation block 36

    def z1l_296(self):
        self.z1l[296] = self.yxr[38]

    def z1l_297(self):
        self.z1l[297] = self.yxr[39]
    # Equation block 37

    def z1l_292(self):
        self.z1l[292] = self.yxr[38]

    def z1l_294(self):
        self.z1l[294] = self.yxr[38]

    def z1l_293(self):
        self.z1l[293] = self.yxr[39]

    def z1l_295(self):
        self.z1l[295] = self.yxr[39]
    # Equation block 38

    def x1l_6(self):
        self.x1l[6] = self.z1r[114]+(1-self.par[50]-self.par[144])*self.yxr[6]

    def x1l_8(self):
        self.x1l[8] = self.z1r[116]+(1-self.par[50]-self.par[144])*self.yxr[8]

    def x1l_7(self):
        self.x1l[7] = self.z1r[115]+(1-self.par[51]-self.par[145])*self.yxr[7]

    def x1l_9(self):
        self.x1l[9] = self.z1r[117]+(1-self.par[51]-self.par[145])*self.yxr[9]
    # Equation block 39

    def x1l_10(self):
        self.x1l[10] = self.z1r[118]+(1-self.par[50]-self.par[144])*self.yxr[10]

    def x1l_11(self):
        self.x1l[11] = self.z1r[119]+(1-self.par[51]-self.par[145])*self.yxr[11]
    # Equation block 40

    def x1l_12(self):
        self.x1l[12] = self.z1r[120]+(1-self.par[50]-self.par[144])*self.yxr[12]

    def x1l_13(self):
        self.x1l[13] = self.z1r[121]+(1-self.par[51]-self.par[145])*self.yxr[13]
    # Equation block 41

    def z1l_100(self):
        self.z1l[100] = (((1+.5*(self.z1r[278]-1))*(self.z1r[278]-1)*self.yxr[6])/self.par[196])*self.par[134]+(((1+.5*(self.yxr[30]-1))*(self.yxr[30]-1)*self.yxr[6])/self.par[196])*(1-self.par[134])+self.exo[80]

    def z1l_102(self):
        self.z1l[102] = (((1+.5*(self.z1r[280]-1))*(self.z1r[280]-1)*self.yxr[8])/self.par[198])*self.par[136]+(((1+.5*(self.yxr[32]-1))*(self.yxr[32]-1)*self.yxr[8])/self.par[198])*(1-self.par[136])+self.exo[81]

    def z1l_101(self):
        self.z1l[101] = (((1+.5*(self.z1r[279]-1))*(self.z1r[279]-1)*self.yxr[7])/self.par[197])*self.par[135]+(((1+.5*(self.yxr[31]-1))*(self.yxr[31]-1)*self.yxr[7])/self.par[197])*(1-self.par[135])+self.exo[82]

    def z1l_103(self):
        self.z1l[103] = (((1+.5*(self.z1r[281]-1))*(self.z1r[281]-1)*self.yxr[9])/self.par[199])*self.par[137]+(((1+.5*(self.yxr[33]-1))*(self.yxr[33]-1)*self.yxr[9])/self.par[199])*(1-self.par[137])+self.exo[83]
    # Equation block 42

    def z1l_114(self):
        self.z1l[114] = (self.z1r[100]+(self.par[196]/2)*self.par[14]**2*self.yxr[6])/(1+self.par[196]*self.par[14])

    def z1l_116(self):
        self.z1l[116] = (self.z1r[102]+(self.par[198]/2)*self.par[16]**2*self.yxr[8])/(1+self.par[198]*self.par[16])

    def z1l_115(self):
        self.z1l[115] = (self.z1r[101]+(self.par[197]/2)*self.par[15]**2*self.yxr[7])/(1+self.par[197]*self.par[15])

    def z1l_117(self):
        self.z1l[117] = (self.z1r[103]+(self.par[199]/2)*self.par[17]**2*self.yxr[9])/(1+self.par[199]*self.par[17])
    # Equation block 43

    def z1l_108(self):
        self.z1l[108] = self.z1r[118]*(1+((self.par[200]/2)*self.z1r[118])/self.yxr[10])

    def z1l_109(self):
        self.z1l[109] = self.z1r[119]*(1+((self.par[201]/2)*self.z1r[119])/self.yxr[11])
    # Equation block 44

    def z1l_110(self):
        self.z1l[110] = self.z1r[120]*(1+((self.par[202]/2)*self.z1r[120])/self.yxr[12])

    def z1l_111(self):
        self.z1l[111] = self.z1r[121]*(1+((self.par[203]/2)*self.z1r[121])/self.yxr[13])
    # Equation block 45

    def z1l_118(self):
        self.z1l[118] = (self.yxr[10]*(self.par[130]*self.z1r[282]+(1-self.par[130])*self.yxr[34]-1))/self.par[200]

    def z1l_119(self):
        self.z1l[119] = (self.yxr[11]*(self.par[131]*self.z1r[283]+(1-self.par[131])*self.yxr[35]-1))/self.par[201]
    # Equation block 46

    def z1l_120(self):
        self.z1l[120] = (self.yxr[12]*(self.par[132]*self.z1r[284]+(1-self.par[132])*self.yxr[36]-1))/self.par[202]

    def z1l_121(self):
        self.z1l[121] = (self.yxr[13]*(self.par[133]*self.z1r[285]+(1-self.par[133])*self.yxr[37]-1))/self.par[203]
    # Equation block 47

    def j1l_0(self):
        self.j1l[0] = (1+self.z1r[98]+self.exo[50]+self.par[50])*self.yjr[0]-(1-self.exo[108])*exp(self.z1r[212]-self.zer[4])-(1-self.exo[128])*exp(self.z1r[206]-self.zer[4])*(self.par[196]/2)*(self.z1r[114]/self.yxr[6])**2

    def j1l_2(self):
        self.j1l[2] = (1+self.z1r[98]+self.exo[52]+self.par[50])*self.yjr[2]-(1-self.exo[108])*exp(self.z1r[214]-self.zer[4])-(1-self.exo[130])*exp(self.z1r[206]-self.zer[4])*(self.par[198]/2)*(self.z1r[116]/self.yxr[8])**2

    def j1l_1(self):
        self.j1l[1] = (1+self.z1r[99]+self.exo[51]+self.par[51])*self.yjr[1]-(1-self.exo[109])*exp(self.z1r[213]-self.zer[5])-(1-self.exo[129])*exp(self.z1r[207]-self.zer[5])*(self.par[197]/2)*(self.z1r[115]/self.yxr[7])**2

    def j1l_3(self):
        self.j1l[3] = (1+self.z1r[99]+self.exo[53]+self.par[51])*self.yjr[3]-(1-self.exo[109])*exp(self.z1r[215]-self.zer[5])-(1-self.exo[131])*exp(self.z1r[207]-self.zer[5])*(self.par[199]/2)*(self.z1r[117]/self.yxr[9])**2
    # Equation block 48

    def j1l_4(self):
        self.j1l[4] = (1+self.z1r[98]+self.exo[60]+self.par[50])*self.yjr[4]-(1-self.exo[108])*exp(self.z1r[216]-self.zer[4])-exp(self.z1r[206]-self.zer[4])*(self.par[200]/2)*(self.z1r[118]/self.yxr[10])**2

    def j1l_5(self):
        self.j1l[5] = (1+self.z1r[99]+self.exo[61]+self.par[51])*self.yjr[5]-(1-self.exo[109])*exp(self.z1r[217]-self.zer[5])-exp(self.z1r[207]-self.zer[5])*(self.par[201]/2)*(self.z1r[119]/self.yxr[11])**2
    # Equation block 49

    def j1l_6(self):
        self.j1l[6] = (1+self.z1r[98]+self.exo[62]+self.par[50])*self.yjr[6]-exp(self.z1r[218]-self.zer[4])-(1-self.exo[132])*exp(self.z1r[206]-self.zer[4])*(self.par[202]/2)*(self.z1r[120]/self.yxr[12])**2

    def j1l_7(self):
        self.j1l[7] = (1+self.z1r[99]+self.exo[63]+self.par[51])*self.yjr[7]-exp(self.z1r[219]-self.zer[5])-(1-self.exo[133])*exp(self.z1r[207]-self.zer[5])*(self.par[203]/2)*(self.z1r[121]/self.yxr[13])**2
    # Equation block 50

    def z1l_278(self):
        self.z1l[278] = (self.yjr[0]*exp(self.zer[4]-self.z1r[206]))/(1-self.exo[128])

    def z1l_280(self):
        self.z1l[280] = (self.yjr[2]*exp(self.zer[4]-self.z1r[206]))/(1-self.exo[130])

    def z1l_279(self):
        self.z1l[279] = (self.yjr[1]*exp(self.zer[5]-self.z1r[207]))/(1-self.exo[129])

    def z1l_281(self):
        self.z1l[281] = (self.yjr[3]*exp(self.zer[5]-self.z1r[207]))/(1-self.exo[131])
    # Equation block 51

    def z1l_282(self):
        self.z1l[282] = self.yjr[4]*exp(self.zer[4]-self.z1r[206])

    def z1l_283(self):
        self.z1l[283] = self.yjr[5]*exp(self.zer[5]-self.z1r[207])
    # Equation block 52

    def z1l_284(self):
        self.z1l[284] = (self.yjr[6]*exp(self.zer[4]-self.z1r[206]))/(1-self.exo[132])

    def z1l_285(self):
        self.z1l[285] = (self.yjr[7]*exp(self.zer[5]-self.z1r[207]))/(1-self.exo[133])
    # Equation block 53

    def x1l_30(self):
        self.x1l[30] = self.yxr[30]+self.par[0]*(self.z1r[278]-self.yxr[30])

    def x1l_32(self):
        self.x1l[32] = self.yxr[32]+self.par[0]*(self.z1r[280]-self.yxr[32])

    def x1l_31(self):
        self.x1l[31] = self.yxr[31]+self.par[1]*(self.z1r[279]-self.yxr[31])

    def x1l_33(self):
        self.x1l[33] = self.yxr[33]+self.par[1]*(self.z1r[281]-self.yxr[33])
    # Equation block 54

    def x1l_34(self):
        self.x1l[34] = self.yxr[34]+self.par[0]*(self.z1r[282]-self.yxr[34])

    def x1l_35(self):
        self.x1l[35] = self.yxr[35]+self.par[1]*(self.z1r[283]-self.yxr[35])
    # Equation block 55

    def x1l_36(self):
        self.x1l[36] = self.yxr[36]+self.par[0]*(self.z1r[284]-self.yxr[36])

    def x1l_37(self):
        self.x1l[37] = self.yxr[37]+self.par[1]*(self.z1r[285]-self.yxr[37])
    # Equation block 56

    def z1l_192(self):
        self.z1l[192] = (self.z1r[150]*exp(self.z1r[222])-self.z1r[30]*exp(self.z1r[188])-self.z1r[122]*exp(self.z1r[292])-self.z1r[142]*exp(self.z1r[176])-(1-self.exo[128])*self.z1r[100]*exp(self.z1r[206]))/exp(self.zer[4])

    def z1l_194(self):
        self.z1l[194] = (self.z1r[152]*exp(self.z1r[224])-self.z1r[32]*exp(self.z1r[190])-self.z1r[124]*exp(self.z1r[294])-self.z1r[144]*exp(self.z1r[178])-(1-self.exo[130])*self.z1r[102]*exp(self.z1r[206]))/exp(self.zer[4])

    def z1l_193(self):
        self.z1l[193] = (self.z1r[151]*exp(self.z1r[223])-self.z1r[31]*exp(self.z1r[189])-self.z1r[123]*exp(self.z1r[293])-self.z1r[143]*exp(self.z1r[177])-(1-self.exo[129])*self.z1r[101]*exp(self.z1r[207]))/exp(self.zer[5])

    def z1l_195(self):
        self.z1l[195] = (self.z1r[153]*exp(self.z1r[225])-self.z1r[33]*exp(self.z1r[191])-self.z1r[125]*exp(self.z1r[295])-self.z1r[145]*exp(self.z1r[179])-(1-self.exo[131])*self.z1r[103]*exp(self.z1r[207]))/exp(self.zer[5])
    # Equation block 57

    def z1l_198(self):
        self.z1l[198] = (self.z1r[106]*exp(self.z1r[206])-self.z1r[66]*exp(self.z1r[204])-self.z1r[68]*exp(self.yxr[38])-self.z1r[70]*exp(self.z1r[220])-self.z1r[108]*exp(self.z1r[206]))/exp(self.zer[4])

    def z1l_199(self):
        self.z1l[199] = (self.z1r[107]*exp(self.z1r[207])-self.z1r[67]*exp(self.z1r[205])-self.z1r[69]*exp(self.yxr[39])-self.z1r[71]*exp(self.z1r[221])-self.z1r[109]*exp(self.z1r[207]))/exp(self.zer[5])
    # Equation block 58

    def z1l_200(self):
        self.z1l[200] = (self.z1r[16]*exp(self.zer[2])-self.z1r[4]*exp(self.z1r[180])-self.z1r[8]*exp(self.yxr[38])-self.z1r[10]*exp(self.z1r[182])-(1-self.exo[132])*self.z1r[110]*exp(self.z1r[206]))/exp(self.zer[4])

    def z1l_201(self):
        self.z1l[201] = (self.z1r[17]*exp(self.zer[3])-self.z1r[5]*exp(self.z1r[181])-self.z1r[9]*exp(self.yxr[39])-self.z1r[11]*exp(self.z1r[183])-(1-self.exo[133])*self.z1r[111]*exp(self.z1r[207]))/exp(self.zer[5])
    # Equation block 59

    def z1l_196(self):
        self.z1l[196] = (  self.z1r[192] +self.z1r[194])+self.z1r[198]

    def z1l_197(self):
        self.z1l[197] = (  self.z1r[193] +self.z1r[195])+self.z1r[199]
    # Equation block 60

    def z1l_254(self):
        self.z1l[254] = (self.yjr[0]*self.yxr[6])/(1-self.exo[128])

    def z1l_256(self):
        self.z1l[256] = (self.yjr[2]*self.yxr[8])/(1-self.exo[130])

    def z1l_255(self):
        self.z1l[255] = (self.yjr[1]*self.yxr[7])/(1-self.exo[129])

    def z1l_257(self):
        self.z1l[257] = (self.yjr[3]*self.yxr[9])/(1-self.exo[131])
    # Equation block 61

    def z1l_258(self):
        self.z1l[258] = (  self.z1r[254] +self.z1r[256])

    def z1l_259(self):
        self.z1l[259] = (  self.z1r[255] +self.z1r[257])
    # Equation block 62

    def z1l_104(self):
        self.z1l[104] = (  self.z1r[100] +self.z1r[102])

    def z1l_105(self):
        self.z1l[105] = (  self.z1r[101] +self.z1r[103])
    # Equation block 63

    def z1l_106(self):
        self.z1l[106] = self.z1r[108]+self.z1r[110]+self.z1r[104]

    def z1l_107(self):
        self.z1l[107] = self.z1r[109]+self.z1r[111]+self.z1r[105]
    # Equation block 64

    def zel_4(self):
        self.zel[4] = (  self.par[204]*self.z1r[184] +self.par[206]*self.z1r[186])

    def zel_5(self):
        self.zel[5] = (  self.par[205]*self.z1r[185] +self.par[207]*self.z1r[187])
    # Equation block 65

    def z1l_210(self):
        self.z1l[210] = (  self.par[212]*self.z1r[234] +self.par[214]*self.z1r[236])

    def z1l_211(self):
        self.z1l[211] = (  self.par[213]*self.z1r[235] +self.par[215]*self.z1r[237])
    # Equation block 66

    def zel_0(self):
        self.zel[0] = (  exp(self.z1r[184])*self.z1r[146] +exp(self.z1r[186])*self.z1r[148])/exp(self.zer[4])

    def zel_1(self):
        self.zel[1] = (  exp(self.z1r[185])*self.z1r[147] +exp(self.z1r[187])*self.z1r[149])/exp(self.zer[5])
    # Equation block 67

    def x1l_22(self):
        self.x1l[22] = self.zer[0]

    def x1l_23(self):
        self.x1l[23] = self.zer[1]
    # Equation block 68

    def z1l_88(self):
        self.z1l[88] = self.z1r[286]-self.z1r[266]+self.z1r[98]*self.yxr[4]+self.z1r[112]/exp(self.z1r[246])+self.z1r[200]+(1-self.exo[108])*self.z1r[196]+((1-self.exo[126])*(exp(self.yxr[38])*(self.z1r[68]+self.z1r[8])+exp(self.z1r[296])*self.exo[14]+(  exp(self.z1r[292])*self.z1r[122] +exp(self.z1r[294])*self.z1r[124])))/exp(self.zer[4])

    def z1l_89(self):
        self.z1l[89] = self.z1r[287]-self.z1r[267]+self.z1r[99]*self.yxr[5]+self.z1r[113]/exp(self.z1r[247])+self.z1r[201]+(1-self.exo[109])*self.z1r[197]+((1-self.exo[127])*(exp(self.yxr[39])*(self.z1r[69]+self.z1r[9])+exp(self.z1r[297])*self.exo[15]+(  exp(self.z1r[293])*self.z1r[123] +exp(self.z1r[295])*self.z1r[125])))/exp(self.zer[5])
    # Equation block 69

    def z1l_16(self):
        self.z1l[16] = self.par[128]*(self.par[248]+self.exo[58])*self.z1r[298]*exp(self.zer[4]-self.zer[2])+(1-self.par[128])*self.par[156]*self.z1r[88]*exp(self.zer[4]-self.zer[2])+self.exo[78]

    def z1l_17(self):
        self.z1l[17] = self.par[129]*(self.par[249]+self.exo[59])*self.z1r[299]*exp(self.zer[5]-self.zer[3])+(1-self.par[129])*self.par[157]*self.z1r[89]*exp(self.zer[5]-self.zer[3])+self.exo[79]
    # Equation block 70

    def z1l_112(self):
        self.z1l[112] = (  self.z1r[98]*exp(self.z1r[246])*self.yxr[0] +self.z1r[99]*exp(self.z1r[247])*self.yxr[2])

    def z1l_113(self):
        self.z1l[113] = (  self.z1r[98]*exp(self.z1r[246])*self.yxr[1] +self.z1r[99]*exp(self.z1r[247])*self.yxr[3])
    # Equation block 71

    def z1l_86(self):
        self.z1l[86] = (  self.x1r[20]*exp(self.z1r[246])*self.yxr[0] +self.x1r[21]*exp(self.z1r[247])*self.yxr[2])

    def z1l_87(self):
        self.z1l[87] = (  self.x1r[20]*exp(self.z1r[246])*self.yxr[1] +self.x1r[21]*exp(self.z1r[247])*self.yxr[3])
    # Equation block 72

    def z1l_8(self):
        self.z1l[8] = exp(self.exo[92]+self.exo[100])**(self.par[244]-1)*self.par[110]*self.z1r[16]*exp(self.zer[2]-self.yxr[38])**self.par[244]

    def z1l_9(self):
        self.z1l[9] = exp(self.exo[93]+self.exo[101])**(self.par[245]-1)*self.par[111]*self.z1r[17]*exp(self.zer[3]-self.yxr[39])**self.par[245]
    # Equation block 73

    def z1l_4(self):
        self.z1l[4] = exp(self.exo[72]+self.exo[100])**(self.par[244]-1)*self.par[112]*self.z1r[16]*exp(self.zer[2]-self.z1r[180])**self.par[244]

    def z1l_5(self):
        self.z1l[5] = exp(self.exo[73]+self.exo[101])**(self.par[245]-1)*self.par[113]*self.z1r[17]*exp(self.zer[3]-self.z1r[181])**self.par[245]
    # Equation block 74

    def z1l_10(self):
        self.z1l[10] = exp(self.exo[100])**(self.par[244]-1)*self.par[114]*self.z1r[16]*exp(self.zer[2]-self.z1r[182])**self.par[244]

    def z1l_11(self):
        self.z1l[11] = exp(self.exo[101])**(self.par[245]-1)*self.par[115]*self.z1r[17]*exp(self.zer[3]-self.z1r[183])**self.par[245]
    # Equation block 75

    def z1l_6(self):
        self.z1l[6] = exp(self.exo[100])**(self.par[244]-1)*self.par[108]*self.z1r[16]*exp(self.zer[2]-self.z1r[218])**self.par[244]

    def z1l_7(self):
        self.z1l[7] = exp(self.exo[101])**(self.par[245]-1)*self.par[109]*self.z1r[17]*exp(self.zer[3]-self.z1r[219])**self.par[245]
    # Equation block 76

    def z1l_12(self):
        self.z1l[12] = self.par[62]*self.z1r[4]*exp(self.z1r[180]-self.z1r[238])**self.par[224]

    def z1l_13(self):
        self.z1l[13] = self.par[63]*self.z1r[5]*exp(self.z1r[181]-self.z1r[239])**self.par[225]
    # Equation block 77

    def z1l_14(self):
        self.z1l[14] = self.par[80]*self.z1r[10]*exp(self.z1r[182]-self.z1r[240])**self.par[236]

    def z1l_15(self):
        self.z1l[15] = self.par[81]*self.z1r[11]*exp(self.z1r[183]-self.z1r[241])**self.par[237]
    # Equation block 78

    def zel_2(self):
        self.zel[2] = self.par[46]*(self.par[108]*self.z1r[218]+self.par[110]*self.yxr[38]+self.par[112]*self.z1r[180]+self.par[114]*self.z1r[182]-self.par[110]*self.exo[92]-self.par[112]*self.exo[72])+((1-self.par[46])*log(self.par[108]*exp(self.z1r[218])**(1-self.par[244])+self.par[110]*exp(self.yxr[38]-self.exo[92])**(1-self.par[244])+self.par[112]*exp(self.z1r[180]-self.exo[72])**(1-self.par[244])+self.par[114]*exp(self.z1r[182])**(1-self.par[244])))/(1-self.par[244]*(1-self.par[46]))-self.exo[100]

    def zel_3(self):
        self.zel[3] = self.par[47]*(self.par[109]*self.z1r[219]+self.par[111]*self.yxr[39]+self.par[113]*self.z1r[181]+self.par[115]*self.z1r[183]-self.par[111]*self.exo[93]-self.par[113]*self.exo[73])+((1-self.par[47])*log(self.par[109]*exp(self.z1r[219])**(1-self.par[245])+self.par[111]*exp(self.yxr[39]-self.exo[93])**(1-self.par[245])+self.par[113]*exp(self.z1r[181]-self.exo[73])**(1-self.par[245])+self.par[115]*exp(self.z1r[183])**(1-self.par[245])))/(1-self.par[245]*(1-self.par[47]))-self.exo[101]
    # Equation block 79

    def z1l_180(self):
        self.z1l[180] = self.par[26]*(  self.par[62]*self.z1r[238])+((1-self.par[26])*log((  self.par[62]*exp(self.z1r[238])**(1-self.par[224]))))/(1-self.par[224]*(1-self.par[26]))

    def z1l_181(self):
        self.z1l[181] = self.par[27]*(  self.par[63]*self.z1r[239])+((1-self.par[27])*log((  self.par[63]*exp(self.z1r[239])**(1-self.par[225]))))/(1-self.par[225]*(1-self.par[27]))
    # Equation block 80

    def z1l_182(self):
        self.z1l[182] = self.par[38]*(  self.par[80]*self.z1r[240])+((1-self.par[38])*log((  self.par[80]*exp(self.z1r[240])**(1-self.par[236]))))/(1-self.par[236]*(1-self.par[38]))

    def z1l_183(self):
        self.z1l[183] = self.par[39]*(  self.par[81]*self.z1r[241])+((1-self.par[39])*log((  self.par[81]*exp(self.z1r[241])**(1-self.par[237]))))/(1-self.par[237]*(1-self.par[39]))
    # Equation block 81

    def z1l_202(self):
        self.z1l[202] = (self.par[104]/(self.par[104]+self.par[106]))*(  self.par[60]*self.z1r[238])+(self.par[106]/(self.par[104]+self.par[106]))*(  self.par[78]*self.z1r[240])

    def z1l_203(self):
        self.z1l[203] = (self.par[105]/(self.par[105]+self.par[107]))*(  self.par[61]*self.z1r[239])+(self.par[107]/(self.par[105]+self.par[107]))*(  self.par[79]*self.z1r[241])
    # Equation block 82

    def z1l_128(self):
        self.z1l[128] = self.zer[4]+log(self.zer[0])+self.par[142]*self.x1r[20]+self.exo[84]

    def z1l_129(self):
        self.z1l[129] = self.zer[5]+log(self.zer[1])+self.par[143]*self.x1r[21]+self.exo[85]
    # Equation block 83

    def z1l_96(self):
        self.z1l[96] = self.x1r[20]-self.exz[4]+self.zer[4]

    def z1l_97(self):
        self.z1l[97] = self.x1r[21]-self.exz[5]+self.zer[5]
    # Equation block 84

    def z1l_98(self):
        self.z1l[98] = self.z1r[96]+self.exo[56]

    def z1l_99(self):
        self.z1l[99] = self.z1r[97]+self.exo[57]
    # Equation block 85

    def z1l_94(self):
        self.z1l[94] = self.zer[4]-self.yxr[28]

    def z1l_95(self):
        self.z1l[95] = self.zer[5]-self.yxr[29]
    # Equation block 86

    def x1l_24(self):
        self.x1l[24] = self.zer[2]

    def x1l_25(self):
        self.x1l[25] = self.zer[3]
    # Equation block 87

    def x1l_28(self):
        self.x1l[28] = self.zer[4]

    def x1l_29(self):
        self.x1l[29] = self.zer[5]
    # Equation block 88

    def z1l_50(self):
        self.z1l[50] = exp(self.zer[2])*self.z1r[16]+exp(self.z1r[202])*self.z1r[48]+exp(self.z1r[206])*self.z1r[106]+exp(self.zer[4])*self.z1r[274]+(  exp(self.z1r[206])*self.exo[28] +exp(self.z1r[206])*self.exo[29])

    def z1l_51(self):
        self.z1l[51] = exp(self.zer[3])*self.z1r[17]+exp(self.z1r[203])*self.z1r[49]+exp(self.z1r[207])*self.z1r[107]+exp(self.zer[5])*self.z1r[275]+(  exp(self.z1r[207])*self.exo[30] +exp(self.z1r[207])*self.exo[31])
    # Equation block 89

    def z1l_52(self):
        self.z1l[52] = self.z1r[16]+self.z1r[48]+self.z1r[106]+self.z1r[274]+(  self.exo[28] +self.exo[29])

    def z1l_53(self):
        self.z1l[53] = self.z1r[17]+self.z1r[49]+self.z1r[107]+self.z1r[275]+(  self.exo[30] +self.exo[31])
    # Equation block 90

    def z1l_158(self):
        self.z1l[158] = log(self.z1r[50])-log(self.z1r[52])

    def z1l_159(self):
        self.z1l[159] = log(self.z1r[51])-log(self.z1r[53])
    # Equation block 91

    def z1l_58(self):
        self.z1l[58] = self.z1r[52]+(self.exo[42]+self.z1r[112])/exp(self.z1r[246])

    def z1l_59(self):
        self.z1l[59] = self.z1r[53]+(self.exo[43]+self.z1r[113])/exp(self.z1r[247])
    # Equation block 92

    def z1l_18(self):
        self.z1l[18] = self.z1r[274]+(self.exo[42]+self.z1r[86])/exp(self.z1r[246])

    def z1l_19(self):
        self.z1l[19] = self.z1r[275]+(self.exo[43]+self.z1r[87])/exp(self.z1r[247])
    # Equation block 93

    def z1l_20(self):
        self.z1l[20] = self.z1r[276]+self.exo[42]+self.z1r[112]

    def z1l_21(self):
        self.z1l[21] = self.z1r[277]+self.exo[43]+self.z1r[113]
    # Equation block 94

    def z1l_298(self):
        self.z1l[298] = self.yxr[4]+self.z1r[2]/exp(self.z1r[246])+(self.par[154]*exp(self.z1r[128]))/exp(self.zer[4])+self.yjr[10]+self.yjr[4]*self.yxr[10]+self.yjr[6]*self.yxr[12]+(  self.z1r[254] +self.z1r[256])

    def z1l_299(self):
        self.z1l[299] = self.yxr[5]+self.z1r[3]/exp(self.z1r[247])+(self.par[155]*exp(self.z1r[129]))/exp(self.zer[5])+self.yjr[11]+self.yjr[5]*self.yxr[11]+self.yjr[7]*self.yxr[13]+(  self.z1r[255] +self.z1r[257])
    # Equation block 95

    def j1l_10(self):
        self.j1l[10] = (1+self.exo[58]+self.exo[54]+self.z1r[98]-self.par[144])*self.yjr[10]-self.z1r[286]+self.z1r[264]+self.z1r[266]-(exp(self.yxr[38])*(self.z1r[68]+self.z1r[8])+exp(self.z1r[296])*self.exo[14]+(  exp(self.z1r[292])*self.z1r[122] +exp(self.z1r[294])*self.z1r[124]))/exp(self.zer[4])

    def j1l_11(self):
        self.j1l[11] = (1+self.exo[59]+self.exo[55]+self.z1r[99]-self.par[145])*self.yjr[11]-self.z1r[287]+self.z1r[265]+self.z1r[267]-(exp(self.yxr[39])*(self.z1r[69]+self.z1r[9])+exp(self.z1r[297])*self.exo[15]+(  exp(self.z1r[293])*self.z1r[123] +exp(self.z1r[295])*self.z1r[125]))/exp(self.zer[5])
    # Equation block 96

    def z1l_248(self):
        self.z1l[248] = self.z1r[106]*exp(self.z1r[206]-self.zer[4])+self.z1r[20]/exp(self.z1r[246])+self.z1r[22]

    def z1l_249(self):
        self.z1l[249] = self.z1r[107]*exp(self.z1r[207]-self.zer[5])+self.z1r[21]/exp(self.z1r[247])+self.z1r[23]
    # Equation block 97

    def z1l_250(self):
        self.z1l[250] = self.z1r[106]*exp(self.z1r[206]-self.zer[4])+self.z1r[18]+self.z1r[24]

    def z1l_251(self):
        self.z1l[251] = self.z1r[107]*exp(self.z1r[207]-self.zer[5])+self.z1r[19]+self.z1r[25]
    # Equation block 98

    def z1l_252(self):
        self.z1l[252] = self.z1r[106]*exp(self.z1r[206]-self.zer[4])+self.z1r[18]

    def z1l_253(self):
        self.z1l[253] = self.z1r[107]*exp(self.z1r[207]-self.zer[5])+self.z1r[19]
    # Equation block 99

    def z1l_274(self):
        self.z1l[274] = self.z1r[40]-self.z1r[84]

    def z1l_275(self):
        self.z1l[275] = self.z1r[41]-self.z1r[85]
    # Equation block 100

    def z1l_276(self):
        self.z1l[276] = self.z1r[274]*exp(self.z1r[246])

    def z1l_277(self):
        self.z1l[277] = self.z1r[275]*exp(self.z1r[247])
    # Equation block 101

    def x1l_15(self):
        self.x1l[15] = self.z1r[247]-self.zer[5]+self.zer[4]
    # Equation block 102

    def x1l_16(self):
        self.x1l[16] = self.x1r[14]

    def x1l_17(self):
        self.x1l[17] = self.x1r[15]
    # Equation block 103

    def j1l_8(self):
        self.j1l[8] = self.yjr[8]-self.z1r[98]+self.z1r[98]+self.exo[10]

    def j1l_9(self):
        self.j1l[9] = self.yjr[9]-self.z1r[99]+self.z1r[98]+self.exo[11]
    # Equation block 104

    def z1l_246(self):
        self.z1l[246] = self.yjr[8]

    def z1l_247(self):
        self.z1l[247] = self.yjr[9]
    # Equation block 105

    def z1l_136(self):
        self.z1l[136] = (-(  self.par[124]*(self.x1r[14]-self.x1r[14]) +self.par[125]*(self.x1r[15]-self.x1r[14])))

    def z1l_137(self):
        self.z1l[137] = (-(  self.par[126]*(self.x1r[14]-self.x1r[15]) +self.par[127]*(self.x1r[15]-self.x1r[15])))
    # Equation block 106

    def z1l_244(self):
        self.z1l[244] = (-(  self.par[124]*(self.z1r[246]-self.z1r[246]) +self.par[125]*(self.z1r[247]-self.z1r[246])))

    def z1l_245(self):
        self.z1l[245] = (-(  self.par[126]*(self.z1r[246]-self.z1r[247]) +self.par[127]*(self.z1r[247]-self.z1r[247])))
    # Equation block 107

    def z1l_0(self):
        self.z1l[0] = (  self.par[6]*self.z1r[20] +self.par[7]*self.z1r[21])

    def z1l_1(self):
        self.z1l[1] = (  self.par[8]*self.z1r[20] +self.par[9]*self.z1r[21])
    # Equation block 108

    def x1l_0(self):
        self.x1l[0] = self.yxr[0]*(1-self.par[144])+(self.par[10]*self.z1r[0]+self.par[2]*(self.z1r[20]-self.z1r[0]))/exp(self.z1r[246])

    def x1l_1(self):
        self.x1l[1] = self.yxr[1]*(1-self.par[145])+(self.par[11]*self.z1r[1]+self.par[3]*(self.z1r[21]-self.z1r[1]))/exp(self.z1r[246])

    def x1l_2(self):
        self.x1l[2] = self.yxr[2]*(1-self.par[144])+(self.par[12]*self.z1r[0]+self.par[4]*(self.z1r[20]-self.z1r[0]))/exp(self.z1r[247])

    def x1l_3(self):
        self.x1l[3] = self.yxr[3]*(1-self.par[145])+(self.par[13]*self.z1r[1]+self.par[5]*(self.z1r[21]-self.z1r[1]))/exp(self.z1r[247])
    # Equation block 109

    def z1l_2(self):
        self.z1l[2] = (  exp(self.z1r[246])*self.yxr[0] +exp(self.z1r[247])*self.yxr[2])

    def z1l_3(self):
        self.z1l[3] = (  exp(self.z1r[246])*self.yxr[1] +exp(self.z1r[247])*self.yxr[3])
    # Equation block 110

    def z1l_42(self):
        self.z1l[42] = log(self.exz[0])-log(self.zer[0])

    def z1l_43(self):
        self.z1l[43] = log(self.exz[1])-log(self.zer[1])
    # Equation block 111

    def z1l_34(self):
        self.z1l[34] = self.exz[2]-self.zer[2]

    def z1l_35(self):
        self.z1l[35] = self.exz[3]-self.zer[3]
    # Equation block 112

    def z1l_92(self):
        self.z1l[92] = self.zer[2]-self.yxr[24]

    def z1l_93(self):
        self.z1l[93] = self.zer[3]-self.yxr[25]
    # Equation block 113

    def x1l_26(self):
        self.x1l[26] = self.z1r[182]

    def x1l_27(self):
        self.x1l[27] = self.z1r[183]
    # Equation block 114

    def z1l_90(self):
        self.z1l[90] = self.z1r[182]-self.yxr[26]

    def z1l_91(self):
        self.z1l[91] = self.z1r[183]-self.yxr[27]
    # Equation block 115

    def z1l_54(self):
        self.z1l[54] = exp(self.zer[2])*self.z1r[16]+exp(self.zer[4])*self.z1r[48]+exp(self.z1r[206])*self.z1r[106]+(  exp(self.z1r[206])*self.exo[28] +exp(self.z1r[206])*self.exo[29])

    def z1l_55(self):
        self.z1l[55] = exp(self.zer[3])*self.z1r[17]+exp(self.zer[5])*self.z1r[49]+exp(self.z1r[207])*self.z1r[107]+(  exp(self.z1r[207])*self.exo[30] +exp(self.z1r[207])*self.exo[31])
    # Equation block 116

    def z1l_56(self):
        self.z1l[56] = self.z1r[16]+self.z1r[48]+self.z1r[106]+(  self.exo[28] +self.exo[29])

    def z1l_57(self):
        self.z1l[57] = self.z1r[17]+self.z1r[49]+self.z1r[107]+(  self.exo[30] +self.exo[31])
    # Equation block 117

    def x1l_20(self):
        self.x1l[20] = self.par[190]*self.yxr[18]+self.par[188]*(self.x1r[14]-self.yxr[16]-self.exo[12])+self.par[158]*(self.z1r[92]-self.exo[26])+self.par[172]*(self.z1r[94]-self.exo[26])+self.par[174]*(self.z1r[90]-self.exo[26])+self.par[176]*(self.zer[2]-self.exo[48])+self.par[178]*(self.zer[4]-self.exo[48])+self.par[180]*(self.yxr[38]-self.exo[48])+self.par[182]*0+self.par[184]*(log(self.zer[0])-log(self.yxr[22])-self.exo[64])+self.par[186]*(log(self.zer[0])-log(self.yxr[22])-self.exo[64]+self.z1r[94]-self.exo[26])+self.par[160]*(log(self.z1r[50])-self.exo[64])+self.par[162]*(log(self.zer[0])+self.zer[4])+self.par[164]*log((self.zer[0]-self.z1r[274])*exp(self.zer[4]))+self.par[166]*(self.z1r[34]-self.exo[26])+self.par[168]*(self.z1r[42]-self.exo[64])+self.par[170]*(log(self.z1r[54])-self.exo[64])

    def x1l_21(self):
        self.x1l[21] = self.par[191]*self.yxr[19]+self.par[189]*(self.x1r[15]-self.yxr[17]-self.exo[13])+self.par[159]*(self.z1r[93]-self.exo[27])+self.par[173]*(self.z1r[95]-self.exo[27])+self.par[175]*(self.z1r[91]-self.exo[27])+self.par[177]*(self.zer[3]-self.exo[49])+self.par[179]*(self.zer[5]-self.exo[49])+self.par[181]*(self.yxr[39]-self.exo[49])+self.par[183]*0+self.par[185]*(log(self.zer[1])-log(self.yxr[23])-self.exo[65])+self.par[187]*(log(self.zer[1])-log(self.yxr[23])-self.exo[65]+self.z1r[95]-self.exo[27])+self.par[161]*(log(self.z1r[51])-self.exo[65])+self.par[163]*(log(self.zer[1])+self.zer[5])+self.par[165]*log((self.zer[1]-self.z1r[275])*exp(self.zer[5]))+self.par[167]*(self.z1r[35]-self.exo[27])+self.par[169]*(self.z1r[43]-self.exo[65])+self.par[171]*(log(self.z1r[55])-self.exo[65])
    # Equation block 118

    def x1l_18(self):
        self.x1l[18] = self.x1r[20]

    def x1l_19(self):
        self.x1l[19] = self.x1r[21]
    # Equation block 119

    def z1l_44(self):
        self.z1l[44] = (self.par[60]*(self.par[104]/(self.par[104]+self.par[106]))*self.exo[16]*exp(self.z1r[202]))/exp(self.z1r[238])

    def z1l_45(self):
        self.z1l[45] = (self.par[61]*(self.par[105]/(self.par[105]+self.par[107]))*self.exo[17]*exp(self.z1r[203]))/exp(self.z1r[239])
    # Equation block 120

    def z1l_46(self):
        self.z1l[46] = (self.par[78]*(self.par[106]/(self.par[104]+self.par[106]))*self.exo[16]*exp(self.z1r[202]))/exp(self.z1r[240])

    def z1l_47(self):
        self.z1l[47] = (self.par[79]*(self.par[107]/(self.par[105]+self.par[107]))*self.exo[17]*exp(self.z1r[203]))/exp(self.z1r[241])
    # Equation block 121

    def z1l_48(self):
        self.z1l[48] = (  self.z1r[44]*exp(self.z1r[238]) +self.z1r[46]*exp(self.z1r[240]))/exp(self.z1r[202])

    def z1l_49(self):
        self.z1l[49] = (  self.z1r[45]*exp(self.z1r[239]) +self.z1r[47]*exp(self.z1r[241]))/exp(self.z1r[203])
    # Equation block 122

    def z1l_60(self):
        self.z1l[60] = self.z1r[48]+self.exo[14]*exp(self.z1r[296]-self.zer[4])

    def z1l_61(self):
        self.z1l[61] = self.z1r[49]+self.exo[15]*exp(self.z1r[297]-self.zer[5])
    # Equation block 123

    def z1l_286(self):
        self.z1l[286] = self.exo[138]+self.par[250]*self.zer[0]

    def z1l_287(self):
        self.z1l[287] = self.exo[139]+self.par[251]*self.zer[1]
    # Equation block 124

    def z1l_288(self):
        self.z1l[288] = (  (self.exo[118]*self.par[192]+self.exo[114]*self.par[138])*exp(self.z1r[160])*self.z1r[72] +(self.exo[119]*self.par[193]+self.exo[114]*self.par[139])*exp(self.z1r[161])*self.z1r[73])/exp(self.zer[4])

    def z1l_290(self):
        self.z1l[290] = (  (self.exo[122]*self.par[192]+self.exo[116]*self.par[138])*exp(self.z1r[164])*self.z1r[76] +(self.exo[123]*self.par[193]+self.exo[116]*self.par[139])*exp(self.z1r[165])*self.z1r[77])/exp(self.zer[4])

    def z1l_289(self):
        self.z1l[289] = (  (self.exo[120]*self.par[194]+self.exo[115]*self.par[140])*exp(self.z1r[162])*self.z1r[74] +(self.exo[121]*self.par[195]+self.exo[115]*self.par[141])*exp(self.z1r[163])*self.z1r[75])/exp(self.zer[5])

    def z1l_291(self):
        self.z1l[291] = (  (self.exo[124]*self.par[194]+self.exo[117]*self.par[140])*exp(self.z1r[166])*self.z1r[78] +(self.exo[125]*self.par[195]+self.exo[117]*self.par[141])*exp(self.z1r[167])*self.z1r[79])/exp(self.zer[5])
    # Equation block 125

    def z1l_268(self):
        self.z1l[268] = (  self.z1r[288] +self.z1r[290])

    def z1l_269(self):
        self.z1l[269] = (  self.z1r[289] +self.z1r[291])
    # Equation block 126

    def z1l_272(self):
        self.z1l[272] = (  self.exo[110]*exp(self.z1r[226])*self.z1r[36] +self.exo[112]*exp(self.z1r[228])*self.z1r[38])/exp(self.zer[4])

    def z1l_273(self):
        self.z1l[273] = (  self.exo[111]*exp(self.z1r[227])*self.z1r[37] +self.exo[113]*exp(self.z1r[229])*self.z1r[39])/exp(self.zer[5])
    # Equation block 127

    def z1l_264(self):
        self.z1l[264] = (self.exo[126]*(exp(self.yxr[38])*(self.z1r[68]+self.z1r[8])+exp(self.z1r[296])*self.exo[14]+(  exp(self.z1r[292])*self.z1r[122] +exp(self.z1r[294])*self.z1r[124]))-self.exo[132]*exp(self.z1r[206])*self.z1r[110])/exp(self.zer[4])

    def z1l_265(self):
        self.z1l[265] = (self.exo[127]*(exp(self.yxr[39])*(self.z1r[69]+self.z1r[9])+exp(self.z1r[297])*self.exo[15]+(  exp(self.z1r[293])*self.z1r[123] +exp(self.z1r[295])*self.z1r[125]))-self.exo[133]*exp(self.z1r[207])*self.z1r[111])/exp(self.zer[5])
    # Equation block 128

    def x1l_4(self):
        self.x1l[4] = self.z1r[22]+self.yxr[4]*(1-self.par[144])-self.exo[40]

    def x1l_5(self):
        self.x1l[5] = self.z1r[23]+self.yxr[5]*(1-self.par[145])-self.exo[41]
    # Equation block 129

    def z1l_266(self):
        self.z1l[266] = self.z1r[98]*self.yxr[4]+self.exo[106]

    def z1l_267(self):
        self.z1l[267] = self.z1r[99]*self.yxr[5]+self.exo[107]
    # Equation block 130

    def z1l_270(self):
        self.z1l[270] = self.z1r[260]+self.z1r[264]+self.z1r[266]+self.z1r[268]+self.z1r[272]+self.z1r[262]

    def z1l_271(self):
        self.z1l[271] = self.z1r[261]+self.z1r[265]+self.z1r[267]+self.z1r[269]+self.z1r[273]+self.z1r[263]
    # Equation block 131

    def z1l_22(self):
        self.z1l[22] = self.z1r[60]+self.z1r[286]-self.z1r[270]+self.z1r[98]*self.yxr[4]

    def z1l_23(self):
        self.z1l[23] = self.z1r[61]+self.z1r[287]-self.z1r[271]+self.z1r[99]*self.yxr[5]
    # Equation block 132

    def z1l_24(self):
        self.z1l[24] = self.z1r[22]+(self.x1r[20]-self.z1r[98])*self.yxr[4]

    def z1l_25(self):
        self.z1l[25] = self.z1r[23]+(self.x1r[21]-self.z1r[99])*self.yxr[5]
    # Equation block 133

    def z1l_230(self):
        self.z1l[230] = log(exp(self.z1r[226])*(1+self.exo[102])+self.exo[140])

    def z1l_232(self):
        self.z1l[232] = log(exp(self.z1r[226])*(1+self.exo[102])+self.exo[142])

    def z1l_231(self):
        self.z1l[231] = log(exp(self.z1r[227])*(1+self.exo[103])+self.exo[141])

    def z1l_233(self):
        self.z1l[233] = log(exp(self.z1r[227])*(1+self.exo[103])+self.exo[143])
    # Equation block 134

    def z1l_26(self):
        self.z1l[26] = self.par[56]*self.z1r[30]*exp(self.z1r[188]-self.z1r[230])**self.par[220]

    def z1l_28(self):
        self.z1l[28] = self.par[57]*self.z1r[32]*exp(self.z1r[190]-self.z1r[232])**self.par[222]

    def z1l_27(self):
        self.z1l[27] = self.par[58]*self.z1r[31]*exp(self.z1r[189]-self.z1r[231])**self.par[221]

    def z1l_29(self):
        self.z1l[29] = self.par[59]*self.z1r[33]*exp(self.z1r[191]-self.z1r[233])**self.par[223]
    # Equation block 135

    def z1l_138(self):
        self.z1l[138] = self.par[74]*self.z1r[142]*exp(self.z1r[176]-self.z1r[240])**self.par[232]

    def z1l_140(self):
        self.z1l[140] = self.par[75]*self.z1r[144]*exp(self.z1r[178]-self.z1r[240])**self.par[234]

    def z1l_139(self):
        self.z1l[139] = self.par[76]*self.z1r[143]*exp(self.z1r[177]-self.z1r[241])**self.par[233]

    def z1l_141(self):
        self.z1l[141] = self.par[77]*self.z1r[145]*exp(self.z1r[179]-self.z1r[241])**self.par[235]
    # Equation block 136

    def z1l_188(self):
        self.z1l[188] = self.par[22]*(  self.par[56]*self.z1r[230])+((1-self.par[22])*log((  self.par[56]*exp(self.z1r[230])**(1-self.par[220]))))/(1-self.par[220]*(1-self.par[22]))

    def z1l_190(self):
        self.z1l[190] = self.par[24]*(  self.par[57]*self.z1r[232])+((1-self.par[24])*log((  self.par[57]*exp(self.z1r[232])**(1-self.par[222]))))/(1-self.par[222]*(1-self.par[24]))

    def z1l_189(self):
        self.z1l[189] = self.par[23]*(  self.par[58]*self.z1r[231])+((1-self.par[23])*log((  self.par[58]*exp(self.z1r[231])**(1-self.par[221]))))/(1-self.par[221]*(1-self.par[23]))

    def z1l_191(self):
        self.z1l[191] = self.par[25]*(  self.par[59]*self.z1r[233])+((1-self.par[25])*log((  self.par[59]*exp(self.z1r[233])**(1-self.par[223]))))/(1-self.par[223]*(1-self.par[25]))
    # Equation block 137

    def z1l_176(self):
        self.z1l[176] = self.par[34]*(  self.par[74]*self.z1r[240])+((1-self.par[34])*log((  self.par[74]*exp(self.z1r[240])**(1-self.par[232]))))/(1-self.par[232]*(1-self.par[34]))

    def z1l_178(self):
        self.z1l[178] = self.par[36]*(  self.par[75]*self.z1r[240])+((1-self.par[36])*log((  self.par[75]*exp(self.z1r[240])**(1-self.par[234]))))/(1-self.par[234]*(1-self.par[36]))

    def z1l_177(self):
        self.z1l[177] = self.par[35]*(  self.par[76]*self.z1r[241])+((1-self.par[35])*log((  self.par[76]*exp(self.z1r[241])**(1-self.par[233]))))/(1-self.par[233]*(1-self.par[35]))

    def z1l_179(self):
        self.z1l[179] = self.par[37]*(  self.par[77]*self.z1r[241])+((1-self.par[37])*log((  self.par[77]*exp(self.z1r[241])**(1-self.par[235]))))/(1-self.par[235]*(1-self.par[37]))
    # Equation block 138

    def z1l_262(self):
        self.z1l[262] = self.exo[66]

    def z1l_263(self):
        self.z1l[263] = self.exo[67]
    # Equation block 139

    def z1l_260(self):
        self.z1l[260] = self.exo[108]*((  self.z1r[192] +self.z1r[194])+self.z1r[198])+((  self.exo[102]*exp(self.z1r[184])*self.z1r[146] +self.exo[104]*exp(self.z1r[186])*self.z1r[148])+(  self.exo[102]*exp(self.z1r[172])*self.z1r[80] +self.exo[104]*exp(self.z1r[174])*self.z1r[82])-(  self.exo[128]*exp(self.z1r[206])*self.z1r[100] +self.exo[130]*exp(self.z1r[206])*self.z1r[102])-(  self.exo[102]*exp(self.z1r[226])*self.z1r[36] +self.exo[104]*exp(self.z1r[228])*self.z1r[38]))/exp(self.zer[4])

    def z1l_261(self):
        self.z1l[261] = self.exo[109]*((  self.z1r[193] +self.z1r[195])+self.z1r[199])+((  self.exo[103]*exp(self.z1r[185])*self.z1r[147] +self.exo[105]*exp(self.z1r[187])*self.z1r[149])+(  self.exo[103]*exp(self.z1r[173])*self.z1r[81] +self.exo[105]*exp(self.z1r[175])*self.z1r[83])-(  self.exo[129]*exp(self.z1r[207])*self.z1r[101] +self.exo[131]*exp(self.z1r[207])*self.z1r[103])-(  self.exo[103]*exp(self.z1r[227])*self.z1r[37] +self.exo[105]*exp(self.z1r[229])*self.z1r[39]))/exp(self.zer[5])

# End of G-cubed equations class declaration

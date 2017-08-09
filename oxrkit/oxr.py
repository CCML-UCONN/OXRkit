#!/usr/bin/env python
import numpy as np
import os

T=300
beta=0.02585/300*T*2.3025850929940459

tze_oh=0.41
tze_o=0.05
tze_ooh=0.46
sl=1.0
ins=3.2
class OXR:
    def __init__(self,mdict, PH=0,U=0):
        self.ebo=mdict['ebo']
        self.eboh=mdict['eboh']
        self.scaling=mdict['scaling']
        try:
            self.ebooh=mdict['ebooh']
        except KeyError:
            print "no key for ebooh, using scaling "
            self.ebooh = sl * self.eboh + ins
        self.PH=PH
        self.U=U
        self.rdgs=[None]*4
        self.gads={'bare':0.0,
                    'OH':None,
                    'O':None,
                    'OOH':None}
        self.ads=None
        self.get_dg()

    def get_dg(self):
        #dg[] is for OER: H2O->OH->O->OOH->O2
        ebo=self.ebo
        eboh=self.eboh
        ebooh=self.ebooh
        ph=self.PH
        u=self.U
        
        if self.scaling or ebooh==None:
            ebooh=sl*eboh+ins

        self.gads['O']=ebo + tze_o - 2* ( u + beta* ph)
        self.gads['OH']=eboh + tze_oh -  ( u + beta* ph)
        #print ebooh, eboh,ebo
        self.gads['OOH']=ebooh + tze_ooh - 3* ( u + beta* ph)

        self.rdgs[0]= self.gads['OH']
        self.rdgs[1]= self.gads['O'] - self.gads['OH']
        self.rdgs[2]= self.gads['OOH'] - self.gads['O']
        self.rdgs[3]= 4*(1.23 -(u + beta*ph)) - self.gads['OOH']

    def get_op_oer(self):
        #self.get_dg()
        op_oer=max(self.rdgs)-1.23
        return op_oer

    def get_op_orr(self):
        #self.get_dg()
        op_orr=1.23-min(self.rdgs)
        return op_orr

    
    def get_ads(self):
        #self.get_dg()
        self.ads=min(self.gads.items(), key=lambda x: x[1])[0]
        #print "ads: "+str(self.ads)
        return self.ads

    def get_gads(self):
        return self.gads

    def get_rdgs(self):
        return self.rdgs
#test=OXR(1.76,0.41)
#print test.rdg, test.get_ads()

"""
ophyd commands from SPEC config file

CAUTION: Review the object names below before using them!
    Some names may not be valid python identifiers
    or may be reserved (such as ``time`` or ``del``)
    or may be vulnerable to re-definition because
    they are short or common.
"""

__all__ = """
    satop
    saboy
    sain
    saout
    energy
    detv
    detz
    gonv
    gonh
    bpmh
    bayv
    robz
	robh
	subot
	sutop
	suin
	suout
	mtheta
	mtwin
	mfocus
	mchi
	mnorm
	mpar
	momega
	mtwist
	bsv
	bsz
	deth
	cryov
	sec
	mon
	det
	c3
	c4
	c5
	c6
	c7
	c8
	c9
""".split()


from ophyd import EpicsMotor, EpicsSignal
from ophyd.scaler import ScalerCH

#-----------------------------------------------------------------------
# Motors - previously defined in EPICS
#-----------------------------------------------------------------------


satop = EpicsMotor('17bm:m1', name='satop', labels=('motor',))  # SlitATop
saboy = EpicsMotor('17bm:m2', name='saboy', labels=('motor',))  # SlitABot
sain = EpicsMotor('17bm:m3', name='sain', labels=('motor',))  # SlitAIn   
saout = EpicsMotor('17bm:m4', name='saout', labels=('motor',))  # SlitAOut
energy = EpicsMotor('17bm:pm1', name='energy', labels=('motor',))
detv = EpicsMotor('17bm:m25', name='detv', labels=('motor',))
detz = EpicsMotor('17bm:m75', name='detz', labels=('motor',))
gonv = EpicsMotor('17bm:m13', name='gonv', labels=('motor',))
gonh = EpicsMotor('17bm:m14', name='gonh', labels=('motor',))
bpmh = EpicsMotor('17bm:m15', name='bpmh', labels=('motor',))
bayv = EpicsMotor('17bm:m16', name='bayv', labels=('motor',))  # SamplBayV

robz = EpicsMotor('17bm:m19', name='robz', labels=('motor',))  # RobotZ
robh = EpicsMotor('17bm:m27', name='robh', labels=('motor',))  # RobotH
subot = EpicsMotor('17bm:m33', name='subot', labels=('motor',))  # SlitUpBot
sutop = EpicsMotor('17bm:m34', name='sutop', labels=('motor',))  # SlitUpTop
suin = EpicsMotor('17bm:m35', name='suin', labels=('motor',))  # SlitUpIn
suout = EpicsMotor('17bm:m36', name='suout', labels=('motor',))  # SlitUpOut

sdbot = EpicsMotor('17bm:m41', name='sdbot', labels=('motor',))  # SlitDownBot
sdtop = EpicsMotor('17bm:m42', name='sdtop', labels=('motor',))  # SlitDownTop
sdin = EpicsMotor('17bm:m43', name='sdin', labels=('motor',))  # SlitDownIn
sdout = EpicsMotor('17bm:m44', name='sdout', labels=('motor',))  # SlitDownOut

mtheta = EpicsMotor('17bm:m77', name='mtheta', labels=('motor',))  # MonoTheta
mtwout = EpicsMotor('17bm:m78', name='mtwout', labels=('motor',))  # MonTwstOut
mtwin = EpicsMotor('17bm:m79', name='mtwin', labels=('motor',))  # MonTwstIn
mfocus = EpicsMotor('17bm:m80', name='mfocus', labels=('motor',))  # MonoFocus
mchi = EpicsMotor('17bm:m82', name='mchi', labels=('motor',))  # MonoChi
mnorm = EpicsMotor('17bm:m83', name='mnorm', labels=('motor',))  # MonoNormal
mpar = EpicsMotor('17bm:m84', name='mpar', labels=('motor',))  # MonoParal
momega = EpicsMotor('17bm:pm10', name='momega', labels=('motor',))  # MonoOmega
mtwist = EpicsMotor('17bm:pm11', name='mtwist', labels=('motor',))  # MonoTwist
bsh = EpicsMotor('17bm:m22', name='bsh', labels=('motor',))  # BeamStopH
bsv = EpicsMotor('17bm:m21', name='bsv', labels=('motor',))  # BeamStopV
bsz = EpicsMotor('17bm:m20', name='bsz', labels=('motor',))  # BeamStopZ

deth = EpicsMotor('17bm:m23', name='deth', labels=('motor',))  # XrayCamStg
cryov = EpicsMotor('17bm:m24', name='cryov', labels=('motor',))  # CryoVV

#-----------------------------------------------------------------------
# Motors - previously defined in EPICS, in SPEC were EPICS_M1 instead of
#          the usual EPICS_M2; comment before each EpicMotor call is the
#          original SPEC definition  
#-----------------------------------------------------------------------


# 7: MOT007 = EPICS_M1:0/10    640 -1  4000  200  -50  125    0 0x003     samh  samh
samh = EpicsMotor('17bm:m10', name='samh', labels=('motor',))  # samh

# 8: MOT008 = EPICS_M1:0/11    640 -1  4000  200  -50  125    0 0x003     samv  samv
samv = EpicsMotor('17bm:m11', name='samv', labels=('motor',))  # samv

# 9: MOT009 = EPICS_M1:0/12   1600  1  4000  200   50  125    0 0x003     samr  samr
samhr = EpicsMotor('17bm:m12', name='samr', labels=('motor',))  # samr

# 14: MOT014 = EPICS_M1:0/17   1600 -1  2000  200   50  200    0 0x003     pinh  pinh
pinh = EpicsMotor('17bm:m17', name='pinh', labels=('motor',))  # pinh

# 15: MOT015 = EPICS_M1:0/18   1600 -1  2000  200   50  200    0 0x003     pinv  pinv
pinv = EpicsMotor('17bm:m18', name='pinv', labels=('motor',))  # pinv

#-----------------------------------------------------------------------
# Motors - previously defined as SPEC macros
#-----------------------------------------------------------------------


# Macro Motor: SpecMotor(mne='suvgap', config_line='22', name='SlitUpVGap', macro_prefix='slit')  # SlitUpVGap # misc_par_2=18
# Macro Motor: SpecMotor(mne='suvpos', config_line='23', name='SlitUpVCtr', macro_prefix='slit')  # SlitUpVCtr # misc_par_2=18
# Macro Motor: SpecMotor(mne='suhgap', config_line='24', name='SlitUpHGap', macro_prefix='slit')  # SlitUpHGap # misc_par_2=20
# Macro Motor: SpecMotor(mne='suhpos', config_line='25', name='SlitUpHCtr', macro_prefix='slit')  # SlitUpHCtr # misc_par_2=20

# Macro Motor: SpecMotor(mne='sdvgap', config_line='47', name='SlDVgap', macro_prefix='slit')  # SlDVgap # misc_par_2=26
# Macro Motor: SpecMotor(mne='sdvpos', config_line='48', name='SlDVpos', macro_prefix='slit')  # SlDVpos # misc_par_2=26
# Macro Motor: SpecMotor(mne='sdhgap', config_line='49', name='SlDHgap', macro_prefix='slit')  # SlDHgap # misc_par_2=28
# Macro Motor: SpecMotor(mne='sdhpos', config_line='50', name='SlDHpos', macro_prefix='slit')  # SlDHpos # misc_par_2=28
# Macro Motor: SpecMotor(mne='m78', config_line='78', name='Motor 78', macro_prefix='junk')  # Motor 78

# The following were in SPEC but as of 2021.07.29, no longer in use
# Macro Motor: SpecMotor(mne='fmjht', config_line='33', name='FocMJkV', macro_prefix='bm17mirr')  # FocMJkV
# Macro Motor: SpecMotor(mne='fmjtlt', config_line='34', name='FocMJkPitch', macro_prefix='bm17mirr')  # FocMJkPitch


#-----------------------------------------------------------------------
# Motors - previously controlled directly in SPEC; controller(s) at 
#          10.40.30.60 and 10.40.30.61 on beamline's "SPEC" network.
#          controller:  Step-Pak SPI-MAXnet-8000 8-Axis Ethernet
#          Indexer/Controller
#-----------------------------------------------------------------------


# 90: MOT090 =     OMS:0/0     40  1  2000  200   50  125    0 0x003    utabv  UpStrTablV  # UpStrTablV
# 91: MOT091 =     OMS:0/1     40  1  2000  200   50  125    0 0x003   drtabv  DnRStrTablV  # DnRStrTablV
# 92: MOT092 =     OMS:0/2     40  1  2000  200   50  125    0 0x003   dltabv  DnLStrTablV  # DnLStrTablV
# 93: MOT093 =     OMS:0/3    310  1  2000  200   50  125    0 0x003    utabh  UpStrTabH  # UpStrTabH
# 94: MOT094 =     OMS:0/4    310  1  2000  200   50  125    0 0x003    dtabh  DnStrTablH  # DnStrTablH
# 95: MOT095 =     OMS:1/1    200  1  1000  200   50  125    0 0x003  nmtheta  NMTheta  # NMTheta
# 96: MOT096 =     OMS:0/6    302  1  2500  200   50  125    0 0x003  nmpitch  NMThetAdj  # NMThetAdj
# 97: MOT097 =     OMS:0/5    302  1  2500  200   50  125    0 0x003    nmchi  NMChi  # NMChi
# 98: MOT098 =     OMS:0/7    302  1  2500  200   50  125    0 0x003   nmbend  NMBent  # NMBent
# 99: MOT099 =     OMS:1/0    400  1  2500  200   50  125    0 0x003  nmtwist  NMTwist  # NMTwist


#-----------------------------------------------------------------------
# Scalers/Counters
#-----------------------------------------------------------------------

scaler2 = ScalerCH('17bm:scaler2', name='scaler2', labels=('detectors',))
scaler2.select_channels(None)
sec = scaler2.channels.chan01.s
mon = scaler2.channels.chan02.s
det = scaler2.channels.chan03.s
c3 = scaler2.channels.chan04.s
c4 = scaler2.channels.chan05.s
c5 = scaler2.channels.chan06.s
c6 = scaler2.channels.chan07.s
c7 = scaler2.channels.chan08.s
c8 = scaler2.channels.chan09.s
c9 = scaler2.channels.chan10.s
# counter: c10 = SpecCounter(mne='c10', config_line='10', name='Counter 10', unit='0', chan='0', pvname=None)
# counter: c11 = SpecCounter(mne='c11', config_line='11', name='BPM', unit='0', chan='1', pvname=None)
# counter: c12 = SpecCounter(mne='c12', config_line='12', name='Counter 12', unit='0', chan='2', pvname=None)
# counter: c13 = SpecCounter(mne='c13', config_line='13', name='Counter 13', unit='0', chan='3', pvname=None)
# counter: c14 = SpecCounter(mne='c14', config_line='14', name='Counter 14', unit='0', chan='4', pvname=None)
# 15: CNT015 =     NONE  2  5      1 0x000      c15  Counter 15
# 16: CNT016 =     NONE  2  6      1 0x000      c16  Counter 16
# 17: CNT017 =     NONE  2  7      1 0x000      c17  Counter 17
# 18: CNT018 =     NONE  3  8      1 0x000      c18  Counter 18
# 19: CNT019 =     NONE  3  9      1 0x000      c19  Counter 19

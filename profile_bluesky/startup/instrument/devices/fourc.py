"""
ophyd commands from SPEC config file

file: /tmp/spec/fourc/config

CAUTION: Review the object names below before using them!
    Some names may not be valid python identifiers
    or may be reserved (such as ``time`` or ``del``)
    or may be vulnerable to re-definition because
    they are short or common.
"""

from ophyd import EpicsMotor, EpicsSignal
from ophyd.scaler import ScalerCH

# 0: MOT000 =    NONE   2000  1  2000  200   50  125    0 0x003      tth  Two Theta  # Two Theta
# 1: MOT001 =    NONE   2000  1  2000  200   50  125    0 0x003       th  Theta  # Theta
# 2: MOT002 =    NONE   2000  1  2000  200   50  125    0 0x003      chi  Chi  # Chi
# 3: MOT003 =    NONE   2000  1  2000  200   50  125    0 0x003      phi  Phi  # Phi
# counter: sec = SpecCounter(mne='sec', config_line='0', name='Seconds', unit='0', chan='0', pvname=None)
# 1: CNT001 =     NONE  0  1      1 0x002      mon  Monitor
# 2: CNT002 =     NONE  0  2      1 0x000      det  Detector

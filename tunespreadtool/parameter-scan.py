from os import system as ex
from itertools import product
import numpy as np

def go_through_scan(twiss_files, scan, lshape):
    params = scan.keys()
    combinations = [ dict( zip(params, joined) ) for joined in product(
                                            *(scan[p] for p in params) ) ]
    labels = ' --labels '
    for actualsetting in combinations:
        flags = ''
        for param, value in actualsetting.iteritems():
            flags += ' --' + param + ' ' + str(value)
        ex('python tunespread.py ' + ' '.join(twiss_files) + labels + 
                                               flags + ' --lshape ' + str(lshape))
        labels = ''

# === PSB ===
print "\nPSB:"

# fixed parameters
twiss_files = ['PSB-inj50MeV.tfs']
scan = {                # comment out what you do not want to fix 
                        # (and instead read from file) :
        'n_part': [29.55e+11, 25.55e+11],
        'emit_norm_tr': [1.71e-6, 1.5e-6],
        'Ekin': [0.16],
        'bunch_length': [650],
        'deltap': [1.8e-3]
        }

go_through_scan(twiss_files, scan, np.sqrt(2*np.pi)*.35)

# === PS ===
print "PS:"

# fixed parameters
twiss_files = ['PS-inj2GeV-s.tfs', 'PS-inj2GeV-data.tfs']
scan = {                # comment out what you do not want to fix 
                        # (and instead read from file) :
        'n_part': [14.04e+11],
        'emit_norm_tr': [1.1e-6],
        'Ekin': [2],
        'bunch_length': [140],
        'deltap': [1.2e-3]
        }

go_through_scan(twiss_files, scan, 1.0)

# === SPS ===
print "\nSPS:"

# fixed parameters
twiss_files = ['SPS-inj25GeV.tfs']
scan = {                # comment out what you do not want to fix 
                        # (and instead read from file) :
        'n_part': [2.22e+11],
        'emit_norm_tr': [1.16e-6],
        #'Ekin': [25],
        'bunch_length': [3],
        'deltap': [1.7e-3]
        }

go_through_scan(twiss_files, scan, 1.0)

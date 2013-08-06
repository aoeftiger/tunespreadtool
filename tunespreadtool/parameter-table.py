import numpy as np
from os import system as ex

def go_through_table(twiss_files, table, lshape):
    labels = ' --labels '
    for actualsetting in table[1:]:
        flags = ''
        for i in xrange(len(table[0])):
            flags += ' --' + table[0][i] + ' ' + str(actualsetting[i])
        ex('python tunespread.py ' + ' '.join(twiss_files) + labels + 
                                               flags + ' --lshape ' + str(lshape))
        labels = ''

# === PSB ===
print "\nPSB:"

# fixed parameters
twiss_files = ['PSB-inj50MeV.tfs']
table = [ ['n_part', 'emit_norm_tr', 'Ekin', 'bunch_length', 'deltap'],
          [28.07e+11, 1.8e-6, 2, 180, 1.2e-3]
        ]

go_through_table(twiss_files, table, np.sqrt(2*np.pi)*.35)

# === PS ===
print "PS:"

# fixed parameters
twiss_files = ['PS-inj2GeV-s.tfs', 'PS-inj2GeV-data.tfs']
table = [ ['n_part', 'emit_norm_tr', 'Ekin', 'bunch_length', 'deltap'],
          [28.07e+11, 1.8e-6, 2, 180, 1.2e-3],
          [29.07e+11, 1.8e-6, 2, 180, 1.2e-3]
        ]

go_through_table(twiss_files, table, 1.0)

# === SPS ===
print "\nSPS:"

# fixed parameters
twiss_files = ['SPS-inj25GeV.tfs']
table = [ ['n_part', 'emit_norm_tr', 'Ekin', 'bunch_length', 'deltap'],
          [28.07e+11, 1.8e-6, 2, 180, 1.2e-3]
        ]

go_through_table(twiss_files, table, 1.0)

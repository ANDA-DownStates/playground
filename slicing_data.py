# -*- coding: utf-8 -*-
"""
Cuts out the waiting period from our data and adds the reaction time (RT)
"""

import neo
import quantities as pq
import numpy as np
import useful_tools as ut
     
path        = '../data/'
resultpath  = '../data_resliced/'

data_idx = 0    # select dataset


block = np.load(path + 'data{}.npy'.format(data_idx), encoding='latin1').item()

block_sliced = neo.Block()

for idx, trial in enumerate(block.segments):  # for each trial
        
    # Find the index of our event in the event substructure
    on_num      = trial.events[0].annotations['trial_event_labels'].index(b'CUE-OFF')
    off_num     = trial.events[0].annotations['trial_event_labels'].index(b'GO-ON')
    
    # Find the associated times
    on_time     = trial.events[0].annotations['signal'][on_num]
    off_time    = trial.events[0].annotations['signal'][off_num]
    
    # Reslice the existing spiketrains, put them into a new neo.Segment
    seg_sliced  = neo.Segment()
    for idx_s, spike in enumerate(trial.spiketrains):
        seg_sliced.spiketrains.append(spike.time_slice(on_time, off_time))

    # ... and stuff the result into our new block
    block_sliced.segments.append(seg_sliced)
    block_sliced.segments[-1].annotations           = trial.annotations
    block_sliced.segments[-1].annotations['RT']     = trial.events[0].annotations['signal'][trial.events[0].annotations['trial_event_labels'].index(b'GO-ON')] - trial.events[0].annotations['signal'][trial.events[0].annotations['trial_event_labels'].index(b'CUE-OFF')]
    
ut.add_channel_and_units_v2(block_sliced)

np.save(resultpath + 'data_resliced{}.npy'.format(data_idx), block_sliced)

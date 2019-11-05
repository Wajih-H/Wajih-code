"""
    Send passive jobs to frioul using frioul_batch command.


    /hpc/soft/anaconda3/bin/python /hpc/banco/hermi.w/scripts/frioul_batch_msm.py
"""

import pandas
import os.path as op
import os
import numpy as np
import shutil
import subprocess
import datetime as dt


def MSM_on_frioul(tgt_sub, src_sub, h, lvl, smth, conf_f, log_dir):
    """ Create a new job on frioul that run MSMessai.sh """
    # Get current date and time
    d = dt.datetime.now()
    d_str = d.strftime("%Y%m%d_%H%M%S")

    conf_name = op.split(conf_f)[1]

    outdir = "dataMSM/MSM_beta/MSM_SameTransform_PCA/{}to{}_{}_lvl-{}_s-{}_cnf-{}".format(src_sub, tgt_sub, h, lvl, smth, conf_name)
    outemplate_fname = "{}to{}_{}_lvl-{}_s-{}_cnf-{}.".format(src_sub, tgt_sub, h, lvl, smth, conf_name)

    # Shell command that will be run on the frioul's node (in the passive job)
    cmd = "/hpc/banco/hermi.w/scripts/MSMessai.sh {} {} {} {} {} {} {} {}".format(src_sub, tgt_sub, h, lvl, smth, conf_f, outdir, outemplate_fname)
        
    # Template for log filenames (stdout, stderr, stdcmd)
    std = log_dir + "/{}_%jobid%_msm_{}to{}_{}_lvl-{}_s-{}_cnf-{}.".format(d_str, src_sub, tgt_sub, h, lvl, smth, conf_name)

    # Frioul_batch command (run on the head of frioul)
    fb_cmd = "mkdir {} -p; frioul_batch \"{}\"  -C {}cmd -O {}out -E {}err".format(log_dir, cmd, std, std, std)

    # Print and execute
    print(fb_cmd)
    subprocess.run(fb_cmd, shell=True)


def main():
    """ Launch many MSM jobs on frioul testing all the parameters on several subjects """
    # Subjects to process
    subnums = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,41,42]
    #subnums = [3]
    # MSM's target subject
    #target_subnums = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,41,42]
    target_subnums = ['mean']
    # Levels to test
    levels = [0]

    # Smoothings to test
    smoothings = [0]

    # Config file to test
    config_files = [
        'dataMSM/myconfdefault'
        #'dataMSM/myconf_lambda10e-2',
        #'dataMSM/myconf_lambda10e-3',
        #'dataMSM/myconf_lambda_1',
        #'dataMSM/myconf_lambda_10',
        #'dataMSM/myconf_lambda10e2',
        #'dataMSM/myconf_lambda10e3'
        #'dataMSM/myconf_lambda10e4',
        #'dataMSM/myconf_lambda10e-4',
        #'dataMSM/myconfdefault_sigmaINLissag_eleve',
        #'dataMSM/myconfdefault_itera_30_5',
        #'dataMSM/myconflambda10e-2_itera_30_5',
        #'dataMSM/myconflambda1_itera_30_5'
        #'dataMSM/myconfdefault_cutthr0.1--IN',
        #'dataMSM/myconflambda10e-2_cutthr0.1--IN',
        #'dataMSM/myconflambda1_cutthr0.1--IN'
        #'dataMSM/myconflambda1_sigmaINLissag_eleve',
        #'dataMSM/myconflambda10e-2_sigmaINLissag_eleve'
        #'dataMSM/myconfdefaultsigma2,2,2',

    ]

    # Hemispheres
    hemis = ['lh']

    # Where the log files will write
    log_dir = "/hpc/banco/hermi.w/logs"

    # For each target subject
    #for tgts in target_subnums:
     #   target_sub = "sub-{:02d}".format(tgts)

        # For each source subject (if different from target)
    for s in subnums:
        #if s != tgts:
           # Subname
        source_sub = "sub-{:02d}".format(s)

        # For each level
        for level in levels:
            # Each smoothings
            for smoothing in smoothings:
                # Each configuration file
                for config_file in config_files:
                     # Each hemisphere
                    for h in hemis:
                        # Create a new job
                        MSM_on_frioul(target_subnums, source_sub, h, level, smoothing, config_file, log_dir)

if __name__ == "__main__":                        
    main()


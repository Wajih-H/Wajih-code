#!/bin/bash

subin=$1
subref=$2
hemi=$3
level=$4
smooth=$5
conf=$6
savedir=$7
outtemplate=$8

hcp_outdir=/hpc/banco/hermi.w/data/fs_db/fsavg6_beta_gii
fsldir=/hpc/soft/fsl/fsl_6.0.1/bin
mydirname=/hpc/banco/hermi.w


mkdir -p $mydirname/$savedir

$fsldir/msm --inmesh=$mydirname/Ressources_fsavg-gii/fsaverage6.$hemi.white.surf.gii --refmesh=$mydirname/Ressources_fsavg-gii/fsaverage6.$hemi.white.surf.gii --indata=$hcp_outdir/fsaverage6_SameTransform_beta.$subin.$hemi.gii --refdata=$hcp_outdir/fsaverage6_mean_beta.$hemi.gii --levels=$level --smoothout=$smooth --conf=$mydirname/$conf -o $mydirname/$savedir/$outtemplate

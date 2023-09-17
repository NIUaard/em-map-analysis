# AWA linac characterization




## Description
characterize the beam-dynamics properties in a cavity (1D, and 3D)
		            
### file list:
- field for ASTRA : 
   - 3D_asta.* (6 files) contains the 3D field for a TESLA superconducting cavity for ASTRA
   - Ez_axis.dat represent the field on axis for astra (z, Ez)
- ASTRA input file
   - 9-cell3D.in: input file for tracking in a 3D map only and vary the phase from -100 to 100 deg (produces 41 outputs)
   - 9-celltest.in: input file with run #1 trackin in 1D file and run #2 tracking in 3D map 
 - Scripts:
   - MakeGridBeam.py  produce a distribution with small longitudinal size and macroparticle arrange on a 2D grid in (x,y). The transverse moementum is set to zero
   - SeeCouplerKick.py generate a map of the transverse kick (copmuting run 1 and 2 from 9-celltest.in) 
   - MomentumAnalysisPRAB36.py copmute variation of kick strnegth as a function of phase (from output from 9-cell3D.in)
   
### run
- generate kick 2D map:
   - generate the input distribution ```python MakeGridBeam.py```
   - copy distribution to proper file name (use by Astra) ```cp grid_distrib.ini dist.ini```
   - run ASTRA  ```astra 9-celltest.in```
   - produce 2D map ```python MomentumAnalysisPRAB36.py```
- analyze kick multipolse component (following [A. Halavanau et al. PRAB 20, 040102, 2017][https://journals.aps.org/prab/abstract/10.1103/PhysRevAccelBeams.20.040102]:
   - generate the input distribution ```python MakeGridBeam.py```
   - copy distribution to proper file name (use by Astra) ```cp grid_distrib.ini dist.ini```
   - run ASTRA  ```astra 9-cell3D.in```
   - produce 2D map ```python SeeCouplerKick.py```


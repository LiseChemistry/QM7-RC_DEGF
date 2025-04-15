# MasterProject_SPAHM-ENN
This is a tentative folder for tracking the master project with Elizavetha
> wandb : https://wandb.ai/lisechemistry_masterproject/nequimol?nw=nwuserlisechemistry

## ToDo List
- [X] read SPAHM articles
- [X] extract xyz files for QM7 database (.inp)
- [X] search for the best geometry optimization procedure (wB97X-D/def2-SVP)
- [X] extract relaxed geometries (redefine database, excluding non-converged structures)
- [X] compute atomization energy for the new database
- [X] install `Q-stack` package
- [X] generate `spahm-a`, `spahm-b` and `spahm-e` representations for the new database
- [X] generate `slatm` representation for the new database 
- [X] compute Hirschfeld charges (`Q-stack`): `wb97xd/def2svp`
- [X] read articles KRR
- [X] change programs' names
- [X] test `mol_0000` with original geometry (`spahm-a`, `spahm-b` and `slatm`, `hirsh`)
- [X] add `docs` in code
- [X] extract charges to the tagret files
- [X] prepare files for `spahm-a` and `spahm-b` (atomic representations for each molecule)
- [X] compute `slatm`
- [X] install the packages
- [ ] data loader
- [ ] use the data to evaluate performances using `3DMol` model
- [ ] compare performances of KRR and ENN models with previous results (Atomization energy - targer property)
- [ ] extract electronic features from spahm-a` and `spahm-b` to use as input for the ENN

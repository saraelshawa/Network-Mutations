# This trial is using many default values to run DFE-Alpha programs
# the data are based on degree as a measure of connectivity from chlamynet
cd /scratch/research/projects/chlamydomonas/network_evolution/analysis/dfe/trial1
#lower
cd lower10th/
est_dfe -c trial2.lower10th.est_dfe-site_class0.config.txt
est_dfe -c trial2.lower10th.est_dfe-site_class1.config.txt 
prop_muts_in_s_ranges -c lower10th_degree_selected/est_dfe.out -o lowerDFE.results.txt
est_alpha_omega -c trial2.lower10th.est_alpha_omega.config.txt
cd ..
#upper
cd upper10th/
est_dfe -c trial2.upper10th.est_dfe-site_class0.config.txt
est_dfe -c trial2.upper10th.est_dfe-site_class1.config.txt 
prop_muts_in_s_ranges -c upper10th_degree_selected/est_dfe.out -o upperDFE.results.txt
est_alpha_omega -c trial2.upper10th.est_alpha_omega.config.txt

NeS_lo	NeS_hi	lower10	upper10
0.000000 1.000000 0.071265	0.088146
1.000000 10.000000 0.043491	0.066407
10.000000 100.000000 0.070027	0.116300
100.000000 -99.000000 0.815218	0.729147 

parameter	lower10	upper10
lambda 0.211353	0.270516
selected_divergence 0.057317	0.099793 
alpha 0.765416	0.789877
omega_A 0.207575	0.291385

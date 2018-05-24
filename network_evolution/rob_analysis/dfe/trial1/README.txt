# This trial is using many default values to run DFE-Alpha programs
# the data are based on degree as a measure of connectivity from chlamynet
cd /scratch/research/projects/chlamydomonas/network_evolution/analysis/dfe/trial1
#lower
cd lower10th/
est_dfe -c trial1.lower10th.est_dfe-site_class0.config.txt
est_dfe -c trial1.lower10th.est_dfe-site_class1.config.txt 
prop_muts_in_s_ranges -c lower10th_degree_selected/est_dfe.out -o lowerDFE.results.txt
est_alpha_omega -c trial1.lower10th.est_alpha_omega.config.txt
cd ..
#upper
cd upper10th/
est_dfe -c trial1.upper10th.est_dfe-site_class0.config.txt
est_dfe -c trial1.upper10th.est_dfe-site_class1.config.txt 
prop_muts_in_s_ranges -c upper10th_degree_selected/est_dfe.out -o upperDFE.results.txt
est_alpha_omega -c trial1.upper10th.est_alpha_omega.config.txt

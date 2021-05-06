# A topological selection of folding pathways from native states of knotted proteins

Agnese Barbensi, Naya Yerolemou, Oliver Vipond, Barbara I. Mahler, Pawel Dabrowski-Tumanski, Dimos Goundaroulis.


Repository to accompany the manuscript [A topological selection of folding pathways from native states of knotted proteins](https://arxiv.org/abs/2104.10530).


We used Python 3.8.


## DATA

1. 'f_distance_matrix.txt' - $f$-distance cost matrix
2. For all 517 trefoil proteins available in KnotProt:
	- xyz files, and
	- knotoid distributions,
	for the entire chain and the knot core.
3. Configurations:
	- xyz files, and
	- knotoid distributions,
	for the knot core.
4. 'double_loop_configuration_mapping.pickle' - name mapping for 2-L configuration names
5. 'knotted_unknotted_sequence_similar_to_3KZN.pickle' - dictionary of all proteins with similar sequence to 3KZN
6. 'non_redundant_representatives.pickle' - list of non-redundant trefoil proteins
7. 'trefoil_proteins_sequence_similarity_clusters.pickle' - dictionary of clusters displayed in Figure 3A


## CODE

1. 'knoto_emd.py' - script to compute the distance between two knotoid distributions
2. 'perturb_uniform.py' - script to compute perturbations of configuration trajectories



## RESULTS

1. Distance matrices and heatmaps for KnotoEMD computations between proteins and configurations
	- 'distance_matrices/trefoil_proteins_ordered.pickle' - a list of all trefoil in the order used in the distance matrices
	- 'distance_matrices/configurations_ordered.pickle' - an (ordered) dictionary of the configurations and their groups in the order used in the distance matrices
2. UMAP plots to accompany Figures 3 and 4. All UMAP projections were computed using: 
	-       n_neighbors=60
	-       min_dist=0.3
	-       n_components=2,3
	-       metric='precomputed'
3. 'trefoil_proteins_sequence_similarity_dendrogram.png' - dendrogram displayed in Figure 3A

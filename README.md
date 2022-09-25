# Comparison-from-network-science-to-sexual-dimorphism-in-the-human-connectome.
This project was realized by

**Juan C Higuera C**

**Kevin N Ramos G**

This project was presented for the course **Advanced Biophysics** of the National University of Colombia.

In the present work, a comparison was made from network science to the human connectome of men and women, this through the establishment of consensus connectomes which incorporated the links present in at least a certain percentage of the population. It was found that regardless of the consensus, the connectome of men exhibits greater segregation and that of women greater integration, in turn, the connectome of men is more asymmetric and non-random. It was found that in terms of local connectivity the connections of men and women do not seem to differ significantly, however in terms of global connectivity they exhibit clear differences.

## Data and methods
The Data was obtained from https://pitgroup.org/connectome/. The data downloaded was consensus structural connectome matrices, this were builded using data from the HCP 1200 (https://www.humanconnectome.org/study/hcp-young-adult/document/1200-subjects-data-release).

![image](https://github.com/JuanHigueraC/A-exploration-of-the-relation-between-structure-dynamics-and-function-of-simmetric-proteins./blob/1454d48cfa3f001344c1a0182a6a1323f0497aee/Images/budapest%20connectome.PNG)

**Figure 1. Budapest Reference Connectome**

A example of a adjacency matrix are presented below

![image](https://github.com/JuanHigueraC/Comparison-from-network-science-to-sexual-dimorphism-in-the-human-connectome./blob/3c42e2b044db21643594b5bf34671efdc1e137bd/Images/example%20of%20adjacency%20matrix.PNG)

Using the library Networkx some topological properties of this matrices was studied.

## Results.
We compare the topological properties of this brain networks at different consensus, this with the objetive to see if the topological patterns reported in the literature are persistent across consensus.

The first analisis was a visualization of the network density at differents consensus.
![image](https://github.com/JuanHigueraC/Comparison-from-network-science-to-sexual-dimorphism-in-the-human-connectome./blob/3c42e2b044db21643594b5bf34671efdc1e137bd/Images/density%20vs%20threshold.PNG)

**Figure 2. Network density at different consensus.**

In this plot its possible see for the same consensus, women´s structural brain networks have less resemblance. Other global topological measures are present in the pdf of this work. 

We also study the nodal properties only with consensus of 20% and 100%.

The degree centrality in the nodes from smallest to largest was for the 20% consensus was:
![image](https://github.com/JuanHigueraC/Comparison-from-network-science-to-sexual-dimorphism-in-the-human-connectome./blob/3c42e2b044db21643594b5bf34671efdc1e137bd/Images/degree%20for%20the%20nodes.PNG)

**Figure 3. Degree centrality from the smallest to the largest.**

Given the resemblance between the degree of the two types of networks at 20% consensus, we suppose that dimorphism in the human connectome are presented in the global patterns of architecture, to evaluate this hipotesis we use a random network with the same degree sequence of this connectomes, and the result obtained was:

![image](https://github.com/JuanHigueraC/Comparison-from-network-science-to-sexual-dimorphism-in-the-human-connectome./blob/3c42e2b044db21643594b5bf34671efdc1e137bd/Images/eigenvector%20for%20the%20nodes.PNG)

**Figure 4. Eigenvector centrality from the smallest to the largest.**

in which it can be seen that the two consensus networks have different differences with respect to the random graph.

For the 100% consensus only a few brain regions aren´t isolate

![image](https://github.com/JuanHigueraC/Comparison-from-network-science-to-sexual-dimorphism-in-the-human-connectome./blob/3c42e2b044db21643594b5bf34671efdc1e137bd/Images/maximum%20threshold%20men.PNG)

**Figure 5. Structural brain network for men´s group at 100% consensus.**

![image](https://github.com/JuanHigueraC/Comparison-from-network-science-to-sexual-dimorphism-in-the-human-connectome./blob/3c42e2b044db21643594b5bf34671efdc1e137bd/Images/maximum%20threshold%20women.PNG)

**Figure 6. Structural brain network for women´s group at 100% consensus.**

In this networks its possible seen a common result of this work and those carried out in the literature, the more integrated character of women´s brain.

## Conclusions

**1.** In the women´s group, the structurals brain networks have less resemblance than in the men´s group.

**2.** In local centrality no sexual dimorphism were presented.

**3.** In global centrality, men´s structural brain network appear more different respect to the random network. In conclusion in global centrality a sexual dimorphism were presented.

**4.** Structural network of the men´s group are more segregated that structural network of the women´s group.

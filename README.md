## Project Title: Studying the influence of climate on woody plant encroachment in semiarid areas of Western US.

## Collaborators on this Project:
•	Project Lead - Erkan Istanbulluoglu
•	Data Science Lead - Sai Nudurupati

## The Problem:
Semiarid ecosystems of the Western US have experienced a major change from grasslands to woody plants in the last 150 years. These include shifts in shrub dominance in the Southwest and changes in grasslands to western juniper in the Northwest US. A number of hypotheses proposed have related woody plant encroachment to climate change, introduced herbivore grazing, changes in grassland fire frequency and the grazers impact on woody plant seed dispersal. 

## Objectives:
In this project we will use a Landlab (Hobley et al., 2017) implementation of the Cellular Automaton Tree-Grass-Shrub Simulator (CATGraSS) (Zhou et al., 2013). CATGraSS simulates dynamics of establishment, growth, disturbance and loss of individual plant functional types across a spatial grid domain. CATGraSS has been used to study woody plant encroachment in relation to climate change in the southwest (Zhou et al., 2013; Caracciolo et al., 2016) and western Northwest (Caracciolo et al.,2017).

Project domains can be in central New Mexico (e.g., Sevilleta National Wildlife Refuge) or Ochoco National Forest, Oregon using actual DEMs of no larger than 10m grid resolution. Alternatively, flat hypothetical surfaces with lower cell resolution can be used. Projects could aim to investigate the influence of climate change, atmospheric CO2 concentration, and human impact in past, present and future on vegetation organization. 

Projects will require developing historical and future climate input. Depending on the modeling domain you can use spatially distributed fields of historical (e.g., Livneh et al., 2013; 2015) and future climate (Abatzoglou, 2011; Abatzoglou and Brown, 2012). A longer-term perspective can be also taken to reconstruct climate from Paleological proxies (Hall and Penner, 2013). The role of CO2 can be included in the transpiration process as well as for calculating Water Use Efficiency (WUE) of plants. Climate inputs from various sources can be downloaded using the OGH tool (Phuong et al., 2019).

A side project, especially when an actual watershed is used as input domain, can include running extreme storm events on you project domain and use runoff routing model options in Landlab. To crease spatial rainfall from radar precipitation data you can use Rainyday (http://her.cee.wisc.edu/projects/rainyday/) which creates stochastically generated storm patterns from radar data using a stochastic storm transposition (SST) method (Wright et al., 2017). 

## Sample Data  : 
• **current climate**:
    - meteorogical data at Deepwell station, Sevilleta LTER - (http://sevlter.unm.edu/content/deep-well-meteorological-station-no-40)

• **past climate**: 
    - paleo reconstructions from Hall et al. 2013
    - CO2 concentrations from Rose et al. 2010
     
• **future climate**:
    - MACA data using Observatory for Gridded Hydrometeorology (OGH) - (https://climate.northwestknowledge.net/MACA/)

## References: 

• Abatzoglou J. T. (2011). Development of gridded surface meteorological data for ecological applications and modelling " International Journal of Climatology. doi: 10.1002/joc.3413. 

• Abatzoglou J.T. and Brown T.J. (2012). A comparison of statistical downscaling methods suited for wildfire applications" International Journal of Climatology.   doi: 10.1002/joc.2312.

• Caracciolo, D., E. Istanbulluoglu, and L.V. Noto (2017). An ecohydrological cellular automaton model investigation of juniper pine tree encroachment in a western North America landscape. Ecosystems, 20: 1114-1123, doi:10.1007/s10021-016-0096-6.

• Caracciolo, D., E. Istanbulluoglu, L.V. Noto, and S. Collins (2016). Mechanisms of shrub encroachment into Northern Chihuahuan Desert grasslands and impacts of climate change investigated using a cellular automata model. Advances in Water Resources, 91: 46–62.

• Caracciolo D., L.V. Noto, E. Istanbulluoglu, S. Fatichi, and X. Zhou (2014). Climate change and ecotone boundaries: Insights from a cellular automata ecohydrology model in a Mediterranean catchment with aspect controlled vegetation patterns. Advances in Water Resources, 73: 159-175. doi.org/10.1016/j.advwatres.2014.08.001. 

• Hall, S. A. and Penner, W. L. (2013): Stable carbon isotopes, C3–C4 vegetation, and 12800 years of climate change in central New Mexico, USA, Palaeogeogr. Palaeocl., 369, 272–281, doi:10.1016/j.palaeo.2012.10.034.

• Hobley, D. E. J., J. M. Adams, S. S. Nudurupati, E. W. H. Hutton, N. M. Gasparini, E. Istanbulluoglu, and G. E. Tucker, (2017): Creative computing with Landlab: an open-source toolkit for building, coupling, and exploring two-dimensional numerical models of Earth-surface dynamics, Earth Surf. Dynam., 5: 21-46, doi:10.5194/esurf-5-21-2017.

• Livneh, B., E. A. Rosenberg, C. Lin, B. Nijssen, V. Mishra, K. M. Andreadis, E. P. Maurer, and D. P. Lettenmaier, 2013: A Long-Term Hydrologically Based Dataset of Land Surface Fluxes and States for the Conterminous United States: Update and Extensions. (2013). J . Climate, 26.  

• Livneh, B., Theodore J. Bohn, David W. Pierce, Francisco Munoz-Arriola, Bart Nijssen, Russell Vose, Daniel R. Cayan, & Levi Brekke (2015). Scientific Data 2. doi:10.1038/sdata.2015.42

• Phuong J., Bandaragoda C., Istanbulluoglu E., Beveridge C., Strauch R., Setiawan L., S. D. Mooney (2019).
Automated retrieval, preprocessing, and visualization of gridded hydrometeorology data products for spatial-temporal exploratory analysis and intercomparison, Environmental Modelling & Software.

• Rose, J. (2010). Quaternary climates: a perspective for global warming. Proceedings of the Geologists' Association, 121(3), 334-341.

• Zhou X., E Istanbulluoglu, and E. R. Vivoni (2013). Modeling the ecohydrological role of aspect-controlled radiation on tree-grass-shrub coexistence in a semiarid climate, Water Resour. Res., 49: 2872-2895. doi:10.1002/wrcr.20259. 

• Wright, D.B., R. Mantilla, and C.D. Peters-Lidard (2017). A remote sensing-based tool for assessing rainfall driven hazards Environmental Modelling & Software, 90 (34-54).

---
layout: page
title: Research areas
section: Research
description: ISISLab research on parallel and distributed computing, graphs and hypergraphs, collaborative systems, semantic data, and immersive technologies.
permalink: /en/research-area/
alt_url: /linee-di-ricerca/
lang: en
custom_css:
- /assets/css/info-box.css
---
 
 
<div class="isis-research">
<p>ISISLab studies how to represent, analyze and simulate complex systems and how people explore data and digital environments. The lab designs algorithms, develops software and evaluates its work with users, schools, cultural institutions and companies.</p>
<p>Each topic is classified using the <a href="https://www.acm.org/publications/class-2012">2012 ACM Computing Classification System</a>.</p>
<ul>
<li>
<strong><a href="#distributed-and-parallel-computing">Distributed and Parallel Computing</a></strong>
<ul>
<li><a href="#large-scale-agent-based-simulation">Large-Scale Agent-Based Simulation</a></li>
<li><a href="#parallel-architectures">Parallel Architectures</a></li>
<li><a href="#high-performance-computing-cloud-and-edge-computing">High Performance Computing, Cloud and Edge Computing</a></li>
<li><a href="#graph-and-hypergraph-algorithms">Graph and Hypergraph Algorithms</a></li>
</ul>
</li>
<li>
<strong><a href="#collaborative-and-social-computing">Collaborative and Social Computing</a></strong>
<ul>
<li><a href="#collaborative-systems-open-data-and-learning">Collaborative Systems, Open Data and Learning</a></li>
<li><a href="#social-network-analysis">Social Network Analysis</a></li>
<li><a href="#semantic-web-and-knowledge-graphs">Semantic Web and Knowledge Graphs</a></li>
<li><a href="#artificial-intelligence-for-networks-and-semantic-data">Artificial Intelligence for Networks and Semantic Data</a></li>
<li><a href="#adaptive-and-personalized-systems">Adaptive and Personalized Systems</a></li>
</ul>
</li>
<li>
<strong><a href="#visualization-and-interaction">Visualization and Interaction</a></strong>
<ul>
<li><a href="#scalable-visualization-of-data-and-networks">Scalable Visualization of Data and Networks</a></li>
<li><a href="#augmented-and-extended-reality">Augmented and Extended Reality</a></li>
<li><a href="#digital-twins">Digital Twins</a></li>
<li><a href="#immersive-interfaces">Immersive Interfaces</a></li>
</ul>
</li>
</ul>
<section id="distributed-and-parallel-computations" aria-labelledby="distributed-and-parallel-computing" style="margin: 35px 0; padding: 28px; background: #f5f7fa; border: 1px solid #dce3eb; border-radius: 12px;"><h1 id="distributed-and-parallel-computing" class="wp-block-heading">Distributed and Parallel Computing</h1>
<section class="info-box" aria-labelledby="large-scale-agent-based-simulation"><h2 id="large-scale-agent-based-simulation">Large-Scale Agent-Based Simulation</h2>
<p>With D-MASON and krABMaga, researchers can model individual agents and observe how collective behaviour emerges from their interactions. The lab studies how to distribute agents across processing units and balance the workload as agents cluster in particular regions of the simulation.</p>
<ul aria-label="ACM CCS 2012 categories">
<li>CCS → Computing methodologies → Modeling and simulation → Simulation types and techniques → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10010355&amp;lid=0.10010147.10010341.10010349.10010355">Agent / discrete models</a></li>
<li>CCS → Computing methodologies → Modeling and simulation → Simulation types and techniques → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10010356&amp;lid=0.10010147.10010341.10010349.10010356">Distributed simulation</a></li>
</ul>
<p><strong>References</strong></p>
<ul>
<li><a href="https://doi.org/10.1177/0037549713489594">Bringing together efficiency and effectiveness in distributed simulations: The experience with D-Mason</a> (2013)</li>
<li><a href="https://dblp.org/rec/conf/bighpc/AmbrosioVFSS25">The Impact of ECS Logic on Parallel Performance in Agent-based Model Simulations</a> (2025)</li>
<li><a href="https://journals.sagepub.com/doi/abs/10.1177/0037549713489594">D-MASON</a></li>
<li><a href="https://github.com/krABMaga/krABMaga">krABMaga simulator</a></li>
</ul>
</section>

<section class="info-box" aria-labelledby="parallel-architectures"><h2 id="parallel-architectures">Parallel Architectures</h2>
<p>The lab studies how parallel architectures affect application performance. The miniLB benchmark compares the same simulation across GPUs from different vendors. The SYgraph framework addresses a related question: how to run graph analytics algorithms efficiently across GPU architectures.</p>
<ul aria-label="ACM CCS 2012 categories">
<li>CCS → Computer systems organization → Architectures → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10010528&amp;lid=0.10010520.10010521.10010528">Parallel architectures</a></li>
</ul>
<p><strong>References</strong></p>
<ul>
<li><a href="https://doi.org/10.1016/j.future.2025.108032">miniLB: Benchmarking Lattice Boltzmann simulations on AMD, Intel, and NVIDIA GPUs</a> (2026)</li>
<li><a href="https://doi.org/10.1145/3754598.3754615">SYgraph: A Portable Heterogeneous Graph Analytics Framework for GPUs</a> (2025)</li>
</ul>
</section>

<section class="info-box" aria-labelledby="high-performance-computing-cloud-and-edge-computing"><h2 id="high-performance-computing-cloud-and-edge-computing">High Performance Computing, Cloud and Edge Computing</h2>
<p>The lab developed the SOF framework to explore model parameters by running simulations on clusters and in the cloud. Other work examined how to describe scientific workflows that run across multiple cloud infrastructures.</p>
<ul aria-label="ACM CCS 2012 categories">
<li>CCS → Computing methodologies → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10010169&amp;lid=0.10010147.10010169">Parallel computing methodologies</a></li>
<li>CCS → Computer systems organization → Architectures → Distributed architectures → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10003100&amp;lid=0.10010520.10010521.10010537.10003100">Cloud computing</a></li>
</ul>
<p><strong>References</strong></p>
<ul>
<li><a href="https://doi.org/10.1016/j.simpat.2017.12.005">Distributed simulation optimization and parameter exploration framework for the cloud</a> (2018)</li>
<li><a href="https://dblp.org/rec/conf/webist/MalandrinoS05">A Taxonomy of Programmable http Proxies for Advanced Edge Services</a> (2005)</li>
<li><a href="/en/progetti/ligate/">LIGATE</a></li>
<li><a href="https://doi.org/10.1002/cpe.5802">Scientific workflows across multiple clouds (2020)</a></li>
</ul>
</section>

<section class="info-box" aria-labelledby="graph-and-hypergraph-algorithms"><h2 id="graph-and-hypergraph-algorithms">Graph and Hypergraph Algorithms</h2>
<p>Early work examined how to reduce the number of links needed to route a request through a peer-to-peer network. Later research used hypergraphs to study how to select the nodes that initiate a diffusion process when interactions involve whole groups.</p>
<ul aria-label="ACM CCS 2012 categories">
<li>CCS → Mathematics of computing → Discrete mathematics → Graph theory → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10010917&amp;lid=0.10002950.10003624.10003633.10010917">Graph algorithms</a></li>
<li>CCS → Mathematics of computing → Discrete mathematics → Graph theory → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10003637&amp;lid=0.10002950.10003624.10003633.10003637">Hypergraphs</a></li>
</ul>
<p><strong>References</strong></p>
<ul>
<li><a href="https://doi.org/10.1007/s00224-007-9074-x">Degree-Optimal Routing for P2P Systems</a> (2009)</li>
<li><a href="https://doi.org/10.3390/e23070796">Social Influence Maximization in Hypergraphs</a> (2021)</li>
</ul>
</section>
</section>

<section aria-labelledby="collaborative-and-social-computing" style="margin: 35px 0; padding: 28px; background: #f5f7fa; border: 1px solid #dce3eb; border-radius: 12px;"><h1 id="collaborative-and-social-computing" class="wp-block-heading">Collaborative and Social Computing</h1>
<section class="info-box" aria-labelledby="collaborative-systems-open-data-and-learning"><h2 id="collaborative-systems-open-data-and-learning">Collaborative Systems, Open Data and Learning</h2>
<p>The lab designs and evaluates tools that help people create data, discuss findings and make decisions together. In the European ROUTE-TO-PA project, citizens and public authorities used the Social Platform for Open Data to build and interpret open datasets. In education, CoFFEE helped teachers organize small-group discussions and study student participation. These projects complement the lab’s research on teaching computer science and artificial intelligence.</p>
<ul aria-label="ACM CCS 2012 categories">
<li>CCS → Information systems → Information systems applications → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10003233&amp;lid=0.10002951.10003227.10003233">Collaborative and social computing systems and tools</a></li>
<li>CCS → Applied computing → Education → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10010490&amp;lid=0.10010405.10010489.10010490">Computer-assisted instruction</a></li>
</ul>
<p><strong>References</strong></p>
<ul>
<li><a href="https://doi.org/10.1109/COLCOM.2007.4553836">CoFFEE : Cooperative Face2Face educational environment</a> (2007)</li>
<li>ROUTE-TO-PA (<a href="/en/progetti/route-to-pa/">ISISLab project page</a>, <a href="https://cordis.europa.eu/project/id/645860/en">CORDIS project record</a>)</li>
<li><a href="/en/progetti/lead/">LEAD</a></li>
</ul>
</section>

<section class="info-box" aria-labelledby="social-network-analysis"><h2 id="social-network-analysis">Social Network Analysis</h2>
<p>How does information spread when people interact in groups? ISISLab studies how the structure of social relationships shapes diffusion. One problem is to identify a small set of people who can initiate a process that reaches the entire network. Hypergraph models make it possible to examine the role of group interactions in that process.</p>
<ul aria-label="ACM CCS 2012 categories">
<li>CCS → Human-centered computing → Collaborative and social computing → Collaborative and social computing design and evaluation methods → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10003293&amp;lid=0.10003120.10003130.10003134.10003293">Social network analysis</a></li>
</ul>
<p><strong>References</strong></p>
<ul>
<li><a href="https://doi.org/10.1016/J.TCS.2018.02.024">Active influence spreading in social networks</a> (2019)</li>
<li><a href="https://doi.org/10.1007/978-3-032-02555-5_19">Stay and Play - Modeling Social Influence of Players in the Steam Gaming Community</a> (2025)</li>
<li><a href="https://doi.org/10.3390/e23070796">Social influence diffusion in hypergraphs</a></li>
</ul>
</section>

<section class="info-box" aria-labelledby="semantic-web-and-knowledge-graphs"><h2 id="semantic-web-and-knowledge-graphs">Semantic Web and Knowledge Graphs</h2>
<p>Reusing data from different organizations requires knowing what the data describe, how they are connected and how reliable they are. The lab studies knowledge representation using <em>knowledge graphs</em>, the transformation of tabular data into RDF and queries across distributed sources. Its work on <em>Linked Open Data</em> investigates how to assess the quality of collections of interlinked datasets and how to represent the results so that other systems can query and reuse them.</p>
<ul aria-label="ACM CCS 2012 categories">
<li>CCS → Information systems → World Wide Web → Web data description languages → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10003315&amp;lid=0.10002951.10003260.10003309.10003315">Semantic web description languages</a></li>
</ul>
<p><strong>References</strong></p>
<ul>
<li><a href="https://doi.org/10.1145/3786331">Lost in LOD: Analyzing the Linked Open Data Cloud Quality Maze</a> (2026)</li>
<li><a href="https://doi.org/10.1145/3701716.3717809">From Quality Reports to Knowledge Graphs: a Case Study on CSV-to-KG Transformation</a> (2025)</li>
</ul>
</section>

<section class="info-box" aria-labelledby="artificial-intelligence-for-networks-and-semantic-data"><h2 id="artificial-intelligence-for-networks-and-semantic-data">Artificial Intelligence for Networks and Semantic Data</h2>
<p>ISISLab studies machine learning methods that use relationships among data items. For hypergraphs, the lab investigates how to learn representations from recurring patterns of group interaction and how to generate new structures using diffusion models. It also studies how large language models can describe and classify knowledge graphs. KGSum combines these models with other machine learning techniques to characterize collections of graphs.</p>
<ul aria-label="ACM CCS 2012 categories">
<li>CCS → Computing methodologies → Machine learning → Machine learning approaches → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10010319&amp;lid=0.10010147.10010257.10010293.10010319">Learning latent representations</a></li>
</ul>
<p><strong>References</strong></p>
<ul>
<li><a href="https://doi.org/10.1145/3690624.3709274">Hypergraph Motif Representation Learning</a> (2025)</li>
<li><a href="https://doi.org/10.1145/3630744.3658418">Deciphering Conversational Networks: Stance Detection via Hypergraphs and LLMs</a> (2024)</li>
<li><a href="https://dblp.org/rec/journals/corr/abs-1808-00434">Leveraging Knowledge Graph Embedding Techniques for Industry 4.0 Use Cases</a> (2018)</li>
<li><a href="https://neurips.cc/virtual/2026/loc/sydney/poster/154651">Hypergraph Generation with Latent Diffusion</a></li>
<li><a href="https://github.com/isislab-unisa/KGSum">KGSum</a></li>
</ul>
</section>

<section class="info-box" aria-labelledby="adaptive-and-personalized-systems"><h2 id="adaptive-and-personalized-systems">Adaptive and Personalized Systems</h2>
<p>ISISLab developed CHEOPS to adapt web navigation to user behaviour. With MIMOSA, the lab investigated how access to web content could adapt to the context of use. A related line of work examined how to protect privacy while browsing.</p>
<ul aria-label="ACM CCS 2012 categories">
<li>CCS → Human-centered computing → Human computer interaction (HCI) → HCI design and evaluation methods → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10003332&amp;lid=0.10003120.10003121.10003122.10003332">User models</a></li>
<li>CCS → Information systems → World Wide Web → Web searching and information discovery → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10003271&amp;lid=0.10002951.10003260.10003261.10003271">Personalization</a></li>
</ul>
<p><strong>References</strong></p>
<ul>
<li><a href="https://doi.org/10.1007/BFb0000353">CHEOPS: Adaptive Hypermedia on World Wide Web</a> (1997)</li>
<li><a href="https://doi.org/10.1007/s00779-009-0232-9">MIMOSA: context-aware adaptation for ubiquitous web access</a> (2010)</li>
<li><a href="https://pure.tue.nl/ws/portalfiles/portal/1413144/9910387.pdf">The CHEOPS user model (1998 workshop proceedings, PDF)</a></li>
</ul>
</section>
</section>

<section aria-labelledby="visualization-and-interaction" style="margin: 35px 0; padding: 28px; background: #f5f7fa; border: 1px solid #dce3eb; border-radius: 12px;"><h1 id="visualization-and-interaction" class="wp-block-heading">Visualization and Interaction</h1>
<section class="info-box" aria-labelledby="scalable-visualization-of-data-and-networks"><h2 id="scalable-visualization-of-data-and-networks">Scalable Visualization of Data and Networks</h2>
<p>With the Datalet Ecosystem Provider (DEEP), ISISLab developed reusable web components that load and visualize data directly in the browser. People can explore an open dataset while it is still being assembled. For complex networks, the lab contributed to SimpleHypergraphs.jl, a library for analyzing and visualizing relationships between nodes and groups.</p>
<ul aria-label="ACM CCS 2012 categories">
<li>CCS → Human-centered computing → Visualization → Visualization application domains → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10010923&amp;lid=0.10003120.10003145.10003147.10010923">Information visualization</a></li>
</ul>
<p><strong>References</strong></p>
<ul>
<li><a href="https://doi.org/10.1109/CEDEM.2017.14">Datalet-Ecosystem Provider (DEEP): Scalable Architecture for Reusable, Portable and User-Friendly Visualizations of Open Data</a> (2017)</li>
<li><a href="https://doi.org/10.24166/im.01.2020">Analyzing, Exploring, and Visualizing Complex Networks via Hypergraphs using SimpleHypergraphs.jl</a> (2020)</li>
</ul>
</section>

<section class="info-box" aria-labelledby="augmented-and-extended-reality"><h2 id="augmented-and-extended-reality">Augmented and Extended Reality</h2>
<p>The lab studies how augmented reality (AR) and extended reality (XR) can support cultural heritage experiences and training. Examples include hybrid tours in which the visitor’s location guides exploration of a virtual reconstruction, and serious games that let players discover archaeological sites and artifacts.</p>
<ul aria-label="ACM CCS 2012 categories">
<li>CCS → Human-centered computing → Human computer interaction (HCI) → Interaction paradigms → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10010392&amp;lid=0.10003120.10003121.10003124.10010392">Mixed / augmented reality</a></li>
<li>CCS → Human-centered computing → Human computer interaction (HCI) → Interaction paradigms → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10010866&amp;lid=0.10003120.10003121.10003124.10010866">Virtual reality</a></li>
</ul>
<p><strong>References</strong></p>
<ul>
<li><a href="https://doi.org/10.1145/3750069.3750323">Exploring Cultural Heritage through Play: Insights from Two Case Studies Combining Immersive and Traditional Play</a> (2025)</li>
<li><a href="/en/progetti/xrtourguide/">XRTourGuide</a></li>
</ul>
</section>

<section class="info-box" aria-labelledby="digital-twins"><h2 id="digital-twins">Digital Twins</h2>
<p>ISISLab investigates how to build digital replicas of real places and use them for training. XRTwinScape uses <em>3D Gaussian splatting</em> to reconstruct workplaces from images, so trainees can explore a virtual version of the spaces where they will work.</p>
<ul aria-label="ACM CCS 2012 categories">
<li>CCS → Computing methodologies → Artificial intelligence → Computer vision → Computer vision problems → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10010254&amp;lid=0.10010147.10010178.10010224.10010245.10010254">Reconstruction</a></li>
</ul>
<p><strong>References</strong></p>
<ul>
<li><a href="https://dblp.org/rec/conf/sensexr/AmorosiniMMMPSS25">XR-Enabled Immersive Training for Industry 5.0: The XRTwinScape Platform</a> (2025)</li>
<li>XRTwinScape (<a href="/en/progetti/xrtwinscape/">ISISLab project page</a>, <a href="https://isislab-unisa.github.io/XRTwinScape/">project website</a>)</li>
</ul>
</section>

<section class="info-box" aria-labelledby="immersive-interfaces"><h2 id="immersive-interfaces">Immersive Interfaces</h2>
<p>How do visitors find their way through a reconstructed space and interact with the objects they encounter? The lab investigates these questions with prototypes that use stereoscopic headsets and motion sensors, including serious games for cultural heritage.</p>
<ul aria-label="ACM CCS 2012 categories">
<li>CCS → Human-centered computing → Human computer interaction (HCI) → <a href="https://dl.acm.org/ccs/ccs.cfm?id=10003128&amp;lid=0.10003120.10003121.10003128">Interaction techniques</a></li>
</ul>
<p><strong>References</strong></p>
<ul>
<li><a href="https://doi.org/10.1145/3064644">A Framework to Design, Develop, and Evaluate Immersive and Collaborative Serious Games in Cultural Heritage</a> (2018)</li>
<li><a href="/en/progetti/sermas/">SERMAS</a></li>
</ul>
</section>
</section><p><a href="/en/scientific-publications/">Explore ISISLab’s scientific publications</a></p>
</div>
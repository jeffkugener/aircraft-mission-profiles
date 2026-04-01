# Aircraft Mission Profiles

## Overview
This repository provides a dataset of synthetic mission-derived power profiles for reliability-oriented evaluation of electric propulsion systems. The profiles are generated from real flight trajectories and environmental data, preserving mission characteristics relevant for converter stress and lifetime assessment.

The dataset is intended to support electro-thermal simulation, reliability modelling and preliminary design studies of power converters in electrified aircraft propulsion.

## Methodology
The dataset is derived from a combination of operational flight data and atmospheric reanalysis:

- **Flight data**: ADS-B trajectories obtained from the OpenSky Network  
- **Environmental data**: ERA5 reanalysis including temperature, pressure and wind  

Mission profiles are reconstructed by computing the propulsive power demand based on aircraft performance models, including aerodynamic drag, climb rate and true airspeed.

Each mission is segmented into flight phases:
- Take-off (TO)  
- Climb (CL)  
- Cruise (CR)  
- Descent (DE)  
- Level segments (LVL)  

Phase-resolved statistical analysis is performed to extract:
- Mean operating points  
- Variability and fluctuation characteristics  
- Spectral properties of power demand  

Based on these statistics, **synthetic mission profiles** are generated that preserve both steady-state conditions and dynamic load characteristics relevant for thermal cycling and reliability assessment.

## Dataset Content
The dataset includes:

### Mission-derived power profiles
- Time series of propulsive power demand  
- Phase-resolved segmentation  
- Synthetic profiles preserving statistical properties of real missions  

### Mission statistics
- Flight frequency and mission occurrence characteristics  
- Phase durations and distributions  
- Statistical descriptors of power demand  

### Environmental conditions
- Altitude profiles  
- Ambient temperature  
- Atmospheric conditions such as humidity and pressure  

## Data Structure

...

## Application
The dataset is designed for:

- Reliability assessment of electric propulsion systems  
- Electro-thermal simulation of mission-dependent loading  
- Thermal cycle extraction and lifetime modelling  
- Preliminary design and system-level studies  

The profiles provide operating points and fluctuation behaviour required to evaluate temperature cycling, mean temperature and mission-dependent stress factors.

## Scope and Limitations
- The dataset is based on conventional aircraft flight data and does not represent measurements from electric aircraft  
- Power profiles are reconstructed using modelling approaches and are therefore synthetic  
- The data is intended for system-level and reliability studies, not for detailed component validation  

## Citation
If you use this dataset, please cite the associated publication:

> J. Kugener et al., “Towards reliability-oriented mission profiles for electric aircraft propulsion converters,” 2025.

## License
Specify license information here (e.g. CC BY 4.0)

## Contact
For questions or collaboration:
Jeff Kugener  
German Aerospace Center (DLR)  
Institute of Electrified Aero Engines

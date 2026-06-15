# Reliability-Oriented Aircraft Mission Profiles

## Overview

This repository provides a dataset of reliability-oriented synthetic mission profiles for the evaluation of electric aircraft propulsion systems.

Reliable operation of power electronic converters in electrified aircraft depends strongly on mission-specific operating conditions. Electrical loading, thermal stress and environmental conditions vary throughout the mission and influence degradation mechanisms such as bond-wire fatigue, solder fatigue, dielectric degradation, corrosion and radiation-induced failures. As a result, reliability assessment requires representative mission profiles that capture both operating conditions and mission-dependent variability.

The mission profiles contained in this repository are derived from large sets of real aircraft operations and environmental data. ADS-B flight trajectories are combined with atmospheric reanalysis data to estimate true airspeed, altitude-dependent environmental conditions and propulsive power demand throughout the mission.

Rather than providing individual flight trajectories, the repository provides statistically derived synthetic mission profiles representing typical operation of a specific aircraft and operator. The profiles preserve phase-dependent operating conditions and mission characteristics relevant for electro-thermal loading, thermal cycling and lifetime assessment of power electronic converters.

The dataset is intended to support:

- Reliability assessment of electric propulsion systems
- Electro-thermal simulation of mission-dependent loading
- Thermal cycle extraction and counting
- Physics-of-failure based lifetime modelling
- Preliminary design and system-level evaluation
- Mission-based stress characterization and comparison

The methodology and datasets are described in:

> J. Kugener, K. Gnerlich, I. Koch and S. Kazula, "Towards Reliability-Oriented Mission Profiles for Electric Aircraft Propulsion Converters," PCIM Europe 2026.

## Methodology

### Data

The dataset is derived from a combination of operational flight data and atmospheric reanalysis.

**Flight data:** ADS-B trajectories obtained from the OpenSky Network.

> M. Schäfer, M. Strohmeier, V. Lenders, I. Martinovic and M. Wilhelm, "Bringing Up OpenSky: A Large-Scale ADS-B Sensor Network for Research," Proceedings of the 13th International Symposium on Information Processing in Sensor Networks (IPSN), 2014. DOI: 10.1109/IPSN.2014.6846743.

**Environmental data:** ERA5 atmospheric reanalysis provided by the Copernicus Climate Change Service (C3S).

> Copernicus Climate Change Service (C3S), ERA5 Hourly Data on Single Levels from 1940 to Present, Climate Data Store, 2023. DOI: 10.24381/cds.adbb2d47.

### Synthetic Mission Generation

For each aircraft, a large number of operational flights are analyzed using ADS-B trajectory data and atmospheric reanalysis information.

Flight trajectories are processed to determine:

- Flight phases
- Altitude profiles
- True airspeed
- Ambient temperature
- Atmospheric pressure
- Relative humidity
- Estimated propulsive power demand

Mission phases are classified into:

- Take-off (TO)
- Climb (CL)
- Cruise (CR)
- Descent (DE)
- Level flight (LVL)

The resulting flight database is statistically evaluated on a phase-resolved basis. For each mission phase, representative operating conditions and mission characteristics are extracted from the complete flight population.

The repository does not contain individual reconstructed flights. Instead, the extracted statistics are used to generate representative synthetic missions that capture typical operation of a given aircraft and operator while preserving reliability-relevant operating conditions.

Two mission representations are provided:

#### Average Mission Profile

The average mission profile contains phase-resolved mean operating conditions and represents a typical mission without synthesized power fluctuations.

#### Dynamic Mission Profile

The dynamic mission profile augments the average mission with synthesized power fluctuations derived from statistical analysis of the flight population.

The fluctuation synthesis is based on phase-resolved characterization of power variability and power spectral density (PSD). The resulting profiles preserve the dominant fluctuation energy within the observable frequency range and provide a more realistic representation of mission-dependent loading relevant for thermal cycling and degradation mechanisms in power semiconductors.

The synthesized profiles are intended for electro-thermal simulation, thermal cycle extraction and mission-based reliability assessment.

### Limitations of the Dynamic Profiles

- ADS-B data are limited to a temporal resolution of 1 Hz
- High-frequency dynamics may not be fully represented
- Derived quantities remain sensitive to trajectory inconsistencies and preprocessing assumptions
- Additional filtering and preprocessing may further improve robustness
- The mapping from propulsive power demand to converter-level electrical loading is currently based on simplified assumptions

Consequently, the average mission profiles should be considered the most robust representation of mission operation, while the dynamic profiles provide an additional approximation of mission-dependent fluctuation behavior that remains subject to ongoing refinement and validation.

## Repository Structure

```text
.
├─ README.md
├─ LICENSE
├─ example_usage.py
└─ missions/
   ├─ dataset_summary.csv
   ├─ mission_profile_<icao24>_avg.csv
   └─ mission_profile_<icao24>_dynamic.csv
```

## Dataset Content

### dataset_summary.csv

Contains aircraft-level mission statistics.

| Column | Description |
|----------|----------|
| icao24 | Aircraft ICAO24 identifier |
| aircraft_type | Aircraft type |
| operator | Aircraft operator |
| n_flights | Number of analysed flights |
| analysis_period_start | Start date of analysis period |
| analysis_period_end | End date of analysis period |
| mission_duration_mean_min | Mean mission duration |
| mission_duration_median_min | Median mission duration |
| mission_duration_std_min | Standard deviation of mission duration |
| mission_distance_mean_km | Mean mission distance |
| mission_distance_median_km | Median mission distance |
| mission_distance_std_km | Standard deviation of mission distance |

### mission_profile_<icao24>_avg.csv

Average synthetic mission profile.

| Column | Unit | Description |
|----------|----------|----------|
| time_s | s | Mission time |
| phase | - | Flight phase |
| ambient_temperature_K | K | Ambient temperature |
| relative_humidity_pct | % | Relative humidity |
| pressure_Pa | Pa | Atmospheric pressure |
| altitude_m | m | Altitude |
| tas_ms | m/s | True airspeed |
| thrust_N | N | Propulsive thrust |
| propulsive_power_kW | kW | Propulsive power demand |

### mission_profile_<icao24>_dynamic.csv

Dynamic synthetic mission profile including synthesized intra-phase power fluctuations.

The file uses the same column structure as the average profile.

## Example Usage

Run:

```bash
python example_usage.py
```

Select the aircraft by changing:

```python
ICAO24 = "4cae87"
```

The script loads the mission statistics, prints the aircraft summary and plots both mission loading and environmental conditions.

## Scope and Limitations

- The dataset is based on conventional aircraft operations and does not represent measurements from electric aircraft
- Power and thrust profiles are reconstructed using modelling approaches and are therefore synthetic
- The dataset is intended for system-level simulation and reliability assessment
- The dataset is not intended for detailed aircraft performance validation
- ADS-B resolution limits the representation of high-frequency dynamics
- Additional preprocessing and validation of synthesized fluctuations remain subjects of ongoing work

## Citation

If you use this dataset, please cite both the associated publication and the data repository.

### Publication

J. Kugener, K. Gnerlich, I. Koch and S. Kazula, "Towards Reliability-Oriented Mission Profiles for Electric Aircraft Propulsion Converters," PCIM Europe 2026; International Exhibition and Conference for Power Electronics, Intelligent Motion, Renewable Energy and Energy Management, Nuremberg, Germany. DOI: 10.30420/566716021

### Data Repository

J. Kugener, K. Gnerlich, I. Koch and S. Kazula, "Reliability-Oriented Aircraft Mission Profiles," Data Repository, 2026. [Online]. Available: https://doi.org/10.83196/aircraft-mission-profiles. DOI: 10.83196/aircraft-mission-profiles

## License

This dataset is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

https://creativecommons.org/licenses/by/4.0/

## Contact

Jeff Kugener 
German Aerospace Center (DLR)  
Institute of Electrified Aero Engines

Email: jeff.kugener@dlr.de
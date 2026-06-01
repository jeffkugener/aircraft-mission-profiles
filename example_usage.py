import pandas as pd
import matplotlib.pyplot as plt


MISSIONS_DIR = "missions"

# Select the aircraft here
ICAO24 = "4cae87"


summary = pd.read_csv(f"{MISSIONS_DIR}/dataset_summary.csv")

icao24 = ICAO24.lower()
selected = summary[summary["icao24"] == icao24]

if selected.empty:
    available = ", ".join(summary["icao24"])
    raise ValueError(f"Aircraft '{icao24}' not found. Available aircraft: {available}")

row = selected.iloc[0]

avg_profile = pd.read_csv(f"{MISSIONS_DIR}/mission_profile_{icao24}_avg.csv")
dynamic_profile = pd.read_csv(f"{MISSIONS_DIR}/mission_profile_{icao24}_dynamic.csv")

print()
print("Mission profile dataset")
print("=======================")
print(f"Aircraft:        {row['icao24']} ({row['aircraft_type']})")
print(f"Operator:        {row['operator']}")
print(f"Flights:         {int(row['n_flights'])}")
print(f"Period:          {row['analysis_period_start']} to {row['analysis_period_end']}")
print()
print("Mission duration")
print(f"  Mean:          {row['mission_duration_mean_min']:.1f} min")
print(f"  Median:        {row['mission_duration_median_min']:.1f} min")
print(f"  Std:           {row['mission_duration_std_min']:.1f} min")
print()
print("Mission distance")
print(f"  Mean:          {row['mission_distance_mean_km']:.1f} km")
print(f"  Median:        {row['mission_distance_median_km']:.1f} km")
print(f"  Std:           {row['mission_distance_std_km']:.1f} km")

time_min = dynamic_profile["time_s"] / 60.0

fig, axes = plt.subplots(3, 1, figsize=(9, 7), sharex=True)

axes[0].plot(time_min, dynamic_profile["altitude_m"])
axes[0].set_ylabel("Altitude [m]")
axes[0].grid(True, alpha=0.3)

axes[1].plot(time_min, dynamic_profile["tas_ms"])
axes[1].set_ylabel("TAS [m/s]")
axes[1].grid(True, alpha=0.3)

axes[2].plot(time_min, avg_profile["propulsive_power_kW"], label="Average")
axes[2].plot(time_min, dynamic_profile["propulsive_power_kW"], label="Dynamic")
axes[2].set_ylabel("Power [kW]")
axes[2].set_xlabel("Time [min]")
axes[2].grid(True, alpha=0.3)
axes[2].legend()

fig.suptitle(f"Mission loads: {icao24}")
fig.tight_layout()
plt.show()

fig, axes = plt.subplots(3, 1, figsize=(9, 7), sharex=True)

axes[0].plot(time_min, dynamic_profile["altitude_m"])
axes[0].set_ylabel("Altitude [m]")
axes[0].grid(True, alpha=0.3)

axes[1].plot(time_min, dynamic_profile["ambient_temperature_K"])
axes[1].set_ylabel("Temperature [K]")
axes[1].grid(True, alpha=0.3)

axes[2].plot(time_min, dynamic_profile["relative_humidity_pct"])
axes[2].set_ylabel("Humidity [%]")
axes[2].set_xlabel("Time [min]")
axes[2].grid(True, alpha=0.3)

fig.suptitle(f"Environmental conditions: {icao24}")
fig.tight_layout()
plt.show()

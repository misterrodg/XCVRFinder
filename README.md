# XCVR Finder

A simple Python-based tranceiver finder for use with [FAA NASR Data](https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/).

It is designed to assist in building and maintaining the transceivers for an ARTCC on VATSIM.

## Requirements

Python3.8 or Later (Tested with Python 3.10.12)

# Instructions for Use

First, download the current ARTCC Facilities (AFF) file from the [FAA NASR Data](https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/). Copy the `AFF.txt` file from the zip into the root directory.

## Getting the Data

Run the following command, where `AAA` is the FAA three letter identifier for the facility:

```
python3 find.py --facility=[AAA]
```

The resulting file will be in the root directory as `AFF_[AAA].json`

Note that the data in the file, while directly from the FAA, might be slightly off. If you look the coordinates up, you will often find that the coordinates are an estimate of the actual position. If you look around the location, you will generally find it. RCOs for airports (those served by the ARTCC and not a TRACON) are usually just given as the airport center. The actual antenna/array is on the tower, or main terminal building, but may be a standalone radio tower. RCOs may also be colocated with ARSRs or VORs, and those are usually accurate. Standalone arrays are not often exact. Looking the name up on [RadioReference.com](https://www.radioreference.com/db/) might get you closer to the actual location.

Overall, the data should be a close enough approximation on its own. If you wish to add precision, you can copy the coordinates into map software and try to find the actual antenna/array in satellite view.

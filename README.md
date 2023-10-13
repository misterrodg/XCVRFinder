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

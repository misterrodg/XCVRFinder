from modules.FileHandler import FileHandler
from modules.Location import Location

import json

# AFF Data
AFF_DIR = "."
AFF_FILENAME = "AFF.txt"
AFF_PATH = f"{AFF_DIR}/{AFF_FILENAME}"
# AFF Line Definitions
AFF_BASE_DATA = "AFF1"
AFF_SITE_REMARKS = "AFF2"
AFF_COMMFREQ = "AFF3"
AFF_REMARKS = "AFF4"


class AFFData:
    def __init__(self, facilityId: str):
        self.exists = False
        self.resultPath = f"{AFF_DIR}/AFF_{facilityId}.json"
        self.facilityId = facilityId
        self.location = None
        self.objects = []
        self.setUpPath()
        self.parseAFF()

    def setUpPath(self):
        fh = FileHandler()
        if fh.checkFile(AFF_PATH):
            self.exists = True
        else:
            print(
                f"Unable to find AFF file at {AFF_PATH}. Please ensure it is downloaded and in the root directory."
            )

    def parseAFF(self):
        if self.exists:
            with open(AFF_PATH, "r") as affFile:
                affData = affFile.readlines()
                for line in affData:
                    self.processLine(line)
            if len(self.objects) > 0:
                self.toJsonFile(self.resultPath)

    def processLine(self, line: str):
        if line.startswith(f"{AFF_BASE_DATA}{self.facilityId}"):
            if self.location != None and len(self.location.frequencies) > 0:
                self.objects.append(self.location.toDict())
            self.aff1(line)
        if line.startswith(f"{AFF_SITE_REMARKS}{self.facilityId}"):
            self.aff2(line)
        if line.startswith(f"{AFF_COMMFREQ}{self.facilityId}"):
            self.aff3(line)
        if line.startswith(f"{AFF_REMARKS}{self.facilityId}"):
            self.aff4(line)

    def coordinateStrToFloat(self, value: str) -> float:
        result = float(value[:-1])
        if value[-1] == "S" or value[-1] == "W":
            result = result * -1
        return result

    def secToDecimalDegrees(self, seconds: float) -> float:
        SEC_IN_MIN = 60
        MIN_IN_DEG = 60
        result = seconds / SEC_IN_MIN / MIN_IN_DEG
        return result

    def freqStrToFloat(self, value: str) -> float:
        result = float(value)
        return result

    def aff1(self, line: str):
        artccName = line[8:48].strip()
        siteLocation = line[48:78].strip()
        crossRef = line[78:128].strip()
        facilityType = line[128:133].strip()
        effectiveDate = line[133:143].strip()
        stateName = line[143:173].strip()
        stateId = line[173:175].strip()
        siteLatDMS = line[175:189].strip()
        siteLatS = line[189:200].strip()
        siteLonDMS = line[200:214].strip()
        siteLonS = line[214:225].strip()
        lat = self.secToDecimalDegrees(self.coordinateStrToFloat(siteLatS))
        lon = self.secToDecimalDegrees(self.coordinateStrToFloat(siteLonS))
        artccIcao = line[225:229].strip()
        self.location = Location(siteLocation, facilityType, lat, lon)

    def aff2(self, line: str):
        siteLocation = line[29:38].strip()
        facilityName = line[38:43].strip()
        siteRemarksNumber = line[43:47].strip()
        siteRemarksText = line[47:247].strip()
        # For Posterity - Nothing is done with this data

    def aff3(self, line: str):
        siteLocation = line[29:38].strip()
        facilityType = line[38:43].strip()
        frequency = line[43:51].strip()
        altitude = line[51:61].strip()
        useName = line[61:77].strip()
        chartedYN = line[77:78].strip()
        landingFacilityId = line[78:82].strip()
        landingStateName = line[82:112].strip()
        landingStateId = line[112:114].strip()
        landingCityName = line[114:154].strip()
        landingFacilityName = line[154:204].strip()
        landingFacilityLatDMS = line[204:218].strip()
        landingFacilityLatS = line[218:229].strip()
        landingFacilityLonDMS = line[229:243].strip()
        landingFacilityLonS = line[243:254].strip()
        freq = self.freqStrToFloat(frequency)
        if freq != 121.5 and freq <= 135 and self.location != None:
            if landingFacilityLatS != "":
                lat = self.secToDecimalDegrees(
                    self.coordinateStrToFloat(landingFacilityLatS)
                )
                lon = self.secToDecimalDegrees(
                    self.coordinateStrToFloat(landingFacilityLonS)
                )
                self.location.addAirport(landingFacilityId, freq, lat, lon)
            else:
                self.location.addFrequency(freq)

    def aff4(self, line: str):
        siteLocation = line[8:38].strip()
        facilityType = line[38:43].strip()
        remarkFrequency = line[43:51].strip()
        remarkNumber = line[51:53].strip()
        remarkText = line[53:199].strip()
        # For Posterity - Nothing is done with this data

    def toJsonFile(self, filePath: str):
        jsonData = self.objects
        with open(filePath, "w") as jsonFile:
            json.dump(jsonData, jsonFile)

data = {
    "region": {
        "name": "Africa",
        "avgAge": 19.7,
        "avgDailyIncomeInUSD": 5,
        "avgDailyIncomePopulation": 0.71
    },
    "periodType": "days",
    "timeToElapse": 58,
    "reportedCases": 674,
    "population": 66622705,
    "totalHospitalBeds": 1380614
}


def estimator(data):
    currentlyInfected = data["reportedCases"] * 10
    severeImpact = data["reportedCases"] * 50
    infectionsByRequestedTime = data["reportedCases"] * 512
    infectionsByRequestedTime = data["reportedCases"] * 512*50
    outputData = {
        "data": {},
        "impact": {"currentlyInfected": currentlyInfected},
        "severeImpact": {severeImpact},
        "infectionsByRequestedTime": {"impact": infectionsByRequestedTime}


    }
    return outputData


print(estimator(data))

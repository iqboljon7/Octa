import requests

def rqs(birthDate:str, pspSerial: str, pspNumber:str) -> str:
    payload = {
        "birthDate": birthDate,
        "pspSerial": pspSerial,
        "pspNumber": pspNumber,
    }
    res = requests.post(
        url="https://kabinet.piima.uz/api/Student/getPersonInfoFromGCP", json=payload
    )
    p = res.json()
    if p['pName'] == None:
        return "Nothing was found with the information you provided, or please recheck the information provided"
    return (f"ismi: {p['pName']}\nfamiliyasi: {p['pSurname']}\nkimning farzandi: {p['pPatronym']}\ntug`ilgan joyi: {p['pPlaceBirth']}\njshshir: {p['pPinpp']}")

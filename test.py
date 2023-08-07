import requests
payload = {
    "document": "AB4821451",
    "dob": "1992-06-02",
    "occupation": "student",
}
res = requests.get(
    url="https://uzbekcoders.uz/api/public/info/individual?document=AB4821451&dob=1992-06-02&occupation=student",json=payload
)
print(res.content)

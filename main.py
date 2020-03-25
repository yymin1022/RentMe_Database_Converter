import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore
from urllib.request import urlopen

project_id = "rent-me-1d154"

# Use the application default credentials
cred = credentials.Certificate('/Volumes/Local Disk/AppProjects/ProjectCredentials/rent-me-1d154-a4468d23ea36.json')
firebase_admin.initialize_app(cred, {
  'projectId': project_id,
})

db = firestore.client()

parseUrl1 = "http://api.data.go.kr/openapi/rntcarentrps-std?serviceKey=APIKEY&pageNo="
parseUrl2 = "&numOfRows=100&type=json"

for i in range(22):
    response = urlopen(parseUrl1 + str(i + 1) + parseUrl2).read().decode('utf-8')
    strJson = json.loads(response)

    for j in range(100):
        try:
            print(strJson.get("response").get("body").get("items")[j].get("entrpsNm"))

            doc_ref = db.collection(u'companies').document(str(i) + "-" + str(j))
            doc_ref.set({
                u'addressGarage': strJson.get("response").get("body").get("items")[j].get("garageRdnmadr"),
                u'addressOffice': strJson.get("response").get("body").get("items")[j].get("rdnmadr"),
                u'countAll': strJson.get("response").get("body").get("items")[j].get("vhcleHoldCo"),
                u'countCar': strJson.get("response").get("body").get("items")[j].get("carHoldCo"),
                u'countElecCar': strJson.get("response").get("body").get("items")[j].get("eleCarHoldCo"),
                u'countElecVan': strJson.get("response").get("body").get("items")[j].get("eleVansCarHoldCo"),
                u'countVan': strJson.get("response").get("body").get("items")[j].get("vansHoldCo"),
                u'latitude': strJson.get("response").get("body").get("items")[j].get("latitude"),
                u'longitude': strJson.get("response").get("body").get("items")[j].get("hardness"),
                u'name': strJson.get("response").get("body").get("items")[j].get("entrpsNm"),
                u'telephone': strJson.get("response").get("body").get("items")[j].get("phoneNumber"),
                u'timeClose': strJson.get("response").get("body").get("items")[j].get("weekdayOperColseHhmm"),
                u'timeOpen': strJson.get("response").get("body").get("items")[j].get("weekdayOperOpenHhmm"),
                u'webUrl': strJson.get("response").get("body").get("items")[j].get("homepageUrl"),
            })
        except IndexError:
            break
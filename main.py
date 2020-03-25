import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from bs4 import beautifulsoup4

project_id = "rent-me-1d154"

# Use the application default credentials
cred = credentials.Certificate('/Volumes/Local Disk/AppProjects/ProjectCredentials/rent-me-1d154-a4468d23ea36.json')
firebase_admin.initialize_app(cred, {
  'projectId': project_id,
})

db = firestore.client()

parseUrl1 = "http://api.data.go.kr/openapi/rntcarentrps-std?serviceKey=9eag1d1n%2FBOSl2FTYMUGz6J9uxN3JtSP%2BJtmKOEl%2FY%2FdcHdX%2Fg02MLYG1PMvZa1k8S5lQ7P%2Bz4BOlIaxyZOLYA%3D%3D&pageNo="
parseUrl2 = "&numOfRows=100&type=json"

doc_ref = db.collection(u'companies').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})
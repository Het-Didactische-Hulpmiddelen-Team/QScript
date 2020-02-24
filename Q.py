import requests
import json

url = "http://server.arne.tech:8080"
def addStudentToQ(roomID, studentName):
    requests.get(url+"/room/join/{0}/{1}".format(roomID, studentName))
    showQueue(roomID)
def deleteStudentFromQ(roomID, studentName):
    requests.get(url+"/room/leave/{0}/{1}".format(roomID, studentName))
    showQueue(roomID)
def deleteAllFromQ(roomID):
    requests.get(url+"/room/clear/{0}".format(roomID))
    showQueue(roomID)
def deleteAtFromQ(roomID, position):
    requests.get(url+"/room/deleteat/{0}/{1}".format(roomID, position))
    showQueue(roomID)
def deleteFirst(roomID):
    deleteAtFromQ(roomID, 0)
    showQueue(roomID)
    
def deleteRoom(roomID):
    requests.get(url+"/room/delete/{0}".format(roomID))
       
def listRoomsWithID():
    data = requests.get(url+"/room/all").json()
    for x in ["{0}  |  {1} - {2} - {3}".format(d["id"], d["vak"], d["lector"], d["vak"]) for d in data]:
        print(x)
def createRoom(lector, course, classroom):
    data ={'lector':lector,
           'vak':course,
           'lokaal':classroom
           }
    header = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    requests.post(url+"/room/create", data=json.dumps(data), headers=header)
def showQueue(roomID):
    data = requests.get(url+"/room/queue/{0}".format(roomID)).json()
    print([str(d) for d in data])
    
createRoom("Fogels", "FOG", "C202")
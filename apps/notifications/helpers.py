import requests
import json


def send_notification(title, text, single, destination, api_key):
	HEADERS_FIREBASE = {
		'Authorization': 'key=' + api_key,
		'Content-Type': 'application/json'
	}

	dest = destination if single else ("/topics/" + destination)

	payload = {
		"to":dest,
		"notification":{
			"title":title,
			"text": text,
			"sound": "default"
		}
	}

	r = requests.post("https://fcm.googleapis.com/fcm/send",headers=HEADERS_FIREBASE, data=json.dumps(payload))

	
	try:
		if 'message_id' in r.json():
			return True
	except Exception, e:
		return False
	
	
	return False


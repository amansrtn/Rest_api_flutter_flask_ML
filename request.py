import requests

url = 'http://localhost:5000/predict'
r = requests.post(url, json={'experience': 2,
                  'test_score': 9, 'interview_score': 6})

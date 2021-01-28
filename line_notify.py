import requests

url = "https://notify-api.line.me/api/notify"

token = "JT78HcIpMBjXvdfA4jk61h3Tf8d0X177LPmD0nasYsW"


headers = {"Authorization" : "Bearer "+ token}

message =  'テスト送信です'
payload = {"message":message,'stickerId':623,'stickerPackageId':4}

requests.post(url, headers = headers, params=payload)




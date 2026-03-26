from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file = drive.CreateFile({'title': 'result.csv'})
file.SetContentFile('result.csv')
file.Upload()

print("上传完成")
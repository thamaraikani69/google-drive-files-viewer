from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaFileUpload,MediaIoBaseDownload
import os,io
SCOPES = 'https://www.googleapis.com/auth/drive'


def list_of_files():
   
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            #print(u'{0} ({1})'.format(item['name'], item['id']))
            name=item['name']
            id=item['id']
            print(name)
            print(id)



if __name__ == '__main__':
    t=os.path.realpath('token.json')
    store = file.Storage(t)
    creds = store.get()
    if not creds or creds.invalid:
        k = os.path.realpath('credentials.json')
        flow = client.flow_from_clientsecrets(k, SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    list_of_files()

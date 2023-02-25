#import
import sys
sys.path.append('input')
sys.path.append('C:/Users/hirot/AppData/Local/Programs/Python/Python39/Lib/site-packages/oauth2client')
sys.path.append('C:/Users/hirot/AppData/Local/Programs/Python/Python39/Lib/site-packages/google_auth_oauthlib')
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path
import base64
import email
from bs4 import BeautifulSoup

class CGmail(object):

    ###########################################
    # 機能	：コンストラクタ
    ###########################################
    def __init__(self, ):
        # Define the SCOPES. If modifying it, delete the token.pickle file.
        self.SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

        # Variable creds will store the user access token.
        # If no valid token found, we will create one.
        self.creds = None

    ###########################################
    # 機能	：Tokenを作成する
    # 引数	：
    #		：
    # 返値	：アクセスすべきURL
    ###########################################
    def CreateToken(self,):

        # The file token.pickle contains the user access token.
        # Check if it exists
        if os.path.exists('token.pickle'):

            # Read the token from the file and store it in the variable creds
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)

        # If credentials are not available or are invalid, ask the user to log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('client_id2.json', self.SCOPES)
                self.creds = flow.run_local_server(port=0)

            # Save the access token in token.pickle file for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

    ###########################################
    # 機能	：最新のSECOMメールの特定URLを取得する
    # 引数	：
    #		：
    # 返値	：アクセスすべきURL
    ###########################################
    def GetUrl(self,):

        # Connect to the Gmail API
        service = build('gmail', 'v1', credentials=self.creds)

        # request a list of all the messages
        result = service.users().messages().list(userId='me',q='in:secom').execute()
        #result = service.users().messages().list(userId='me',q='in:secom is:unread').execute()
        #引用2

        # We can also pass maxResults to get any number of emails. Like this:
        # result = service.users().messages().list(maxResults=200, userId='me').execute()
        messages = result.get('messages')

        # messages is a list of dictionaries where each dictionary contains a message id.

        # iterate through all the messages
        for msg in messages:
            # Get the message from its id
            txt = service.users().messages().get(userId='me', id=msg['id']).execute()

            # Use try-except to avoid any Errors
            try:
                # Get value of 'payload' from dictionary 'txt'
                payload = txt['payload']

                # The Body of the message is in Encrypted format. So, we have to decode it.
                # Get the data and decode it with base 64 decoder.
                parts = payload['body']
                data = parts['data']
            
                #    dataはbase64形式でエンコードされている。これをデコードする。
                #    dataは文字列型である。これをバイト型にする必要があったようだ。
                byData = data.encode()
                strDecode = base64.urlsafe_b64decode(byData).decode()
                #print(str)
                #引用3

                strDecode_list = strDecode.splitlines()
                #print(strDecode)
                #http://www0.e-kakushinを含む文字列を取得する

                #内包表記
                #{f(x)|x∈X and 条件(x)}と思うと良いと思う
                strUrl_list = [s for s in strDecode_list if 'http://www0.e-kakushin' in s]
                strUrl = strUrl_list[0].replace(' ', '')
                
                return strUrl

            except:
                pass
                
#	引用1
#	https://www.geeksforgeeks.org/how-to-read-emails-from-gmail-using-gmail-api-in-python/
#	閲覧：2022年1月3日
#	引用2
#	https://stackoverflow.com/questions/51054245/read-mails-from-custom-label-in-gmail-using-pythongoogle-api
#	閲覧：2022年1月3日
#	引用3「Base64によるエンコードとデコード」
#	https://www.python.ambitious-engineer.com/archives/2066
#	閲覧：2022年1月3日
#	引用4「Pythonで文字列のリスト（配列）の条件を満たす要素を抽出、置換」
#	https://note.nkmk.me/python-list-str-select-replace/
#	閲覧：2022年1月3日

#SECOM情報
#企業コード：7272
#ID：0496736
#パスワード：1***y***
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import numpy as np
import gspread 



def insertPlanMiddleware(rows):
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SAMPLE_SPREADSHEET_ID = '1QSGAY_WyamEQBZ4ITdAGCVAbavR9t-D-4gPQx4Sbf7g'
    SAMPLE_RANGE_NAME = 'middleware'
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'C:\\Users\\beuo\\Documents\\Demandas\\AtualizaMiddleIntegrationVtex\\toolbox\\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    

    sheet = service.spreadsheets()

    # result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
    #                             range=SAMPLE_RANGE_NAME).execute()

    # values = result.get('values', [])
    range_ = SAMPLE_RANGE_NAME  
    value_input_option = 'RAW'  
    include_Values_In_Response = True
    insert_data_option = 'INSERT_ROWS'  
    linhas = np.asarray(rows)
    print(linhas)
    linhas_corrigidas = []
    uma_linha = []
    for row in linhas:    
        p0 = row[0]        
        p1 = row[1]        
        p2 = row[2]        
        p3 = row[3]
        print(p0,p1,p2,p3)        
        uma_linha.append(p3)
        uma_linha.append(p0)
        uma_linha.append(p1)
        linhas_corrigidas.append(p2)
        
    print(linhas_corrigidas)    

    #     value_range_body = {
    #     "majorDimension": "ROWS",
    #     "range": "",
    #     "values": [row]
    #     }
    #     request = service.spreadsheets().values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body, includeValuesInResponse = include_Values_In_Response)
    #     response = request.execute()
    #     print(response)

    # print(values)

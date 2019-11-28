from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import numpy as np
# import gspread 



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
    # gs= gspread.authorize(service)
    
    # gs

    

    sheet = service.spreadsheets()
    # result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
    #                             range=SAMPLE_RANGE_NAME).execute()

    # values = result.get('values', [])

    # print(values)
       
    rows = rows[['timeStamp','clienteEstado','warehouseId','Pendentes de integração']]
    rows = np.asarray(rows)

    # range_ = 'my-range'  # TODO: Update placeholder value.

# How the input data should be interpreted.
    value_input_option = ''  # TODO: Update placeholder value.

    value_range_body = {
        rows[0]
    # TODO: Add desired entries to the request body. All existing entries
    # will be replaced.
    }

    request = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME, valueInputOption=value_input_option, body=value_range_body)
    response = request.execute()

# TODO: Change code below to process the `response` dict:
    print(response)
    # # for row in rows:
    # #     print(row)
    # batch_update_spreadsheet_request_body = {
    #    # A list of updates to apply to the spreadsheet.
    #    # Requests will be applied in the order they are specified.
    #    # If any request is not valid, no requests will be applied.
    #    'data':['oseias','beu','3','4'],  # TODO: Update placeholder value
    #    # TODO: Add desired entries to the request body.
    # }
    # service.spreadsheets().batchUpdate(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME, body = batch_update_spreadsheet_request_body)
    # print("item inserido")    
    

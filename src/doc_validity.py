import joblib
from datetime import datetime
import matplotlib.image as mpimg 
import pandas as pd
import pyzbar.pyzbar as pyzbar
import re

def zimra_validity(file_path):
    img = mpimg.imread(file_path)
    try:
        decodeObject = pyzbar.decode(img)  #pyzbar decode qrcode
        for obj in decodeObject:
                data = str(obj.data) #get the decoded object and convert to string
        string_data = data.replace(":", "")
        string = string_data
        match_obj = re.search("Validity(.*) Verification", string) #capture all string between Validity and Verification
        data_str = match_obj.group(1) #return start date and end date
        split_str = data_str.rsplit() 
        end_date = split_str.pop(2) #remove start date leaving end date
  
        try:
            
            split_date_list= end_date.split('/')
            current_date = datetime.now()
            current_date_format = current_date.strftime("%m/%d/%Y")
            split_currentdate_list = current_date_format.split('/')
            '''
            compare list elements of split_date and split_currentdate get valid date 
            ''' 
            if int(split_date_list[0]>=split_currentdate_list[0])==True and int(split_date_list[2]>=split_currentdate_list[2])==True:
                if int(split_date_list[1]>=split_currentdate_list[1])==True:
                    valid = '{} valid'.format(end_date)
                    return valid
            else:
                not_valid = '{} invalid'.format(end_date)
                return not_valid
        except ValueError:
            pass
    except UnboundLocalError:
        no_qr = 'No_QRCODE'.format(decodeObject)
        return no_qr

def dataframe_zimra(file):
    try:
        if file.endswith("invalid"):
            dict_zimra = {"Zimra(ITF263)":[2]}
            df = pd.DataFrame(dict_zimra)
            return df
        elif file.endswith("valid"):
            dict_zimra = {"Zimra(ITF263)":[0]}
            df = pd.DataFrame(dict_zimra)
            return df
    except AttributeError:
        dict_zimra = {"Zimra(ITF263)":[1]}
        df = pd.DataFrame(dict_zimra)
        return df

def praz_validity(file_path):
    img = mpimg.imread(file_path)
    try:
        decodeObject = pyzbar.decode(img)
        for obj in decodeObject:
            data = str(obj.data)
        date_str = data.rsplit('-')
        date = date_str.pop(1)
        try:
           # date_format = datetime.strptime(date, '%Y')
            current_date = datetime.now().strftime("%Y")
            if int(date>=current_date)==True:
                valid = '{} valid'.format(date)
                return valid
            else:
                not_valid = '{} invalid'.format(date)
                return not_valid
        except ValueError:
            pass

    except UnboundLocalError:
        no_qr = 'No_QRCode'.format(decodeObject)
        return no_qr

def dataframe_praz(file):
    if file.endswith("valid"):
        dict_praz = {"PRAZ":[0]}
        df = pd.DataFrame(dict_praz)
        return df
    elif file.endswith("invalid"):
        dict_praz = {"PRAZ":[2]}
        df = pd.DataFrame(dict_praz)
        return df
    else:
        dict_praz = {"PRAZ":[1]}
        df = pd.DataFrame(dict_praz)
        return df

def prediction(zimra_file_path, praz_file_path):
    df1 = dataframe_zimra(zimra_validity(zimra_file_path))
    df2 = dataframe_praz(praz_validity(praz_file_path))
    result = pd.concat([df1, df2], axis=1)
    load_model = joblib.load(r"/home/jd/Django/board/myproject/dapp/src/DTree_Model.pkl") #load trained model
    pred = load_model.predict(result)
    if pred == 0:
        doc = "Invalid Documents"
    else:
        doc = "Valid Documents"
    return doc

from zipfile import ZipFile
import pandas as pd
def extract_csv(filepath):
    zip_file = ZipFile(filepath)
    files = zip_file.infolist()
    df = pd.read_csv(zip_file.open(files[2].filename))
    return df
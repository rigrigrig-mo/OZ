# excel_file.py

import pandas as pd

def create_excel_file(data, file_name):
    df = pd.DataFrame(data)
    df.to_excel(file_name, index=False)
import os
import sys
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df = pd.read_csv(r"C:/Users/ws_htu768/Desktop/Scripts/Pie_Chart/Msg_type.csv")
df['SUM(TOTAL_SUBMIT_SM_PER_CHR_CNT)'] = df['SUM(TOTAL_SUBMIT_SM_PER_CHR_CNT)'].apply(lambda x: '{:.2f}'.format(x))
df.replace("SE", "Service Exlicit", inplace=True)
df.replace("P", "Promotional ", inplace=True)
df.replace("G", "Government", inplace=True)
df.replace("SI", "Service Implicit", inplace=True)
df.replace("T", "Transactional", inplace=True)
df['SUM(TOTAL_SUBMIT_SM_PER_CHR_CNT)'] = df['SUM(TOTAL_SUBMIT_SM_PER_CHR_CNT)'].astype(np.float)
df['SUM(TOTAL_SUBMIT_SM_PER_CHR_CNT)'] = df['SUM(TOTAL_SUBMIT_SM_PER_CHR_CNT)'].astype(np.int64)
TM_ACCOUNT_TYPE_data = df["TM_ACCOUNT_TYPE"]

SUM_TOTAL_SUBMIT_SM_PER_CHR_CNT_data = df["SUM(TOTAL_SUBMIT_SM_PER_CHR_CNT)"]

colors = ['#4F6272', '#B7C3F3', '#DD7596', '#8EB897', '#ffcc99', '#99ff99']

plt.figure(figsize=(10,15))

textprops = {"fontsize":15}

explode = (0, 0, 0.3, 0, 0, 0)

plt.pie(SUM_TOTAL_SUBMIT_SM_PER_CHR_CNT_data, labels = TM_ACCOUNT_TYPE_data, autopct="%0.1f%%", explode=explode, shadow=True, startangle=90, colors=colors, textprops =textprops)

plt.legend(title = "Account Type:",fontsize=18, loc='upper center',bbox_to_anchor=(0.5, -0.0), ncol=3)

plt.title('TM_ACCOUNT_TYPE',fontsize=20,fontweight='bold')

if os.path.exists("C:/Users/ws_htu768/Desktop/Scripts/Pie_Chart/IMG/") is False:
    os.makedirs("C:/Users/ws_htu768/Desktop/Scripts/Pie_Chart/IMG/")
    #plt.show()
    plt.savefig("C:/Users/ws_htu768/Desktop/Scripts/Pie_Chart/IMG/"+"Account_Type_Chart.png")
else:
    #plt.show()
    plt.savefig("C:/Users/ws_htu768/Desktop/Scripts/Pie_Chart/IMG/"+"Account_Type_Chart.png")
#plt.savefig('Account_Type_Chart.png')

#plt.show()
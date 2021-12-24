import numpy as np
import pandas as pd
from random import randint
def sorter(excel_file, class_1, class_2 = False, class_3 = False):
    name = excel_file + ".xlsx"
    data = pd.read_excel(name)
    data["Sıra"] = None
    for i in data.index:
        data["Sıra"] = randint(1,100)
    
    data.sort_values(by = "Sıra", ascending = True)
    data.drop(["Sıra"], axis = 1, inplace = True)
    
    if class_2 == False and class_3 == False:
        data.sort_values(by = "İsim_Soyisim", ascending = True)
        writer = pd.ExcelWriter("sorted_"+name)
        data.to_excel(writer)
        writer.save()
        return f"Tablo sorted_{name} adı altında kaydedildi!"
    
    elif class_3 == False:
        data_1 = data.iloc[:class_1,:]
        data_1.sort_values(by = "İsim_Soyisim", ascending = True)
        writer = pd.ExcelWriter(f"sorted_{class_1}_"+name)
        data_1.to_excel(writer)
        writer.save()
        
        data_2 = data.iloc[class_1:,:]
        data_2.sort_values(by = "İsim_Soyisim", ascending = True)
        writer = pd.ExcelWriter(f"sorted_{class_2}_"+name)
        data_2.to_excel(writer)
        writer.save()
        
        return f"Tablolar sorted_{class_1}_{name} ve sorted_{class_2}_{name} adında kaydedildi!"
    
    else:
        data_1 = data.iloc[:class_1-1,:]
        data_1.sort_values(by = "İsim_Soyisim", ascending = True)
        writer = pd.ExcelWriter(f"sorted_{class_1}_"+name)
        data_1.to_excel(writer)
        writer.save()
        
        data_2 = data.iloc[class_1:class_2-1,:]
        data_2.sort_values(by = "İsim_Soyisim", ascending = True)
        writer = pd.ExcelWriter(f"sorted_{class_2}_"+name)
        data_2.to_excel(writer)
        writer.save()
        
        data_3 = data.iloc[class_2:,:]
        data_3.sort_values(by = "İsim_Soyisim", ascending = True)
        writer = pd.ExcelWriter(f"sorted_{class_3}_"+name)
        data_3.to_excel(writer)
        writer.save()
        
        return f"Tablolar sorted_{class_1}_{name}, sorted_{class_2}_{name} ve sorted_{class_3}_{name} adında kaydedildi!"
        
        

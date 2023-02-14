import pandas as pd

class DataExtractor:
    def __init__(self) -> None:
        pass

    def file_reader(self,new_data,num_val):
        fl_ext = list(new_data.split("."))[-1]
        print(fl_ext)
        '''
        file_ext = {
            "csv":pd.read_csv(new_data),
            "json":pd.read_json(new_data),
            "xml":pd.read_xml(new_data),
            "xlsx":pd.read_html(new_data),
        }
        '''
        data = pd.read_csv(new_data)
        return data["PAA Title"].head(int(num_val))  
if __name__ == "__main__":
    dat = DataExtractor()
    dat = dat.file_reader("dataset/artificial_intelligence.csv")
    print(dat)





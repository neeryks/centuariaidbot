import pandas as pd

class DataExtractor:
    def __init__(self) -> None:
        pass

    def file_reader(self,new_data,num_val):
        fl_ext = list(new_data.split("."))[-1]
        #print(fl_ext)
        data = pd.read_csv(f"dataset/paa/{new_data}")
        return data["PAA Title",].head(num_val)
    
    
if __name__ == "__main__":
    dat = DataExtractor()
    dat = dat.file_reader("dataset/artificial_intelligence.csv","22")
    print(dat)





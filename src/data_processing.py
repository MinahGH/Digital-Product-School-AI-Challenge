import holidays
from meteostat import Point, Daily
from tqdm import tqdm
from datetime import datetime

class DataProcessing():
    def __init__(self,year,month) -> None:
        self.__dict__.update(locals())
        self.features = {}
        self.berlin = Point(52.5667, 13.3167,37)
    
    
    def get_holidays(self):
        for date, _ in sorted(holidays.DE(years=int(self.year)).items()):
            self.features["number_of_holidays"] = [0.0]
            if str(date.month) == self.month:
                self.features["number_of_holidays"][0] = self.features["number_of_holidays"][0] + 1
                
                
    def get_weather_data(self):
        mean_weather_data = {"tavg":[],"tmin":[],"tmax":[],"prcp":[],"snow":[],"wdir":[],"wspd":[],"wpgt":[],"pres":[],"tsun":[]}
        start = datetime(int(self.year),int(self.month),1)
        end = datetime(int(self.year),int(self.month),28)
        data = Daily(self.berlin, start, end)
        data = data.fetch()
        data = data.mean().values
        
        i =0
        for k,v in mean_weather_data.items():
            mean_weather_data[k].append(data[i])
            i =i+1        
        self.features.update(mean_weather_data)
 
        
        
    def process_data(self):
        self.get_holidays()
        self.get_weather_data()
        return self.features
    
    
if __name__ == "__main__":
    dataprocessing = DataProcessing(year="2012",month="1")
    print(dataprocessing.process_data())

        
        
        
        
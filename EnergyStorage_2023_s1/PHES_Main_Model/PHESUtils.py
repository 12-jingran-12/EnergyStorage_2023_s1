from geopy.geocoders import Nominatim
from geopy.point import Point
from geopy.distance import geodesic
import pandas as pd
import googlemaps



class Location:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.__geolocator = Nominatim(user_agent='demo_of_gnss_help', timeout=20)
        self.point = Point(self.lat, self.lon)

    def get_separation(self, l):
        l1 = (self.lat, self.lon)
        l2 = (l.lat, l.lon)
        return geodesic(l1, l2).meters

    def get_average_geocode(self, l):
        lat = (self.lat + l.lat) / 2
        lon = (self.lon + l.lon) / 2
        return [lon, lat]

    def get_head(self, l):
        api_key = "AIzaSyBOg3mbFMqox4CbDiYl1Y5uyLYuHCJc_bA"
        client = googlemaps.Client(api_key)

        l1 = (self.lat, self.lon)
        l2 = (l.lat, l.lon)

        a1 = client.elevation([l1])[0]["elevation"]
        a2 = client.elevation([l2])[0]["elevation"]
        return abs(a1-a2)

        # data = pd.read_csv("./test_data.csv", sep=',')
        # data['Upper latitude'].apply(lambda x: float(x))
        # data['Lower latitude'].apply(lambda x: float(x))
        # data['Upper longitude'].apply(lambda x: float(x))
        # data['Lower longitude'].apply(lambda x: float(x))
        #
        # a = data.loc[((data['Upper latitude'] > data['Lower latitude']) & (
        #             data['Upper longitude'] > data['Lower longitude'])) & (
        #                          (geocode[0] <= data['Upper latitude']) & (
        #                              geocode[0] >= data['Lower latitude'])) & (
        #                          (geocode[1] <= data['Upper longitude']) & (
        #                              geocode[1] >= data['Lower longitude'])), ['Class', 'Head (m)',
        #                                                                        'Separation (km)', 'Slope (%)',
        #                                                                        'Volume (GL)', 'Energy (GWh)',
        #                                                                        'Storage time (h)',
        #                                                                        'Combined water to rock ratio',
        #                                                                        'Energy stoage MWh per ha']]
        # b = data.loc[
        #     ((data['Upper latitude'] > data['Lower latitude']) & (
        #                 data['Upper longitude'] < data['Lower longitude'])) & (
        #             (geocode[0] <= data['Upper latitude']) & (geocode[0] >= data['Lower latitude'])) & (
        #             (geocode[1] >= data['Upper longitude']) & (geocode[1] <= data['Lower longitude'])), ['Class',
        #                                                                                                  'Head (m)',
        #                                                                                                  'Separation (km)',
        #                                                                                                  'Slope (%)',
        #                                                                                                  'Volume (GL)',
        #                                                                                                  'Energy (GWh)',
        #                                                                                                  'Storage time (h)',
        #                                                                                                  'Combined water to rock ratio',
        #                                                                                                  'Energy stoage MWh per ha']]
        # c = data.loc[
        #     ((data['Upper latitude'] < data['Lower latitude']) & (
        #                 data['Upper longitude'] > data['Lower longitude'])) & (
        #             (geocode[0] >= data['Upper latitude']) & (geocode[0] <= data['Lower latitude'])) & (
        #             (geocode[1] <= data['Upper longitude']) & (geocode[1] >= data['Lower longitude'])), ['Class',
        #                                                                                                  'Head (m)',
        #                                                                                                  'Separation (km)',
        #                                                                                                  'Slope (%)',
        #                                                                                                  'Volume (GL)',
        #                                                                                                  'Energy (GWh)',
        #                                                                                                  'Storage time (h)',
        #                                                                                                  'Combined water to rock ratio',
        #                                                                                                  'Energy stoage MWh per ha']]
        # d = data.loc[
        #     ((data['Upper latitude'] < data['Lower latitude']) & (
        #                 data['Upper longitude'] < data['Lower longitude'])) & (
        #             (geocode[0] >= data['Upper latitude']) & (geocode[0] <= data['Lower latitude'])) & (
        #             (geocode[1] >= data['Upper longitude']) & (geocode[1] <= data['Lower longitude'])), ['Class',
        #                                                                                                  'Head (m)',
        #                                                                                                  'Separation (km)',
        #                                                                                                  'Slope (%)',
        #                                                                                                  'Volume (GL)',
        #                                                                                                  'Energy (GWh)',
        #                                                                                                  'Storage time (h)',
        #                                                                                                  'Combined water to rock ratio',
        #                                                                                                  'Energy stoage MWh per ha']]
        #
        # e = data.loc[
        #     ((data['Upper latitude'] < data['Lower latitude']) & (
        #                 data['Upper longitude'] < data['Lower longitude'])) & (
        #             (geocode[0] >= data['Upper latitude']) & (geocode[0] >= data['Lower latitude'])) & (
        #             (geocode[1] <= data['Upper longitude']) & (geocode[1] <= data['Lower longitude'])), ['Class',
        #                                                                                                  'Head (m)',
        #                                                                                                  'Separation (km)',
        #                                                                                                  'Slope (%)',
        #                                                                                                  'Volume (GL)',
        #                                                                                                  'Energy (GWh)',
        #                                                                                                  'Storage time (h)',
        #                                                                                                  'Combined water to rock ratio',
        #                                                                                                  'Energy stoage MWh per ha']]
        #
        # tmp_dict = {}
        # if not a.empty:
        #     tmp_dict = a.to_dict('records')[0]
        #     return tmp_dict
        # if not b.empty:
        #     tmp_dict = b.to_dict('records')[0]
        #     return tmp_dict
        # if not c.empty:
        #     tmp_dict = c.to_dict('records')[0]
        #     return tmp_dict
        # if not d.empty:
        #     tmp_dict = d.to_dict('records')[0]
        #     return tmp_dict
        # if not e.empty:
        #     tmp_dict = e.to_dict('records')[0]
        #     return float(tmp_dict["Head (m)"]) * 1000
        # else:
        #     tmp_dict['Class'] = 'No value in this area'
        #     tmp_dict['Head (m)'] = 'No value in this area'
        #     tmp_dict['Separation (km)'] = 'No value in this area'
        #     tmp_dict['Slope (%)'] = 'No value in this area'
        #     tmp_dict['Volume (GL)'] = 'No value in this area'
        #     tmp_dict['Energy (GWh)'] = 'No value in this area'
        #     tmp_dict['Storage time (h)'] = 'No value in this area'
        #     tmp_dict['Combined water to rock ratio'] = 'No value in this area'
        #     tmp_dict['Energy stoage MWh per ha'] = 'No value in this area'
        #     return float(tmp_dict["Head (m)"]) * 1000


if __name__ == '__main__':
    l1 = Location(1.5782065575090678, 108.62547847458541)
    l2 = Location(34.2253171, -108.9426205)
    print(l1.get_separation(l2))
    print(l1.get_head(l2))

    # location = geolocator.reverse("39.9073426, 116.391264649167")  # 传入纬度、经度字符串
   
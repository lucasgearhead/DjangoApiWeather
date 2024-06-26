class WeatherSerializer:
    def __init__(self, data):
        # Initialize the WeatherSerializer with weather data
        self.data = data

    def data_to_dict(self):
        """
        Convert weather data to a dictionary following a specific structure.

        Returns:
        - dict: Serialized weather data in dictionary format.
        """
        # Create a dictionary structure representing the serialized weather data
        serialized_data = {
            '_id': str(self.data['_id']),
            'coord': {
                'lon': self.data['coord_lon'],
                'lat': self.data['coord_lat']
            },
            'weather': [
                {
                    'main': self.data['weather_main'],
                    'description': self.data['weather_description']
                }
            ],
            'main': {
                'temp': self.data['temp'],
                'feels_like': self.data['feels_like'],
                'temp_min': self.data['temp_min'],
                'temp_max': self.data['temp_max'],
                'pressure': self.data['pressure'],
                'humidity': self.data['humidity'],
                'sea_level': self.data['sea_level'],
                'grnd_level': self.data['grnd_level']
            },
            'visibility': self.data['visibility'],
            'wind': {
                'speed': self.data['wind_speed'],
                'deg': self.data['wind_deg'],
                'gust': self.data['wind_gust']
            },
            'rain': {
                '1h': self.data['rain_one_hr'],
                '3h': self.data['rain_three_hr']
            },
            'snow': {
                '1h': self.data['snow_one_hr'],
                '3h': self.data['snow_three_hr']
            },
            'clouds': {
                'all': self.data['clouds_all']
            },
            'dt': self.data['date_time'],
            'sys': {
                'country': self.data['country'],
                'sunrise': self.data['sunrise'],
                'sunset': self.data['sunset']
            },
            'timezone': self.data['timezone'],
            'name': self.data['city'],
            'cod': self.data['cod']
        }
        return serialized_data


class WeatherHistorySerializer:
    def __init__(self, weather_history):
        # Initialize the WeatherHistorySerializer with a list of weather history data
        self.weather_history = weather_history

    def data_to_list(self):
        """
        Convert weather history data to a list of dictionaries following a specific structure.

        Returns:
        - list: Serialized weather history data in list format.
        """
        # Initialize an empty list to store serialized weather history data
        serialized_data = []
        # Iterate over each weather data in the weather history
        for weather_data in self.weather_history:
            # Create a dictionary structure representing the serialized weather data
            data = {
                '_id': str(weather_data['_id']),
                'coord_lon': weather_data['coord_lon'],
                'coord_lat': weather_data['coord_lat'],
                'weather_main': weather_data['weather_main'],
                'weather_description': weather_data['weather_description'],
                'temp': weather_data['temp'],
                'feels_like': weather_data['feels_like'],
                'temp_min': weather_data['temp_min'],
                'temp_max': weather_data['temp_max'],
                'pressure': weather_data['pressure'],
                'humidity': weather_data['humidity'],
                'sea_level': weather_data['sea_level'],
                'grnd_level': weather_data['grnd_level'],
                'visibility': weather_data['visibility'],
                'wind_speed': weather_data['wind_speed'],
                'wind_deg': weather_data['wind_deg'],
                'wind_gust': weather_data['wind_gust'],
                'rain_one_hr': weather_data['rain_one_hr'],
                'rain_three_hr': weather_data['rain_three_hr'],
                'snow_one_hr': weather_data['snow_one_hr'],
                'snow_three_hr': weather_data['snow_three_hr'],
                'clouds_all': weather_data['clouds_all'],
                'date_time': weather_data['date_time'],
                'country': weather_data['country'],
                'sunrise': weather_data['sunrise'],
                'sunset': weather_data['sunset'],
                'timezone': weather_data['timezone'],
                'city': weather_data['city'],
                'cod': weather_data['cod']
            }
            # Append the serialized weather data to the list
            serialized_data.append(data)
        return serialized_data

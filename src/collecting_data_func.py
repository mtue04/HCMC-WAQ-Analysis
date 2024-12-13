import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry


def crawl_weather_data(start_date: str, end_date: str, output_file: str):
    """
    Crawl weather data from Open-Meteo API and save to CSV file.

    Parameters:
    - start_date (str): The start date in "YYYY-MM-DD" format.
    - end_date (str): The end date in "YYYY-MM-DD" format.
    - output_file (str): The name of the output CSV file.
    """

    # Setup cache and retry mechanism
    cache_session = requests_cache.CachedSession(".cache", expire_after=-1)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # Open-Meteo API endpoint and parameters
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 10.823099,
        "longitude": 106.629664,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": [
            "temperature_2m",
            "relative_humidity_2m",
            "dew_point_2m",
            "apparent_temperature",
            "precipitation",
            "weather_code",
            "cloud_cover",
            "vapour_pressure_deficit",
            "wind_speed_10m",
            "wind_direction_10m",
        ],
    }

    # Fetch weather data
    try:
        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]
        hourly = response.Hourly()

        # Process hourly data
        hourly_data = {
            "date_time": pd.date_range(
                start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
                end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
                freq=pd.Timedelta(seconds=hourly.Interval()),
                inclusive="left",
            ),
            "temperature_2m": hourly.Variables(0).ValuesAsNumpy(),
            "relative_humidity_2m": hourly.Variables(1).ValuesAsNumpy(),
            "dew_point_2m": hourly.Variables(2).ValuesAsNumpy(),
            "apparent_temperature": hourly.Variables(3).ValuesAsNumpy(),
            "precipitation": hourly.Variables(4).ValuesAsNumpy(),
            "cloud_cover": hourly.Variables(6).ValuesAsNumpy(),
            "vapour_pressure_deficit": hourly.Variables(7).ValuesAsNumpy(),
            "wind_speed_10m": hourly.Variables(8).ValuesAsNumpy(),
            "wind_direction_10m": hourly.Variables(9).ValuesAsNumpy(),
            "weather_code": hourly.Variables(5).ValuesAsNumpy(),
        }

        hourly_dataframe = pd.DataFrame(data=hourly_data)

        # Save to CSV
        hourly_dataframe.to_csv(output_file, index=False)
        print(f"Data successfully saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
# crawl_weather_data("2022-10-01", "2024-09-30", "weather_data.csv")


def crawl_aq_data(start_date: str, end_date: str, output_file: str):
    """
    Crawl air quality data from Open-Meteo API and save to CSV file.

    Parameters:
    - start_date (str): The start date in "YYYY-MM-DD" format.
    - end_date (str): The end date in "YYYY-MM-DD" format.
    - output_file (str): The name of the output CSV file.
    """

    # Setup cache and retry mechanism
    cache_session = requests_cache.CachedSession(".cache", expire_after=-1)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # Open-Meteo API endpoint and parameters
    url = "https://air-quality-api.open-meteo.com/v1/air-quality"
    params = {
        "latitude": 10.823099,
        "longitude": 106.629664,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": [
            "pm10",
            "pm2_5",
            "carbon_monoxide",
            "nitrogen_dioxide",
            "sulphur_dioxide",
            "ozone",
            "us_aqi",
        ],
    }

    # Fetch air quality data
    try:
        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]
        hourly = response.Hourly()

        # Process hourly data
        hourly_data = {
            "date_time": pd.date_range(
                start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
                end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
                freq=pd.Timedelta(seconds=hourly.Interval()),
                inclusive="left",
            ),
            "pm10": hourly.Variables(0).ValuesAsNumpy(),
            "pm2_5": hourly.Variables(1).ValuesAsNumpy(),
            "carbon_monoxide": hourly.Variables(2).ValuesAsNumpy(),
            "nitrogen_dioxide": hourly.Variables(3).ValuesAsNumpy(),
            "sulphur_dioxide": hourly.Variables(4).ValuesAsNumpy(),
            "ozone": hourly.Variables(5).ValuesAsNumpy(),
            "us_aqi": hourly.Variables(6).ValuesAsNumpy(),
        }

        hourly_dataframe = pd.DataFrame(data=hourly_data)

        # Save to CSV
        hourly_dataframe.to_csv(output_file, index=False)
        print(f"Data successfully saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
# crawl_aq_data("2022-10-01", "2024-09-30", ".data/hcmc_aq_data.csv")

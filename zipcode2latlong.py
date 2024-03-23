from geopy.geocoders import Nominatim

def zip_to_coordinates(zip_code):
    geolocator = Nominatim(user_agent="zip_to_coordinates")
    location = geolocator.geocode(zip_code)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Example usage:
zip_code = input("Enter zip code: ")
latitude, longitude = zip_to_coordinates(zip_code)
if latitude is not None and longitude is not None:
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print("Invalid zip code or unable to retrieve coordinates.")

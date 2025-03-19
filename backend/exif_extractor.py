from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS

def extract_exif(image_path):
    try:
        image = Image.open(image_path)
        exif_data = {}
        gps_coords = {}

        if image._getexif() is None:
            return {"exif_data": "No exif data"}

        for tag, value in image._getexif().items():
            tag_name = TAGS.get(tag)
            if tag_name == "GPSInfo":
                gps_info = {}
                for key, val in value.items():
                    try:
                        gps_info[GPSTAGS.get(key)] = str(val)
                        if GPSTAGS.get(key) == "GPSLatitude":
                            gps_coords["lat"] = val
                        elif GPSTAGS.get(key) == "GPSLongitude":
                            gps_coords["lon"] = val
                        elif GPSTAGS.get(key) == "GPSLatitudeRef":
                            gps_coords["lat_ref"] = val
                        elif GPSTAGS.get(key) == "GPSLongitudeRef":
                            gps_coords["lon_ref"] = val
                    except UnicodeEncodeError:
                        gps_info[GPSTAGS.get(key)] = str(val).encode('utf-8', errors='replace').decode('utf-8')
                exif_data["GPSInfo"] = gps_info
            else:
                try:
                    exif_data[tag_name] = str(value)
                except UnicodeEncodeError:
                    exif_data[tag_name] = str(value).encode('utf-8', errors='replace').decode('utf-8')

        if gps_coords:
            exif_data["google_maps_url"] = create_google_maps_url(gps_coords)

        return exif_data

    except IOError:
        return {"error": "File format not supported!"}

def create_google_maps_url(gps_coords):
    dec_deg_lat = convert_decimal_degrees(float(gps_coords["lat"][0]), float(gps_coords["lat"][1]),
                                          float(gps_coords["lat"][2]), gps_coords["lat_ref"])
    dec_deg_lon = convert_decimal_degrees(float(gps_coords["lon"][0]), float(gps_coords["lon"][1]),
                                          float(gps_coords["lon"][2]), gps_coords["lon_ref"])
    return f"https://maps.google.com/?q={dec_deg_lat},{dec_deg_lon}"

def convert_decimal_degrees(degree, minutes, seconds, direction):
    decimal_degrees = degree + minutes / 60 + seconds / 3600
    if direction == "S" or direction == "W":
        decimal_degrees *= -1
    return decimal_degrees
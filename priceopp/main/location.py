import requests

class Location():
    
    def get_ip(self):
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]


    def get_location(self):
        ip_address = self.get_ip()
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        location_data = {
            "ip": ip_address,
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country_name")
        }
        return str(location_data["city"])

call = Location()
print(call.get_location())
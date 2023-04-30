import json
ips = ""
countries= ""

def ip_is_saved(ip):
    global ips
    if ips == "":
        try:
            with open('ips.json') as f:
                ips = json.load(f)
            return ip in ips if ips else False
        except FileNotFoundError:
            return False
    else:
        print("found ip in cache")
        return ip in ips if ips else False

def load_saved_ip(ip):
    global ips
    if ips == "":
        with open('ips.json') as f:
            data = json.load(f)
            ip = data[ip]
        return ip["latitude"], ip["longitude"]
    else:
        print("loading ip from cache")
        return ips[ip]["latitude"], ips[ip]["longitude"]

def save_ip(ip, ip_data):
    try:
        with open('ips.json') as f:
            ips = json.load(f)
    except FileNotFoundError:
        ips = {}

    if ip in ips:
        print("Country already exists in JSON file")
        return False

    try:
        ips[ip] = ip_data
    except Exception as e:
        print(f"Failed to add new country: {e}")
        return False

    with open('ips.json', 'w') as f:
        json.dump(ips, f)

    return True

def country_is_saved(country):
    if country in countries:
        return country in countries if countries else False
    else:
        try:
            with open('countries.json') as f:
                data = json.load(f)
            return country in data if data else False
        except FileNotFoundError:
            return False

def load_saved_country(country):
    global countries
    if countries == "":
        with open('countries.json') as f:
            data = json.load(f)
            country = data[country]
        return country["latitude"], country["longitude"]
    else:
        with open('countries.json') as f:
            data = json.load(f)
            country = data[country]
        return country["latitude"], country["longitude"]


def save_country(country_name, country_data):
    global countries
    if country_name in countries:
        print("Country already exists in JSON file")
        return False
    else:
        try:
            with open('countries.json') as f:
                countries = json.load(f)
        except FileNotFoundError:
            countries = {}
    try:
        countries[country_name] = country_data
    except Exception as e:
        print(f"Failed to add new country: {e}")
        return False

    with open('countries.json', 'w') as f:
        json.dump(countries, f)

    return True
import os
import time
import geoip2.database

os.system("clear")
print ("\033[1;32m[+] Downloading && INSTALLING Figlet")
time.sleep(1.05)

os.system("pkg install figlet")

os.system("clear")
print ("\033[1;32m[+] Figlet Installed Successfully")
time.sleep(1.05)
os.system("clear)



from termcolor import colored



os.system("clear")


print(colored("==================================================================" , 'red'))
os.system('figlet IP-finder')
print(colored("==================================================================" , 'red'))

print ( "                        \033[34m COD3D BY R3X1N             ")
print ( "                        \033[  INSTA:-psycho_rexin_ofc_               ")
print(".")
print ( "                        \033[34m CONTACT-ME:-https://t.me/psycho_rexin_ofc             ")



def find_ip_location(ip_address):
    # Read the MaxMind DB file
    db_file = '/path/to/GeoLite2-City.mmdb'
    reader = geoip2.database.Reader(db_file)

    # Look up the IP address
    response = reader.city(ip_address)

    # Extract the location details
    city = response.city.name
    region = response.subdivisions.most_specific.name
    country = response.country.name

    location = {
        "city": city,
        "region": region,
        "country": country
    }

    return location

ip_address = "8.8.8.8"  # Google's public DNS
location = find_ip_location(ip_address)
print(location)

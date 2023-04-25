import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your phone number: ").strip()
phone_number = phonenumbers.parse(number)

print("Location: "+ geocoder.description_for_number(phone_number, 'en'))
print("Carrier Name: " + carrier.name_for_number(phone_number, 'en'))
print("Timezone: " + "".join(timezone.time_zones_for_number(phone_number)))

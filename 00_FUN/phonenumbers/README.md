### phonenumbers

This is a simple python package that is used to get information about phone numbers.

### Installation

To install phone numbers you need to run the following command:

```shell
pip install phonenumbers
```

Let's create a simple application where we can get the basic information about phone numbers.

```py
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your phone number: ").strip()
phone_number = phonenumbers.parse(number)

print("Location: "+ geocoder.description_for_number(phone_number, 'en'))
print("Carrier Name: " + carrier.name_for_number(phone_number, 'en'))
print("Timezone: " + "".join(timezone.time_zones_for_number(phone_number)))
```

Output:

```shell
Enter your phone number:  +27652****
Location: South Africa
Carrier Name: Cell C
Timezone: Africa/Johannesburg
```

### References

1. [phonenumbers](https://pypi.org/project/phonenumbers/)

import re

email = 'Insert Transaction #14879'
pattern ='Insert Transaction #[0-9]{5,5}$'

hasil = re.match(pattern, email)

print(hasil)
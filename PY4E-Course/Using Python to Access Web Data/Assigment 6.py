############
# Assigment 6
############

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

print('Retrieving', address)

uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()

info = json.loads(data)

print('Retrieved', len(data), 'characters')
print('Count:', len(info["comments"]))
sumatoria = 0

for item in info["comments"]:
    sumatoria = sumatoria + int(item["count"])
print("Sum:", sumatoria)
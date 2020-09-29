############
# Assigment 5
############

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

print('Retrieving', address)

uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()

tree = ET.fromstring(data)

lst = tree.findall('comments/comment/count')
#lst = tree.findall('.//count')
print('Retrieved', len(data), 'characters')
print('Count:', len(lst))

sumatoria = 0
for item in lst:
    sumatoria = sumatoria + int(item.text)

print(sumatoria)
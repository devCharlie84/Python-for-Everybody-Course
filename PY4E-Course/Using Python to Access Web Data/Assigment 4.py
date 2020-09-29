############
# Assigment 4
############

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
count = input('Enter count- ')
position = input('Enter position- ')
contador = int(count)
pos = int(position)

print("Retrieving:", url)

i = 0
while i < contador:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    tagPos = 0
    i = i+1
    for tag in tags:
        tagPos = tagPos+1
        if tagPos == pos:
            print("Retrieving:", tag.get('href', None))
            url = tag.get('href', None)
            tagPos = 0
            break
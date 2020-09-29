############
# Assigment 3
############

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sumatoria = 0
count = 0

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    sumatoria = int(tag.contents[0])+sumatoria
    count = count+1

print("Count", count)
print("Sum", sumatoria)
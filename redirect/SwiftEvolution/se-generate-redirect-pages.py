import requests
import os
import json

URL = "https://github.com/apple/swift-evolution/tree/main/proposals"
BASE_URL = "https://github.com/apple/swift-evolution/blob/main/"
BASE_DIR = 'proposals'

response = requests.get(URL)
data = json.loads(response.text)

# Create base directory if it doesn't exist
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)

# Extract links from JSON and generate redirect HTML files
for item in data['payload']['tree']['items']:
    if item['contentType'] == 'file' and item['path'].endswith('.md'):
        href = BASE_URL + item['path']
        code = item['name'].split('-')[0]
        filename = os.path.join(BASE_DIR, f"SE-{code}.html")

        with open(filename, 'w') as file:
            file.write(f"""<html>
<head>
    <meta http-equiv="refresh" content="0;url={href}" />
</head>
<body>
    If you are not redirected, <a href="{href}">click here</a>.
</body>
</html>
""")

print(f"Files generated in {BASE_DIR} directory.")



# import requests
# from bs4 import BeautifulSoup
# import os

# URL = "https://github.com/apple/swift-evolution/tree/main/proposals"
# BASE_DIR = 'generated_html_files'  # Change to desired directory if needed

# response = requests.get(URL)
# print(f"Response == {response.text}")

# soup = BeautifulSoup(response.content, 'html.parser')

# # Create base directory if it doesn't exist
# if not os.path.exists(BASE_DIR):
#     os.makedirs(BASE_DIR)


# # Search for all links matching the desired form
# for a_tag in soup.find_all('a', href=True):
#     print(f"Found url: {a_tag}")

#     href = a_tag['href']
#     print(f"Found href: {href}")
    
#     if "https://github.com/apple/swift-evolution/blob/main/proposals/" in href and href.endswith('.md'):
#         code = href.split('/')[-1].split('-')[0]
#         filename = os.path.join(BASE_DIR, f"{code}.html")

#         with open(filename, 'w') as file:
#             file.write(f"""<html>
# <head>
#     <meta http-equiv="refresh" content="0;url={href}" />
# </head>
# <body>
#     If you are not redirected, <a href="{href}">click here</a>.
# </body>
# </html>
# """)
#     else:
#         print(f"  *** Skipping this href: {href}")

# print(f"Files generated in {BASE_DIR} directory.")

import xml.etree.ElementTree as ET

# Open and parse the XML file
tree = ET.parse('PortfolioItems.xml')
root = tree.getroot()
data = []

# Loop through each PortfolioItem element
for portfolio_item in root.findall('PortfolioItem'):
    item = {}
    item["title"] = portfolio_item.find('Title').text
    item["description"] = portfolio_item.find('Description').text
    item["image"] = portfolio_item.find('Image').text
    item["link"] = portfolio_item.find('Link').text
    item["created_at"] = portfolio_item.find('Created_at').text
    data.append(item)


for d in data:
    print("Title:", d["title"])
    print("Description:", d["description"])
    print("Image:", d["image"])
    print("Link:", d["link"])
    print("Created at:", d["created_at"])
    print("-" * 40)

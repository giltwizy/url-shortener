import pyshorteners

link = input("Enter the link: ")
shortener = pyshorteners.Shortener()
output_link = shortener.tinyurl.short(link)

print(output_link)
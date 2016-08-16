import webbrowser

#raw_input("\n")
ra = raw_input("Please write the RA of your desired galaxy: \n")
dec = raw_input("Please write the DEC of your desired galaxy: \n")
ra = float(ra)
dec = float(dec)
web = "http://skyserver.sdss.org/dr12/en/tools/chart/image.aspx?ra="\
	+ str(ra) + "&dec=" + str(dec) + \
	"&width=512&height=512&scale=0.2"
print web
webbrowser.open(web)


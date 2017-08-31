import xml.etree.ElementTree as et

def main():
	xml_file = 'orders.xml'
	dom = et.parse(xml_file)
	amts = dom.findall('order/ordAmt')
	for amt in amts :
		print(amt.text)

if __name__ == '__main__':
	main()
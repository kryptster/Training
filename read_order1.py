import xml.dom.minidom as md

doc = md.parse("orders.xml")

orders=doc.getElementsByTagName("order")

for order in orders:
	print("========= ORDER ==========")
	print(order.getElementsByTagName("ordId")[0].childNodes[0].data)
	print(order.getElementsByTagName("custId")[0].childNodes[0].data)
	print(order.getElementsByTagName("custAdd")[0].childNodes[0].data)
	print(order.getElementsByTagName("ordAmt")[0].childNodes[0].data)

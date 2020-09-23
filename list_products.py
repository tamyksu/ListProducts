	
def print_menu():
	print("\nplease choose from the menu:\n\n1.print list of food\n2.print number of foods on list\n3.check if the foos on list")
	print("4.print how many time some product appears\n5.delet product from the list\n6.add product to the list")
	print("7.print all products that are not iliigeal\n8.remove all duplication in the list\n9.Exit\n\n")
	return input("Please enter number 1-9 :")
	
	

list_products = input('please enter list of food: ').split(",")

print(list_products)
input_number = print_menu()
while(not(input_number == "9")):
	if input_number == "1":
		print(list_products)
	elif input_number == "2":
		print("Number of foods on list are: ",len(list_products))
	elif input_number == "3":
		product_name = input("Please enter name of the product ")
		print(product_name in list_products)
	elif input_number == "4":
		product_name = input("Please enter name of the product ")
		print("This pruduct appears: ", list_products.count(product_name), " Times") 
	elif input_number == "5":
		delete_product = input("Please enter name of product you want to delete ")
		list_products.remove(delete_product)
		print("The product ", delete_product ," was removed")
	elif input_number == "6":
		product_name = input("Please enter name of product you want to add ")
		list_products.add(product_name)
		print(product_name," was added")
	elif input_number == "7":
		print("not iliigeal products")
		for product in list_products:
			if len(product)<3 or not(product.isalpha):
				print(product)
	elif input_number == "8":
		list_products=list(dict.fromkeys(list_products))
		#print("removed duplication of products\n"+)
	input_number = print_menu()
	
print("Bye Bye")
		
				
	
		
		
	
		
		
		
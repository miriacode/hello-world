# 1. TAREA: imprime "Hola, mundo"
print("Hello, World")
# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Miriam"
print("Hello", name)	# con una coma
print("Hello "+ name)	# con un +
# 3. imprimir "Hola 42!" con el número en una variable
name = 42
print("Hello", name,"!")	# con una coma
#print("Hello "+ name)	# con una +	-- este debería arrojar un error!
print("Hello "+ str(name)+ " !")
# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "chicken"
fave_food2 = "salad"
print("I love eating {f1} and {f2}".format(f1 =fave_food1, f2=fave_food2)) # con .format()
print(f'I love eating {fave_food1} and {fave_food2}') # con una cadena f
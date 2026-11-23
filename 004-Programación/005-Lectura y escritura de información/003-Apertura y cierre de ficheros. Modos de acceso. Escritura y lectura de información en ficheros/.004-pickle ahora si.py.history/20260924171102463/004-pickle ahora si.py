import pickle

frutas = ['manzana', 'pera', 'platano']

# Save the list to a binary file
archivo = open('frutas.bin', 'wb')
pickle.dump(frutas, archivo)
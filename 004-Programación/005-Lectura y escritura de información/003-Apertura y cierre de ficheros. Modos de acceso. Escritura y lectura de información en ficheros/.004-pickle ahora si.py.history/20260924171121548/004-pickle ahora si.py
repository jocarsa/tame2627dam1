import pickle

frutas = ['manzana', 'pera', 'platano']

# Save the list to a binary file
archivo = open('frutas.dat', 'wb')
pickle.dump(frutas, archivo)
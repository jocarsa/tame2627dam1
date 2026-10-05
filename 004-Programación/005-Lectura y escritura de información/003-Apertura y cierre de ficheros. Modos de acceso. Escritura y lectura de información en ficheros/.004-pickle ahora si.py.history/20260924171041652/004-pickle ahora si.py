import pickle

frutas = ['manzana', 'pera', 'platano']

# Save the list to a binary file
archivo = open('frutas.pkl', 'wb')
pickle.dump(frutas, archivo)
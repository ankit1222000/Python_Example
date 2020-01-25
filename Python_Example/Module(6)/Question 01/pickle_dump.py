import pickle
phonebook={'Chris':'555-222','Katie':'45454354'}
output_file=open("phonebook.dat","wb")
pickle.dump(phonebook,output_file)
output_file.close()
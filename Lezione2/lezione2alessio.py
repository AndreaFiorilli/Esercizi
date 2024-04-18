#Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
#2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

name= "Alessio"
message: str = f"Hello {name}, would you like to learn some Python today?"
print(message)

#Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

name: str= "Alessio"
print (name.lower())
print (name.upper())
print (name.title())

#Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”

print("Albert Einstein \“A person who never made a mistake never tried anything new.\”")

#Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message. 

famous_person: str= "Albert Einstein"
message= f"A person who never made a mistake never tried anything new."
print("\“A person who never made a mistake never tried anything new.\”")

#Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

filename: str= "python_notes.txt"
filename_without_extension= filename.removesuffix(".txt")

#store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
name= ["Luca", "Giancarlo", "Gabriel"]
print (name[0])
print (name[1])
print (name[2])

#Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

names: list= ["luca", "Giancarlo", "Gabriel"]
message: str= f"ciao{names[0]}"
print (message)
message: str= f"ciao{names[1]}"
print (message)
message: str= f"ciao{names[2]}"
print (message)

#Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

list_mezzi: list= ["ducati", "yamaha"]
print(f"vorrei avere una moto {list_mezzi[0]}")
print(f"vorrei avere una moto {list_mezzi[1]}")

#f you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

list_persone: list=["Marco", "Giorgio", "Giovanni"]
print(f"vuoi venire a cena{list_persone[0]}")
print(f"vuoi venire a cena{list_persone[1]}")
print(f"vuoi venire a cena{list_persone[2]}")

#ou just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.

list_persone: list=["Marco", "Giorgio", "Giovanni"]
print(f"vuoi venire a cena{list_persone[0]}")
print(f"vuoi venire a cena{list_persone[1]}")
print(f"vuoi venire a cena{list_persone[2]}")
print(f"purtroppo Giorgio non potrà esserci")
list_persone.remove("Giorgio")
list_persone.append("Andrea")
print(list_persone)

#You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.

list_persone: list=["Marco", "Giorgio", "Giovanni"]
print(f"vuoi venire a cena{list_persone[0]}")
print(f"vuoi venire a cena{list_persone[1]}")
print(f"vuoi venire a cena{list_persone[2]}")
print(f"purtroppo Giorgio non potrà esserci")
list_persone.remove("Giorgio")
list_persone.append("Andrea")
print(list_persone)
print(f"ciao,abbiamo trovato una tavola più grande{list_persone[0]}")
print(f"ciao,abbiamo trovato una tavola più grande{list_persone[1]}")
print(f"ciao,abbiamo trovato una tavola più grande{list_persone[2]}")
list_persone.insert(0, "Filippo")
list_persone.insert(2, "Lorenzo")
list_persone.append("Francesco")
print(f"ciao, vuoi venire a cena che ho il tavolo più grande?{list_persone[0]}")
print(f"ciao, vuoi venire a cenache ho il tavolo più grande?{list_persone[1]}")
print(f"ciao, vuoi venire a cenache ho il tavolo più grande?{list_persone[2]}")

#You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

list_persone: list=["Marco", "Giorgio", "Giovanni"]
print(f"vuoi venire a cena{list_persone[0]}")
print(f"vuoi venire a cena{list_persone[1]}")
print(f"vuoi venire a cena{list_persone[2]}")
print(f"purtroppo Giorgio non potrà esserci")
list_persone.remove("Giorgio")
list_persone.append("Andrea")
print(list_persone)
print(f"ciao,abbiamo trovato una tavola più grande{list_persone[0]}")
print(f"ciao,abbiamo trovato una tavola più grande{list_persone[1]}")
print(f"ciao,abbiamo trovato una tavola più grande{list_persone[2]}")
list_persone.insert(0, "Filippo")
list_persone.insert(2, "Lorenzo")
list_persone.append("Francesco")
print(f"ciao, vuoi venire a cena che ho il tavolo più grande?{list_persone[0]}")
print(f"ciao, vuoi venire a cenache ho il tavolo più grande?{list_persone[1]}")
print(f"ciao, vuoi venire a cenache ho il tavolo più grande?{list_persone[2]}")
print(f"ciao, purtroppo mi si è allagata casa, dobbiamo rimandare{list_persone}")
filippo=list_persone.pop(0)
print(f"{filippo}mi dispiace nn puoi più venire")
marco=list_persone.pop(1)
print(f"{marco}mi dispiace nn puoi più venire")
giovanni=list_persone.pop(3)
print(f"{giovanni}mi dispiace nn puoi più venire")
francesco=list_persone.pop(5)
print(f"{francesco}mi dispiace nn puoi più venire")
del list_persone[0]
del list_persone[0]

#Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.

list_citta: list=["New York", "Dubai" "Londra" "Pechino" "Mosca"]
print(sorted(list_citta))
print(list_citta)
print(sorted(list_citta,reverse=True))
print(list_citta)
list_citta.reverse()
print(list_citta)
list_citta.reverse()
print(list_citta)
list_citta.reverse()
print(list_citta)
list_citta.sort()
print(list_citta)
list_citta.sort(reverse=True)
print(list_citta)


#Working with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner.

list_persone: list=["Marco", "Giorgio", "Giovanni"]
len_lista= len(list_persone)
print (list_persone)









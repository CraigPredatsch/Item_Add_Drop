''' Item_Add_Drop - Allows a user to look at a sample 'Item List' dictionary and add or drop
any of the items, each with their own specified weight, to their personal 'Inventory List' dictionary.
Constraints on the personal Inventory List are set for the total number or items a use can
carry at one time, and the total weight of each item. '''

items = {'shirt': 2, 'pants': 2, 'hat': 1, 'shoes': 3, 'jacket': 4}         #Sample 'Items Found' dictionary
items_copy = {'shirt': 2, 'pants': 2, 'hat': 1, 'shoes': 3, 'jacket': 4}    #Copy of dictionary that will be changing
inventory = {}                                                              #User's Inventory List dictionary
inventory_copy = {}                                                         #Copy of dictionary that will be changing
item_total = 0                                                              #Item Total in Inventory List
item_weight = 0                                                             #Item Weight in Inventory List

def add_item():                                     #Function to add items
    global item_total                               #Declaring global variables
    global item_weight
    print ('You found the following items:')
    print (items_copy)                          #Displays changing dictionary
    print('Would you like to take any items? You can carry up to 3 items or 6 pounds.')
    print ('Press 1 to take. Press 2 to drop an item. Press 3 to end.')
    enter = input()                             #User Input
    try:
        enter_check = int(enter)                #Checks to make sure input is an integer
    except ValueError:
        print ('Sorry that is not a valid response. Please enter 1, 2, or 3.')      #Or it reminds the user that it must be an integer.
        add_item()                              #Re-runs function


    if enter_check == 3:                        #User Input = 3, exits function
        exit()
    elif enter_check == 1:                      #User Input = 1, item selection
        print ('Which object would you like to take?')
        print (items_copy)                      #Print item list
        choice = str(input())                   #User Input
        for word in items:                          #Iterates through dictionary that does not change
            if word == choice:                      #If user input matches word in dictionary
                print ('You selected %s' %choice)   #Tells user which item they selected
                if ((item_total + 1) <= 3) and ((item_weight + items[word]) <= 6):      #If the user will be under the item and weight limit if they add this item
                    inventory[word] = items[word]                                       #Add item to user's inventory
                    inventory_copy[word] = items[word]                                  #Add item to copy inventory
                    print ('You now have the following in your inventory:')
                    print (inventory)
                    item_total += 1                                                     #Increase Item total by one
                    #print (item_total)
                    item_weight += inventory[word]                                      #Increase weight by weight of item
                    #print (item_weight)
                    del items_copy[word]                                                #Delete Item from Items Found list
                    add_item()
                elif (item_total + 1) > 3:                              #If item total over limit
                    print ('You cannot pick up anymore items.')
                    drop_item()                                         #Run drop item function
                    add_item()                                          #Run add item function
                elif (item_weight + items[word]) > 6:                   #If total weight over limit
                    print ('That will put you over the weight limit. You cannot pick that item up.')
                    drop_item()
                    add_item()
            elif choice not in items:                           #If choice not one of the items
                print ('That is not one of the items.')
                add_item()
    elif enter_check == 2:                      #User Input = 2 - Drop Item
        drop_item()
        add_item()
    else:                                                                           #User Input = something else
        print ('Sorry that is not a valid response. please enter 1, 2, or 3.')      #Invalid response - try again
        add_item()



def drop_item():                        #Drop Item function
    global item_total
    global item_weight
    print ('Would you like to drop an item? You may be able to pick up another item if you drop something.')
    print ('Press 1 to choose an item to drop. Press 2 to avoid dropping an item.')
    enter_two = input()                 #User Input
    try:
        drop_choice = int(enter_two)    #Checks that input is an integer
    except ValueError:
        print ('Sorry that is not a valid response. Please enter 1, 2, or 3.')      #Invalid response - try again
        drop_item()

    if drop_choice == 1:                                    #If user input = 1
        print ('Which item would you like to drop?')
        print (inventory_copy)                              #Prints User Inventory List
        drop = str(input())                                 #User Input - string
        for option in inventory:                            #Cycles through User Inventory List
            if option == drop:                                          #If user input matches item in Inventory List
                print('You have decided to drop your %s' %option)
                items_copy[option] = inventory[option]                  #Add item to Items Found list
                item_total -= 1                                         #Subtract one from item total
                item_weight -= inventory[option]                        #Subtract item weight from total weight carried
                del inventory_copy[option]                              #Delete item from Copy of User Inventory List
            elif option not in inventory:                   #If user input not in Inventory List
                print('That is not a valid response.')
        for each in inventory_copy:                         #Cycles through each item in Inventory copy
            inventory[each] = inventory_copy[each]          #Sets items in Inventory equal to Inventory Copy to avoid errors when looping through a list while removing items from it
    elif drop_choice == 2:                          #User input = 2
        add_item()                                  #Run Add item function
    else:                                           #Any other user input
        print ('Please press 1 or 2.')
        drop_item()                                 #Re-run drop item function





add_item()
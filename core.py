import sqlite3 as sql

ingredients = 1
instructions = 2

def input_cycle_user(user_input):
    input_list = []

    #Message condition
    if user_input == 1:
        message_input = "\nInsert ingredients: \n--- to quit \nEnter to continue \n"
    elif user_input == 2:
        message_input = "\nInsert instructions: \n--- to quit \nEnter to continue \n"
    else:
        print ("We cooked.... hahaha")

#Loop function for Input user
    while user_input != "":
        user_input = input(message_input)
        
        
        if user_input == "---":
            break
        elif user_input == "":
            pass
        else:
            input_list.append(user_input)
            print (f"Current user_input: {input_list}")
    user_input=", ".join(input_list)
    return user_input



title = input('Name of receipe: \n')

ingredients = input_cycle_user(ingredients) #Input ingredients
instructions = input_cycle_user(instructions) #Input instructions


#Save receipe
save = input("Do you wanna save the receipe: y/n \n")
while True:
    if save == "y" or save == "Y":
        conn = sql.connect("receipes.db")
        cur = conn.cursor()
        try:
            cur.execute("CREATE TABLE receipes(title,ingredients, instructions)")
        except:
            pass

        cur.execute("INSERT INTO receipes (title, ingredients, instructions) VALUES(?, ?, ?)",
                                                                        (title, ingredients, instructions))
        conn.commit()

        cur.close()
        conn.close()
        break
    elif save == "n" or save == "N":
        ingredients_list = []
        instructions_list = []
        print ('Data inserted deleted')
        break
    else:
        print ('Inserted wrong input')

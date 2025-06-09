import sqlite3 as sql

ingredients_list = []
ingredients = None

instructions_list = []
instructions = None


title = input('Name of receipe: \n')

while ingredients != "":
    ingredients = input('\ningredient: \n--- to quit \nEnter to continue \n')
    
    if ingredients == "---":
        break
    elif ingredients == "":
        pass
    else:
        ingredients_list.append(ingredients)
        print (f"Current ingredients: {ingredients_list}")
ingredients=", ".join(ingredients_list)

#Add Instructions
while instructions != "":
    instructions = input('\ninstructions: \n--- to quit \nEnter to continue \n')
    
    if instructions == "---":
        break
    elif instructions == "":
        pass
    else:
        instructions_list.append(instructions)
        print (f"Current instructions: {instructions_list}\n")
instructions=", ".join(instructions_list)

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

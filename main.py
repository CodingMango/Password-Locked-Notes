import os
# checking if a file with name 'Notes_Password.txt' exists,
# if it doesn't, that means that the password has not yet been set.
########################################################################################
file_exists = os.path.exists('Notes_Password.txt')
#print(file_exists)

if not file_exists:
    password_set = False
else:
    password_set = True
########################################################################################
if password_set:
 f = open('Notes_Password.txt', 'r')
 password = f.read()
# print(password)
 f.close()


# if the password has not been set yet
if not password_set:
    setting_password = input("What would you like to set as a password? (Can be changed later manually): ")
    password_set = True
    with open('Notes_Password.txt', 'w') as f:
        f.write(setting_password)
################################################################
else:
    while True:
        ###
        security=input("PASSWORD: ")
        if security != password:
            print("WRONG PASSWORD. TRY AGAIN")
            continue
        if security == password:
            print("SUCCESS!!!")
################################################################################
            def text_cleaner(txt):
                txt.replace(".txt", "")

            current_path = os.getcwd()
            
            dir_path = current_path
            res = []
            for path in os.listdir(dir_path):
                if os.path.isfile(os.path.join(dir_path, path)):
                    res.append(path)
            length = len(res)


            res.remove('main.py')

            for x in res:
                x.replace('.txt', '')
                text_cleaner(x)
            print(" \n The list of notes are: ")

            print(*res, sep= '\n')
            print('\n')
            print("The .txt file named 'Notes_Password.txt' is an auto generated note, kindly don't try to remove any instance of it from the code.")
            print('\n')
            
            
################################################################################

        while True:
         create_view = input("Would you like to view/edit a previously made note, create a new one, delete a note or change the password?(view, create, delete or change): ")
         if create_view == "view":
#PREVIOUS------------------------------------------------------------------------------------------
#if the user wishes to view/edit a previous note.
            search = input("What was the name of the note(case sensitive): ")
            # searching for said file, if it exists it prints its contents, else it asks for create_view again
            search = search + ".txt"

            file_exists = os.path.exists(str(search))
            if file_exists:
                search=str(search)
                print(search)
#####################################################
                f = open(search, 'r')
                content = f.read()
                print(content)
                f.close()
#####################################################
                print("Success! Now you can try again or edit it")
                again_edit=input("Again or Edit: ")
                if again_edit == "again":
                    continue
                elif again_edit == "edit":
                    print(content)
                    edits=input("What would you like to add?: ")
                    with open(search, "a") as f:
#                        f.write('\n')
                        f.write(edits)
            # if the note doesn't exist
            else:
                create_back=input("Couldn't find a note of this name, would you like to create a note or go back to selection?(create or back):")
                if create_back == "back":
                    continue
                elif create_back == "create":
                   while True:
                    createname=input("What would you like to name this note?: ")
                    createname=createname + ".txt"
                    if os.path.exists(str(createname)) == True:
                        print("A note of the name", createname, "already exists! Try again")
                    createname=createname + ".txt"
                    print(createname)
                    create_write=input("what would you like to write?: ")
                    with open(createname, 'w') as f:
                        f.write(create_write)
                    again_quit=input("Would you like to go again or quit(again or anything)")
                    if again_quit == "again":
                        continue
                    else:
                        quit()
         #PREVIOUS DONE ------------------------------------------------------------------

         #CREATE--------------------------------------------------------------------------
         if create_view == "create":
             while True:
                    createname=input("What would you like to name this note?: ")
                    createname=createname + ".txt"
                    if os.path.exists(str(createname)):
                        print("A file of the name", createname, "already exists! Try again")
                        continue

                    print(createname)
                    create_write=input("what would you like to write?: ")
                    with open(createname, 'w') as f:
                        f.write(create_write)
                        again_quit=input("Would you like to go again or quit(again or anything)")
             if again_quit == "again":
                continue

         if create_view == "delete":
            while True:
             delete=input("What is the name of the note you are willing to delete?: ")
             delete = delete + ".txt"
             if os.path.exists(delete):
                 print("Success! A file of this name has been found")
             else:
                 print("No note of that name exists! Please try again")
                 continue
             see_c=input("Would you like to read the contents of this note?(yes or no): ")
             if see_c=="yes":
                  with open(delete, 'r') as f:
                     deletecontent = f.read()
                     print(deletecontent)
                     f.close()
             confirmation=input("Are you sure you wish to delete this note?(yes or no, incase of typo, file won't be deleted):")
             if confirmation == "yes":
              os.remove(delete)
              print("Successfully deleted", delete, ".txt")
         else:
             continue

         if create_view == "change":
            while True:
             change_security=input("OLD PASSWORD: ")
             if change_security != password:
                print("INCORRECT PASSWORD! TRY AGAIN")
                continue
             else:
                 print("SUCCESS")
             new_pass=input("What would you like the new password to be?: ")
             with open('Notes_Password.txt', 'w') as f:
                 f.write(new_pass)
             print('\n')
#comment to make it 170 lines long
#another comment
             print("SUCCESS! Your password is now", new_pass)


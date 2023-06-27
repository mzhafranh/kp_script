def write_to_file(file_name, content):
    with open(file_name, "w") as file:
        file.write(content)

def main():
    try:
        #SETUP
        print("Enter form name")
        form_name = input()
        print("")

        print("Enter the precondition for this test scenario. Press Ctrl + D (Unix/Linux) or Ctrl + Z (Windows) to finish:")
        precondition = sys.stdin.read()
        print("")

        print("Choose form mode")
        print("[1] Add")
        print("[2] Change")
        form_mode = int(input())
        print("")
        
        invalid_input_count = True
        while invalid_input_count:
            print("Enter the number of input fields")
            count_input_fields = input()
            if count_input_fields.isdigit():
                count_input_fields = int(count_input_fields)
                invalid_input_count = False
            else:
                print("[Error] Please input number")
            print("")

        input_field_name_list = ["" for i in range(count_input_fields)]
        input_field_type_list = [0 for i in range(count_input_fields)]
        input_field_max_list = [0 for i in range(count_input_fields)]
        input_field_mandatory_list = [0 for i in range(count_input_fields)]

        #Getting input fields
        for i in range (count_input_fields):
            print("Input field name number " + str(i+1) + ": ")
            input_field_name_list[i] = input()
            print("")
            input_field_type = 0
            while input_field_type != 1 and input_field_type != 2 and input_field_type != 3 and  input_field_type != 4:
                print("Type of input field")
                print("[1] Text")
                print("[2] Image")
                print("[3] List option")
                print("[4] Switch")
                input_field_type = int(input())
                print("")
                if input_field_type == 1:
                    input_field_type_list[i] = input_field_type
                    print("Input character limit for this field. Input 0 if none")
                    input_field_max_list[i] = int(input())
                    print("")
                elif input_field_type == 2:
                    input_field_type_list[i] = input_field_type
                    print("Input max size limit for this field in MB. Input 0 if none")
                    input_field_max_list[i] = int(input())
                    print("")

                elif input_field_type == 3:
                    input_field_type_list[i] = input_field_type
                elif input_field_type == 4:
                    input_field_type_list[i] = input_field_type
                else:
                    print("[Error] Input type incorrect")

            print("Is this field mandatory? 1 Yes, 2 No")
            input_field_mandatory_list[i] = int(input())
            print("")

        #Form mode changes
        if form_mode == 1:
            form_button = "Tambah"
            form_action = "new"
            form_test = "add"
            form_save_button = "Tambah"

        elif form_mode == 2:
            form_button = "Ubah"
            form_action = "changed"
            form_test = "change"
            form_save_button = "Simpan"

        #Generate Steps
        content = ""
        list_test_case = []

        #Type 1 Similarity between Figma and Application
        similarity_data_test = "[Similarity between Figma and Application]\n"
        # list_test_case.append(similarity_data_test)
        # similarity_precondition = precondition.splitlines()
        # for line in similarity_precondition[:-1]:
        #     similarity_data_test += line + "\n"
        similarity_data_test += precondition
        similarity_data_test += "\n"
        similarity_data_test += "STEP\n"
        similarity_data_test += "GIVEN user do PRECONDITION\n"
        similarity_data_test += "WHEN user look at displayed page\n"
        similarity_data_test += "\n"
        similarity_data_test += "EXPECTED RESULT\n"
        similarity_data_test += "THEN user will see similarity between Figma and Application\n\n"

        content += similarity_data_test
        
        #Type 2 Valid Data
        valid_data_test = "[User " + form_test + " " + form_name + " with valid data" +"]\n"
        list_test_case.append(valid_data_test)
        valid_data_test += precondition
        valid_data_test += "\n"
        valid_data_test += "STEP\n"
        valid_data_test += "GIVEN user do PRECONDITION\n"
        valid_data_test += "WHEN user click " + form_button + " button\n"
        for i in range(count_input_fields):
            valid_data_test += "AND user "
            if input_field_type_list[i] == 1:
                valid_data_test += "input " + input_field_name_list[i] + " with valid data\n"
            elif input_field_type_list[i] == 2:
                valid_data_test += "upload " + input_field_name_list[i] + " with valid image\n"
            elif input_field_type_list[i] == 3:
                valid_data_test += "choose " + input_field_name_list[i] + "\n"
            elif input_field_type_list[i] == 4:
                valid_data_test += "toggle Switch On\n"
        valid_data_test += "AND user click on " + form_save_button + "\n"
        valid_data_test += "\n"
        valid_data_test += "EXPECTED RESULT\n"
        valid_data_test += "THEN " + form_action + " " + form_name + " will be saved\n"
        valid_data_test += "AND user can see " + form_action + " " + form_name + " in " + form_name + " list\n"
        valid_data_test += "AND user can see success notification\n\n"

        content += valid_data_test

        #Type 3 invalid data
        for i in range(count_input_fields):
            if input_field_type_list[i] != 4:
                invalid_data_test = "[User " + form_test + " " + form_name + " without filling " + input_field_name_list[i] +"]\n"
                list_test_case.append(invalid_data_test)
                invalid_data_test += precondition
                invalid_data_test += "\n\n"
                invalid_data_test += "STEP\n"
                invalid_data_test += "GIVEN user do PRECONDITION\n"
                invalid_data_test += "WHEN user click " + form_button + " button\n"
                for j in range(count_input_fields):
                    invalid_data_test += "AND user "
                    if i == j:
                        if input_field_type_list[j] == 1:
                            invalid_data_test += "does not input " + input_field_name_list[j] + "\n"
                        elif input_field_type_list[j] == 2:
                            invalid_data_test += "does not upload " + input_field_name_list[j] + "\n"
                        elif input_field_type_list[j] == 3:
                            invalid_data_test += "does not choose " + input_field_name_list[j] + "\n"
                        elif input_field_type_list[j] == 4:
                            invalid_data_test += "toggle Switch Off\n"
                    else:
                        if input_field_type_list[j] == 1:
                            invalid_data_test += "input " + input_field_name_list[j] + " with valid data\n"
                        elif input_field_type_list[j] == 2:
                            invalid_data_test += "upload " + input_field_name_list[j] + " with valid image\n"
                        elif input_field_type_list[j] == 3:
                            invalid_data_test += "choose " + input_field_name_list[j] + "\n"
                        elif input_field_type_list[j] == 4:
                            invalid_data_test += "toggle Switch On\n"
                    
                invalid_data_test += "AND user click on " + form_save_button + "\n"
                invalid_data_test += "\n"
                invalid_data_test += "EXPECTED RESULT\n"

                if input_field_mandatory_list[i] == 1:
                    invalid_data_test += "THEN " + form_action + " " + form_name + " will not be saved\n"
                    invalid_data_test += "AND user will not see " + form_action + " " + form_name + " in " + form_name + " list\n"
                    invalid_data_test += "AND user can see error notification\n\n"
                
                elif input_field_mandatory_list[i] == 2:
                    invalid_data_test += "THEN " + form_action + " " + form_name + " will be saved\n"
                    invalid_data_test += "AND user can see " + form_action + " " + form_name + " in " + form_name + " list\n"
                    invalid_data_test += "AND user can see success notification\n\n"

                content += invalid_data_test
        
        #Type 4 testing constraint
        constraint_check_list = []
        for i in range(len(input_field_max_list)):
            if input_field_max_list[i] != 0:
                constraint_check_list.append(i)

        for i in range(len(constraint_check_list)):
            item_type = "characters" if input_field_type_list[constraint_check_list[i]] == 1 else "MB"
            constraint_data_test = "[User " + form_test + " " + form_name + " with inputting " + input_field_name_list[i] +" with more than " + str(input_field_max_list[constraint_check_list[i]]) + " " + item_type + "]\n"
            list_test_case.append(constraint_data_test)
            constraint_data_test += precondition
            constraint_data_test += "\n"
            constraint_data_test += "STEP\n"
            constraint_data_test += "GIVEN user do PRECONDITION\n"
            constraint_data_test += "WHEN user click " + form_button + " button\n"

            for j in range(count_input_fields):
                constraint_data_test += "AND user "
                if j == constraint_check_list[i]:
                    if input_field_type_list[j] == 1:
                        constraint_data_test += "input " + input_field_name_list[j] + " with more than " +  str(input_field_max_list[constraint_check_list[i]]) + " " + item_type + "\n"
                    elif input_field_type_list[j] == 2:
                        constraint_data_test += "upload " + input_field_name_list[j] + " with more than " +  str(input_field_max_list[constraint_check_list[i]]) + " " + item_type + "\n"
                else:
                    if input_field_type_list[j] == 1:
                        constraint_data_test += "input " + input_field_name_list[j] + " with valid data\n"
                    elif input_field_type_list[j] == 2:
                        constraint_data_test += "upload " + input_field_name_list[j] + " with valid image\n"
                    elif input_field_type_list[j] == 3:
                        constraint_data_test += "choose " + input_field_name_list[j] + "\n"
                    elif input_field_type_list[j] == 4:
                        constraint_data_test += "toggle Switch On\n"
                
                    constraint_data_test += "AND user click on " + form_save_button + "\n"
                    constraint_data_test += "\n"
                    constraint_data_test += "EXPECTED RESULT\n"
                    constraint_data_test += "THEN " + form_action + " " + form_name + " will not be saved\n"
                    constraint_data_test += "AND user will not see " + form_action + " " + form_name + " in " + form_name + " list\n"
                    constraint_data_test += "AND user can see error notification\n\n"

                    content += constraint_data_test

        #Type 5 click Batal
        batal_data_test = "[User " + form_test + " " + form_name + " with clicking Batal]\n"
        list_test_case.append(batal_data_test)
        batal_data_test += precondition
        batal_data_test += "\n"
        batal_data_test += "STEP\n"
        batal_data_test += "GIVEN user do PRECONDITION\n"
        batal_data_test += "WHEN user click " + form_button + " button\n"
        for i in range(count_input_fields):
            batal_data_test += "AND user "
            if input_field_type_list[i] == 1:
                batal_data_test += "input " + input_field_name_list[i] + " with valid data\n"
            elif input_field_type_list[i] == 2:
                batal_data_test += "upload " + input_field_name_list[i] + " with valid image\n"
            elif input_field_type_list[i] == 3:
                batal_data_test += "choose " + input_field_name_list[i] + "\n"
            elif input_field_type_list[i] == 4:
                batal_data_test += "toggle Switch On\n"
        batal_data_test += "AND user click Batal\n"
        batal_data_test += "\n"
        batal_data_test += "EXPECTED RESULT\n"
        batal_data_test += "THEN " + form_action + " " + form_name + " will not be saved\n"
        batal_data_test += "AND user will return to previous page\n\n"
        content += batal_data_test

        #List the test cases

        test_cases = "[=== === === === === TEST LIST === === === === ===]\n\n"
        for test_case in list_test_case:
            test_cases += test_case
        test_cases += "\n"
        test_cases += "[=== === === === === TEST CASE === === === === ===]\n\n"

        #Log into console
        print("Input field name list")
        print(input_field_name_list)
        print("Input field type list")
        print(input_field_type_list)
        print("Input field mandatory list")
        print(input_field_mandatory_list)
        print("Input field max list")
        print(input_field_max_list)

        #Write into File
        result = test_cases + content
        write_to_file("task.txt", result)
        print("Task generated to task.txt successfully!")
    
    except KeyboardInterrupt:
        print("\nUser exited the program.")

if __name__ == "__main__":
    import sys
    main()
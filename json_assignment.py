#!/usr/bin/env python
# coding: utf-8


import json
import os
import argparse
from os.path import exists,join
import sys
import traceback
import pdb
import subprocess

def user_name1():
    try:
        print('Please enter your first name and last name')
        fname=input('\nFirst Name : ')
        lname=input('\nLast Name : ')
        print('\nHello '+fname.lower().capitalize()+' '+lname.lower().capitalize()+'!\n')
        return fname,lname
    except Exception:
        traceback.print_exc(file=sys.stdout)

def user_access(fname,lname):
    try:
        admin_flag = False
        resident_flag = False
        for x in data["people"]:
            if fname.lower()==x["first_name"].lower() and lname.lower()==x["last_name"].lower():
                if "Admin" in x["roles"]:
                    print("You have admin and resident access.\n")
                    admin_flag = True
                    resident_flag = True
                else: 
                    print("You have resident access.\n")
                    resident_flag = True
        if admin_flag == False and resident_flag == False: 
            print(f"You are not a registered user. '{fname}' '{lname}' is the name you have entered.\n") 
            print("You can re-enter your name or continue without admin or resident access.\n")
        return admin_flag,resident_flag
    except Exception:
        traceback.print_exc(file=sys.stdout)

def choice1_func(first_name,last_name,admin_flag,resident_flag):
    try:
        subprocess.call('cls',shell=True)
        print('Choose one of the following options')
        print('1. Admin \n2. Resident \n3. Input a unit number and view a list of all users and devices in the given unit \n4. Information about a user. Input first name and last name \n5. Re-enter your name \n6. Logout and exit')
        choice = "Wrong"
        while choice not in {'1','2','3','4','5','6'}:
            choice = input("Select an option ")
            if choice =='1':
                if admin_flag==False:
                    print('\nYou do not have admin access. Please choose another option')
                    choice1_func(first_name,last_name,admin_flag,resident_flag)
                else:
                    admin_func(first_name,last_name,admin_flag,resident_flag)
            elif choice =='2':
                if resident_flag==False:
                    print('\nYou do not have resident access. Please choose another option')
                    choice1_func(first_name,last_name,admin_flag,resident_flag)
                else:
                    resident_func(first_name,last_name,admin_flag,resident_flag)
            elif choice =='3':
                print('\nYou have selected option 3')
                view_unit(first_name,last_name,admin_flag,resident_flag)
            elif choice =='4':
                print('\nYou have selected option 4')
                user_info(first_name,last_name,admin_flag,resident_flag)
            elif choice =='5':
                print("\nDo you wish to re-enter your name?(Y/N)")
                option = confirm_func()
                if option=='y':
                    fname,lname=user_name1()
                    
                    admin_flag,resident_flag=user_access(fname,lname)
                    choice1_func(first_name,last_name,admin_flag,resident_flag)
                    
                elif option=='n':
                    choice1_func(first_name,last_name,admin_flag,resident_flag)
                    break
            elif choice =='6':
                print("\nDo you wish to exit the program?(Y/N)")
                option1 = confirm_func()
                if option1=='y':
                    
                    # if modif==True:
                    #     if file_exists:
                    #         os.remove('property_data_changes.json')
                    #         with open("property_data_changes.json", "w") as outfile:
                    #             json.dump(data, outfile)
                    #     else:
                    #         with open("property_data_changes.json", "w") as outfile:
                    #             json.dump(data, outfile)   
                    #     print('\nThank you for using our application')
                    # else:
                    print('\nThank you for using our application')
                        
                elif option=='n':
                    choice1_func(first_name,last_name,admin_flag,resident_flag)
                    break
            else :
                print("\nPlease enter a number between 1 to 6")
    except Exception:
        traceback.print_exc(file=sys.stdout)
   
    

def admin_func(first_name,last_name,admin_flag,resident_flag):
    try:
        print('Choose one of the following options')
        print('1. Move in residents. \n2. Move out residents. \n3. View residents in a unit. \n4. Control admin accessible devices \n5. Go to previous menu.')
        admin_choice='Wrong'
        
        while admin_choice not in {'1','2','3','4','5'}:
            admin_choice = input("Select an option ")
            if admin_choice =='1':
                movein_func(first_name,last_name,admin_flag,resident_flag)
            elif admin_choice =='2':
                moveout_func(first_name,last_name,admin_flag,resident_flag)
            elif admin_choice =='3':
                admin_view(first_name,last_name,admin_flag,resident_flag)
            elif admin_choice =='4':
                admin_control(first_name,last_name,admin_flag,resident_flag)
            elif admin_choice =='5':
                choice1_func(first_name,last_name,admin_flag,resident_flag)
                break
            else :
                print("Please enter a number between 1 to 5")
    except Exception:
        traceback.print_exc(file=sys.stdout)
            
def resident_func(first_name,last_name,admin_flag,resident_flag):
    
    
    try:
        print('Choose one of the following options')
        print('1. See information about yourself. \n2. See devices that are associated with your unit. \n3. Go to previous menu.')
        resident_choice='Wrong'
        while resident_choice not in {'1','2','3'}:
            resident_choice = input("Select an option ")
            if resident_choice =='1':
                
                resident_info(first_name,last_name,admin_flag,resident_flag)
            elif resident_choice =='2':
                
                resident_device(first_name,last_name,admin_flag,resident_flag)
            elif resident_choice =='3':
                
                choice1_func(first_name,last_name,admin_flag,resident_flag)
                break
                              
            else :
                print("Please enter a number between 1 to 3")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        
def view_unit(first_name,last_name,admin_flag,resident_flag):
    try:
        unit_choice = "Wrong"
        while unit_choice.isdigit() is False or int(unit_choice) not in unit_set:
            unit_choice = input("Enter unit number ")
            print("\nIf you wish to return to previous menu enter nothing into the input and submit \n")
            if unit_choice=='' :
                choice1_func(first_name,last_name,admin_flag,resident_flag)
                break
            elif unit_choice.isdigit() is False or int(unit_choice) not in unit_set:
                print("\nEnter a valid unit number ")
            else:
                print('Choose one of the following options \n')
                print('1. Residents in the given unit \n2. Devices in the given unit \n3. Return to previous menu \n')
                choice = "Wrong"
                while choice not in {'1','2','3'}:
                    choice = input("Select an option ")
                    if choice =='1':
                        for i in data["people"]:
                            if i["unit"]==unit_choice:
                                print(f'{i["first_name"]} {i["last_name"]} is a resident of unit {unit_choice}')
                        view_unit(first_name,last_name,admin_flag,resident_flag)
                    elif choice =='2':
                        for i in data["devices"]:
                            x= (data["devices"][i])
                            for j in list(range(len(x))):
                                if (x[j]["unit"]) ==int(unit_choice):
                                    print(f'{i.capitalize()[:-1]} with id {x[j]["id"]} and {x[j]["model"]} model is available in unit {unit_choice}')
                        view_unit(first_name,last_name,admin_flag,resident_flag)
                    elif choice =='3':
                        choice1_func(first_name,last_name,admin_flag,resident_flag)
                        break
                    else:
                        print("\nPlease enter a number between 1 to 3")
    except Exception:
        traceback.print_exc(file=sys.stdout)
                    
def user_info(first_name,last_name,admin_flag,resident_flag):
    try:
        admin_flag1 = False
        resident_flag1 = False
        while resident_flag1==False:
            
            print('Please enter the first name and last name of the user')
            fname1=input('\nFirst Name : ')
            lname1=input('\nLast Name : ')
            if fname1=='' and lname1=='':
                choice1_func(first_name,last_name,admin_flag,resident_flag)
                break
            for x in data["people"]:
                if fname1.lower()==x["first_name"].lower() and lname1.lower()==x["last_name"].lower():
                    if "Admin" in x["roles"]:
                        print('Choose one of the following options \n')
                        print('1. Roles of the given user \n2. Unit information of the given user \n3. Devices controlled by the given user \n4. Return to previous menu \n')
                        choice = "Wrong"
                        while choice not in {'1','2','3','4'}:
                            choice = input("Select an option ")
                            if choice =='1':
                                print(f'{x["first_name"]} {x["last_name"]} has the roles of admin and resident.\n')
                                user_info(first_name,last_name,admin_flag,resident_flag)
                            elif choice =='2':
                                print(f'{x["first_name"]} {x["last_name"]} is a resident of unit {x["unit"]}\n')
                                print(f'The following is all the information regarding unit {x["unit"]}\n')
                                resident_access_devices=unit_info(x["unit"])
                                user_info(first_name,last_name,admin_flag,resident_flag)
                            elif choice=='3':
                                resident_access_devices=unit_info(x["unit"])
                                resident_access_devices.extend(admin_access_devices)
                                print(f'{x["first_name"]} {x["last_name"]} can control the following devices\n')
                                for i in resident_access_devices:
                                    print(i)
                                user_info(first_name,last_name,admin_flag,resident_flag)
                            elif choice=='4':
                                choice1_func(first_name,last_name,admin_flag,resident_flag)
                                break
                            else:
                                 print("\nPlease enter a number between 1 to 4")
                        admin_flag1 = True
                        resident_flag1 = True
                    else:
                        print('Choose one of the following options \n')
                        print('1. Roles of the given user \n2. Unit information of the given user \n3. Devices controlled by the given user \n4. Return to previous menu \n')
                        choice = "Wrong"
                        while choice not in {'1','2','3','4'}:
                            choice = input("Select an option ")
                            if choice =='1':
                                print(f'{x["first_name"]} {x["last_name"]}) has the role of resident.')
                                user_info()
                            elif choice =='2':
                                print(f'{x["first_name"]} {x["last_name"]} is a resident of unit {x["unit"]}')
                                print(f'The following is all the information regarding unit {x["unit"]}\n')
                                resident_access_devices=unit_info(x["unit"])
                                user_info()
                            elif choice=='3':
                                resident_access_devices=unit_info(x["unit"])
                                print(f'{x["first_name"]} {x["last_name"]} can control the following devices\n')
                                for i in resident_access_devices:
                                    print(i)
                                user_info()
                            elif choice=='4':
                                choice1_func(first_name,last_name,admin_flag,resident_flag)
                                break
                            else:
                                 print("\nPlease enter a number between 1 to 4")
                        resident_flag1 = True
                    
            if admin_flag1 == False and resident_flag1 == False: 
                print(f"The name you have given is not a registered user. '{fname1}' '{lname1}' is the name you have entered.\n") 
                print("Please re-enter a valid user name\n")
                print("If you wish to return to previous menu enter nothing into the first name and last name inputs and submit \n")
    except Exception:
        traceback.print_exc(file=sys.stdout)

def movein_func(first_name,last_name,admin_flag,resident_flag):
    try:
        global modif
        print('Please enter first name\n')
        fname2=input("First Name ").title()
        print('Please enter last name\n')
        lname2=input("Last Name ").title()
        print('Please enter unit number\n')
        unit_number=input("Unit Number ")
        while not (unit_number.isdigit()):
            print('Please enter a valid unit number')
            unit_number=input("Unit Number ")
            
        print('Please select the roles to grant\n')
        print('1. Admin and Resident \n2. Resident \n')
        choice ="W"
        while choice not in {'1','2'}:
            choice = input("Option ")
            if choice =='1':
                print(f'{fname2} {lname2} have been granted Admin and Resident access \n')
                roles=["Admin", "Resident"]
            elif choice =='2':
                print(f'{fname2} {lname2} have been granted Resident access \n')
                roles=["Resident"]
            else:
                print("\nPlease enter a number 1 or 2")
        x={"first_name": fname2, "last_name": lname2,"unit": unit_number,"roles": roles}
        
        
        print(f'Are you sure you want to move in {fname2} {lname2} into unit {unit_number} ? (Y/N) \n')
        choice1=confirm_func()
        if choice1=='y':
            print('Successfully added\n')
            data['people'].append(x)
            admin_func(first_name,last_name,admin_flag,resident_flag)
            modif=True
        else:
            print('User not added. Returning to previous menu')
            admin_func(first_name,last_name,admin_flag,resident_flag)
    except Exception:
        traceback.print_exc(file=sys.stdout)
        
        
def moveout_func(first_name,last_name,admin_flag,resident_flag):
    try:
        global modif
        print('Please enter first name\n')
        fname3=input("First Name ").title()
        print('Please enter last name\n')
        lname3=input("Last Name ").title()
        counter=0
        check=False
        for x in data['people']:
            if x['first_name']==fname3 and x['last_name']==lname3:
                print(f'Are you sure you want to move out {fname3} {lname3} from database? (Y/N) \n')
                choice1=confirm_func()
                if choice1=='y':
                    print(f'Successfully removed {fname3} {lname3} \n')
                    data['people'].pop(counter)
                    modif=True
                    check=True
                    return admin_func(first_name,last_name,admin_flag,resident_flag)
                    
                    break
                else:
                    print('User not removed. Returning to previous menu')
                    check=True
                    return admin_func(first_name,last_name,admin_flag,resident_flag)
            counter+=1  
        if check==False:
            print('Name not found. Returning to previous menu\n')
            return admin_func(first_name,last_name,admin_flag,resident_flag)
    except Exception:
        traceback.print_exc(file=sys.stdout)
    
def admin_view(first_name,last_name,admin_flag,resident_flag):
    try:
        unit_choice = "Wrong"
        while unit_choice.isdigit() is False or int(unit_choice) not in unit_set:
            unit_choice = input("Enter unit number ")
            print("\nIf you wish to return to previous menu enter nothing into the input and submit \n")
            if unit_choice=='' :
                choice1_func(first_name,last_name,admin_flag,resident_flag)
                break
            elif unit_choice.isdigit() is False or int(unit_choice) not in unit_set:
                print("\nEnter a valid unit number \n")
                admin_view(first_name,last_name,admin_flag,resident_flag)
            else:
                for i in data["people"]:
                    if i["unit"]==unit_choice:
                        print(f'{i["first_name"]} {i["last_name"]} is a resident of unit {unit_choice}\n')
                admin_view(first_name,last_name,admin_flag,resident_flag)
    except Exception:
        traceback.print_exc(file=sys.stdout)

def admin_control(first_name,last_name,admin_flag,resident_flag):
    try:
        print("Choose one of the options.")
        print("1. View all the devices you can control with admin access. \n2. Return to previous menu \n")
        choice = "Wrong"
        while choice not in {'1','2'}:
            choice = input("Select an option ")
            if choice =='1':
                print('You can access the following devices with admin access\n')
                for i in admin_access_devices:
                    print(i)
                    print('\n')
                admin_control(first_name,last_name,admin_flag,resident_flag)
            elif choice=='2':
                choice1_func(first_name,last_name,admin_flag,resident_flag)
                break
            else:
                print("\nPlease enter a number 1 or 2")
    except Exception:
        traceback.print_exc(file=sys.stdout)
            
            
def resident_info(first_name,last_name,admin_flag,resident_flag):
    try:
        for x in data["people"]:
            if first_name.lower()==x["first_name"].lower() and last_name.lower()==x["last_name"].lower():
                if "Admin" in x["roles"]:
                    print('Choose one of the following options \n')
                    print('1. Your roles \n2. Information about your unit \n3. Devices you can control \n4. Return to previous menu \n')
                    choice = "Wrong"
                    while choice not in {'1','2','3','4'}:
                        choice = input("Select an option ")
                        if choice =='1':
                            print('You have the roles of admin and resident.\n')
                            resident_info(first_name,last_name,admin_flag,resident_flag)
                        elif choice =='2':
                            print(f'You are currently a resident of unit {x["unit"]}\n')
                            print(f'The following is all the information regarding unit {x["unit"]}\n')
                            resident_access_devices=unit_info(x["unit"])
                            resident_info(first_name,last_name,admin_flag,resident_flag)
                        elif choice=='3':
                            resident_access_devices=unit_info(x["unit"])
                            resident_access_devices.extend(admin_access_devices)
                            print('You can control the following devices\n')
                            for i in resident_access_devices:
                                print(i)
                            resident_info(first_name,last_name,admin_flag,resident_flag)
                        elif choice=='4':
                            choice1_func(first_name,last_name,admin_flag,resident_flag)
                            break
                        else:
                            print("\nPlease enter a number between 1 to 4")
                        
                else:
                    print('Choose one of the following options \n')
                    print('1. Your roles \n2. Information about your unit \n3. Devices you can control \n4. Return to previous menu \n')
                    choice = "Wrong"
                    while choice not in {'1','2','3','4'}:
                        choice = input("Select an option ")
                        if choice =='1':
                            print('You have the role of a resident')
                            resident_info(first_name,last_name,admin_flag,resident_flag)
                        elif choice =='2':
                            print(f'You are currently a resident of unit {x["unit"]}')
                            print(f'The following is all the information regarding unit {x["unit"]}\n')
                            resident_access_devices=unit_info(x["unit"])
                            resident_info(first_name,last_name,admin_flag,resident_flag)
                        elif choice=='3':
                            resident_access_devices=unit_info(x["unit"])
                            print('You can control the following devices\n')
                            for i in resident_access_devices:
                                print(i)
                            resident_info(first_name,last_name,admin_flag,resident_flag)
                        elif choice=='4':
                            choice1_func(first_name,last_name,admin_flag,resident_flag)
                            break
                        else:
                            print("\nPlease enter a number between 1 to 4")
    except Exception:
        traceback.print_exc(file=sys.stdout)
                    
                    
def resident_device(first_name,last_name,admin_flag,resident_flag):
    try:
        for x in data["people"]:
            if first_name.lower()==x["first_name"].lower() and last_name.lower()==x["last_name"].lower():
                if "Admin" in x["roles"]:
                    resident_access_devices=unit_info(x["unit"])
                    resident_access_devices.extend(admin_access_devices)
                    print('You can control the following devices\n')
                    for i in resident_access_devices:
                        print(i)
                    
                    
                else :
                    resident_access_devices=unit_info(x["unit"])
                    print('You can control the following devices\n')
                    for i in resident_access_devices:
                        print(i)
                        
            return resident_func(first_name,last_name,admin_flag,resident_flag)
    except Exception:
        traceback.print_exc(file=sys.stdout)
        

def unit_info(unit_choice = "Wrong"):
    try:
        resident_access_devices=[]
        if unit_choice.isdigit() is False or int(unit_choice) not in unit_set:
                print("\nEnter a valid unit number ")
        
        else:
            for i in data["people"]:
                if i["unit"]==unit_choice:
                    print(f'{i["first_name"]} {i["last_name"]} is a resident of unit {unit_choice}')
            for i in data["devices"]:
                x= (data["devices"][i])
                for j in list(range(len(x))):
                    if (x[j]["unit"]) ==int(unit_choice):
                        print(f'{i.capitalize()[:-1]} with id {x[j]["id"]} and {x[j]["model"]} model is available in unit {unit_choice}')
                        y=(f'{i.capitalize()[:-1]} with id {x[j]["id"]} and {x[j]["model"]} model')
                        resident_access_devices.append(y)
        return resident_access_devices
    except Exception:
        traceback.print_exc(file=sys.stdout)
                
    
def confirm_func():
    try:
    
        option = 'WR'
        while option.lower() not in {'y','n'}:
            option = input("Y/N ")
            if option.lower()=='y':
                return 'y'
            elif option.lower()=='n':
                return 'n'
            else :
                print("Please enter either Y or N")
    except Exception:
        traceback.print_exc(file=sys.stdout)



def main():
    try:
        
        parser = argparse.ArgumentParser(description = 'Run Property data changes') 
        parser.add_argument('fname',  help = 'Enter first name')
        parser.add_argument('lname',  help = 'Enter last name')
        
        args = parser.parse_args()
        # import pdb;pdb.set_trace()
        first_name = args.fname 
        last_name = args.lname
        global data, unit_set,modif,admin_access_devices, file_exists
        # if first_name.isalpha() and last_name.isalpha():
        file_exists=exists(join(os.getcwd(),'property_data_changes.json'))
        if file_exists:
            with open("property_data_changes.json", "r") as read_file:
                data = json.load(read_file)
        else:
            with open("property_data.json", "r") as read_file:
                data = json.load(read_file)
        
        modif = False
        unit_list=[]
        for i in data["devices"]:
            x= (data["devices"][i])
            for j in list(range(len(x))):
                unit_list.append((x[j]["unit"]))
        for i in data["people"]:
            y=int((i["unit"]))
            unit_list.append(y)
            unit_set=set(unit_list) 
    
        admin_access_devices=[]
        for i in data["devices"]:
            x= (data["devices"][i])
            for j in list(range(len(x))):
                if (x[j]["admin_accessible"]) =="true":
                    y=(f'{i.capitalize()[:-1]} with id {x[j]["id"]} and {x[j]["model"]} model in unit {x[j]["unit"]}')
                    admin_access_devices.append(y)
                    
        print(f'Welcome to {data["name"]}! \nAddress: \n{data["address"]["address_line_1"]} \n{data["address"]["city"]} \n{data["address"]["state"]} \n{data["address"]["zip"]} ')
        admin_flag,resident_flag = user_access(first_name,last_name)
        choice1_func(first_name,last_name,admin_flag,resident_flag)
        read_file.close()
    except Exception:
        traceback.print_exc(file=sys.stdout)



if __name__ == "__main__":
    try:
        main()
    except Exception as er:
        print("Error in main function: Error: ", er)
    finally:
        
        if modif==True:
            if file_exists:
                os.remove('property_data_changes.json')
                with open("property_data_changes.json", "w") as outfile:
                    json.dump(data, outfile)
            else:
                with open("property_data_changes.json", "w") as outfile:
                    json.dump(data, outfile)   
          
        print("Program execution complete")
        







"""
Complete CMS Project
"""

"""
Intializing Different customer lists:
Id_list,name_list,age_list and mob_list

"""
id_list=[] #Empty customer id list
name_list=[] #Empty customer name list
age_list=[] #Empty customer age list
mobile_list=[] #Empty customer mobile list


def count(cnt,value):  #count function
    c=0
    for i in range(len(cnt)):
        if cnt[i]==value:
            c=c+1
    return(c)

def index(ind,value):  #index function
    for i in range(len(ind)):
        if ind[i]==value:
            return i


# """For adding Customer information in all four lists(Id_list,name_list,age_list and mob_list)"""
def addcust(id,name,age,mobile):
    id_list.append(id)
    name_list.append(name)
    age_list.append(age)
    mobile_list.append(mobile)

# """For search the information of customer that is store in different lists(Id_list,name_list,age_list and mob_list)"""
def search_cust_Id(id): #search by id
    # i=id_list.index(id)
    i = index(id_list,id)
    return i

def search_cust_name(name): #search by name
    while(1):
        if name not in name_list: #if name_list is empty
            print("This name is not present in our data ")
            break

        else:  #if name_list is not empty
            for i in name_list:
                if i==name:    #if name is found in name_list
                    # count_name=name_list.count(name)  #here we check how many times name is present in name_list
                    count_name = count(name_list,name)
                    if count_name==1:  # if name is present only one time
                        # i=name_list.index(name)
                        i=index(name_list,name)
                        return i

                    elif count_name>=2:  #if name is present more than one time
                        for i in range(len(name_list)):
                            if name_list[i]==name:
                                show_cust(i)
                        #now we check the name with mobile or id
                        id_mob=input("""Please give id or mobile number so that we can verify you:
                         Enter "1" for id 
                         Enter "2" for mobile number
                         Enter your choice(1/2): """)
                        if id_mob=="1":   #if we want to search with id
                            id=input("Enter your id: ")
                            # i=id_list.index(id)
                            i=index(id_list,id)
                            return i

                        elif id_mob=="2": #if we want to search with mobile number
                            mob=input("Enter mobile number: ")
                            # i=mobile_list.index(mob)
                            i=index(mobile_list, mob)
                            return i

                        else:  #if user enter wrong choice
                            print("please enter valid data")

def search_cust_age(age):  #search by age
    while(1):
        if age not in age_list:   #if age not present in agelist
            print("The given data is not present in our data")
            break

        else:   #if age present in agelist
            # count_age=age_list.count(age)   #here we count how many times age present in age_list
            count_age=count(age_list,age)
            if count_age==1:  #if age is present only one time
                # i=age_list.index(age)
                i=index(age_list,age)
                return i


            elif count_age >= 2:   #if age present more than one time
                for i in range(len(age_list)):
                    if age_list[i] == age:
                        show_cust(i)
                id_mob = input("""Please give id or mobile number so that we can verify you:
                 Enter "1" for id 
                 Enter "2" for mobile number
                 Enter your choice(1/2): """)  #here we want to search customer detail with id or mobile
                if id_mob == "1":  #if we want to search with id
                    id = input("Enter your id: ")
                    # i = id_list.index(id)
                    i=index(id_list,id)
                    return i

                elif id_mob == "2":   #if we want to search with mobile
                    mob = input("Enter mobile number: ")
                    # i = mobile_list.index(mob)
                    i=index(mobile_list,mob)
                    return i

                else:
                    print("please enter valid data")

    # i=age_list.index(age)
    # return i



def search_cust_mob(mob):  #search by mobile number
    while(1):

        if mob not in mobile_list:   #if mobile number is not present in mobile number
            print("Given mobile number is not our data")
            break

        else:
            # count_mob=mobile_list.count(mob)
            count_mob=count(mobile_list,mob)
            if count_mob==1:
                # i=mobile_list.index(mob)
                i=index(mobile_list,mob)
                return i
            elif count_mob>=2:
                for i in range(len(mobile_list)):
                    if mobile_list[i] == mob:
                        show_cust(i)
                id=input("Please enter customer ID: ")
                # i=id_list.index(id)
                i=index(id_list,id)
                return i
            else:
                print("Invalid input")

# """For delete the information of customer from all four lists(Id_list,name_list,age_list and mob_list)"""
def delete_cust_id(id):
    i = index(id_list,id)
    id_list.pop(i)
    name_list.pop(i)
    age_list.pop(i)
    mobile_list.pop(i)

def delete_cust_name(name):
    while(1):
        if name not in name_list:  #if name not found in name_list
            print("Given name not in our data")
            break

        else:
            # count_name=name_list.count(name)
            count_name=count(name_list,name)    #count how many times name is present in name_list
            if count_name==1: #if name is present in name_list only for one time
                # i=name_list.index(name)
                i=index(name_list,name)  #fina indext of matching name in name_list
                id_list.pop(i)
                name_list.pop(i)
                age_list.pop(i)
                mobile_list.pop(i)
                break
            elif count_name>=2:
                for i in range(len(name_list)):
                    if name_list[i] == name:
                        show_cust(i)
                id_mob=input("""Please enter id or mobile number so that we delete the original customer:
                Enter "1" for id
                Enter "2" for mobile number
                Enter your choice(1/2): """)
                if id_mob=="1":
                    id=input("Enter ID: ")
                    delete_cust_id(id)
                    break
                elif id_mob=="2":
                    mob=input("Enter mobile number: ")
                    delete_cust_mob(mob)
                    break
                else:
                    print("Invalid input")


def delete_cust_age(age):
    while(1):
        if age not in age_list:
            print("Given age not in our data")
        else:
            # count_age=age_list.count(age)
            count_age=count(age_list,age)
            if count_age==1:
                # i=age_list.index(age)
                i=index(age_list,age)
                id_list.pop(i)
                name_list.pop(i)
                age_list.pop(i)
                mobile_list.pop(i)
                break
            elif count_age>=2:
                for i in range(len(age_list)):
                    if age_list[i] == age:
                        show_cust(i)
                id_mob=input("""Please enter id or mobile number so that we delete the original customer:
                Enter"1" for id
                Enter "2" for mobile number
                Enter your choice(1/2): """)
                if id_mob=="1":
                    id=input("Enter ID: ")
                    # i=id_list.index(id)
                    delete_cust_id(id)
                    break
                elif id_mob=="2":
                    mob=input("Enter mobile number: ")
                    # i=mobile_list.index(mob)
                    delete_cust_mob(mob)
                    break
                else:
                    print("Invalid input")



def delete_cust_mob(mob):
    while(1):

        if mob not in mobile_list:
            print("The Given number not present in our data")
            break
        else:
            # count_mob=mobile_list.count(mob)
            count_mob=count(mobile_list,mob)
            if count_mob==1:
                i=mobile_list.index(mob)
                id_list.pop(i)
                name_list.pop(i)
                age_list.pop(i)
                mobile_list.pop(i)
                break

            elif count_mob>=2:
                for i in range(len(mobile_list)):
                    if mobile_list[i] == mob:
                        show_cust(i)
                id=input("Please enter customer id Whose information is to be deleted: ")
                # i=id_list.index(id)
                delete_cust_id(id)
                break
            else:
                print("Invalid input")





# """For modify the information of customer from all four lists(Id_list,name_list,age_list and mob_list)"""
def modify_cust(id,name,age,mobile):
    i=id_list.index(id)
    id_list[i]=id
    name_list[i]=name
    age_list[i]=age
    mobile_list[i]=mobile
def modify_cust_name(id,name):
    i=id_list.index(id)
    name_list[i]=name
def modify_cust_age(id,age):
    i=id_list.index(id)
    age_list[i]=age
def modify_cust_mob(id,mob):
# def modify_cust_mob(mob_P,mob):
    i=id_list.index(id)
    # i=mobile_list.index(mob_P)
    mobile_list[i]=mob

#PL
# """For display the information of customer according to given information"""
def show_cust(i):
    print("Id is: ",id_list[i],", Name is: ",name_list[i],", Age is: ",age_list[i],"and Mobile number is: ",mobile_list[i])

# """For checking that the given input is in valid range or not"""
def check_id():
    while (1):
        id = input("Enter id:")
        if (id not in id_list):
            return id
        else:
            print("Duplicate id")

def check_name():
    while(1):
        name=input("Enter customer name: ")
        if name.isalpha():
            return name
            break
        else:
            print("Invalid Name")

def check_age():
    while(1):
        while(1):
            try:
               age=int(input("Enter customer age: "))
               break

            except Exception:
                print("Enter age in whole number only which is less than 102 ")


        # if age.isdecimal():
            # if len(age)<=2:
        if age<=101:
            return age
            break
        else:
            print("Enter valid age")

def check_mob():
    while(1):
        mob=input("Enter Customer Mobile Number: ")
        if mob.isdecimal():
            if len(mob)==10:
                return mob
            else:
                print("Enter mobile number in range 10")
        else:
            print("Invalid mobile number")
# """For infinite loop"""
while True:

    # """for the choice that user what service want with this CMS"""
    ch=input("""    Enter 1 for add cust, 
    Enter 2 for search cust ,
    Enter 3 for delete cust, 
    Enter 4 for modify cust, 
    Enetr 5 for show cust, 
    Enetr 6 for exit from CMS,
    Enter your choice: """)

    # """for adding customer"""
    if ch=="1":
        id=check_id()
        name=check_name()
        age=check_age()
        mobile=check_mob()
        addcust(id,name,age,mobile)
        print("Customer add Successfully")

    # """for search the customer details"""
    elif ch=="2":
        while(1):
            # id=input("Enter id: ")
            # if id in id_list:
                s_ch=input("""\n    Enter "1" for search by ID
    Enter "2" for search by name
    Enter "3" for search by age
    Enter "4" for search by mobile number
    Enter your choice: """)

                if s_ch=="1":
                    id=input("Enter customer id: ")
                    i=search_cust_Id(id)
                    show_cust(i)
                    break

                elif s_ch=="2":
                    name=input("Enter your name: ")
                    i=search_cust_name(name)
                    show_cust(i)
                    break
                elif s_ch=="3":
                    age=int(input("Enter your age: "))
                    i=search_cust_age(age)
                    show_cust(i)
                    break

                elif s_ch=="4":
                    mob=input("Enter your mobile number: ")
                    i=search_cust_mob(mob)
                    show_cust(i)
                    break
                else:
                    print("You entered wrong choice")
            # else:
            #     print("Id not exist")

        # show_cust(i)

    # """for the deletion of customer details"""
    elif ch=="3":
        while(1):
            id=input("Enter id: ")
            if id in id_list:
                s_ch = input("""Enter "1" for delete by ID
                        Enter "2" for delete by name
                        Enter "3" for delete by age
                        Enter "4" for delete by mobile number
                        Enter your choice: """)

                if s_ch=="1":
                    id=input("Enter id of customer: ")
                    delete_cust_id(id)
                    break
                elif s_ch=="2":
                    name=input("Enter name of customer: ")
                    delete_cust_name(name)
                    break
                elif s_ch=="3":
                    age=int(input("Enter age of customer: "))
                    delete_cust_age(age)
                    break
                elif s_ch=="4":
                    mob=input("Enter mobile number: ")
                    delete_cust_mob(mob)
                    break
                else:
                    print("Wrong choice")

                print("Customer deleted Successfully")
            else:
                print("Id not exist")

        # print("Customer deleted Successfully")


    # """for the updation of customer details"""
    elif ch=="4":
        while(1):
            id = input("Enter id of customer: ")
            if id in id_list:
                choice=input("""What you want to update:
                Enter '1' for name:
                Enter '2' for age:
                Enter '3' for mobile number:
                Enter '4' for name,age,mobile
                Enter your choice(1/4): """)
                if choice=="1":
                    name=input("Enter updated name: ")
                    modify_cust_name(id,name)
                    break
                elif choice=="2":
                    age= int(input("Enter updated age: "))
                    modify_cust_age(id,age)
                    break
                elif choice=="3":
                    # mob_P=input("privious mobile no: ")
                    mob= input("Enter updated mobile: ")
                    modify_cust_mob(id,mob)
                    # modify_cust_mob(mob_P,mob)

                    break
                elif choice=="4":
                    name=input("Enter updated name: ")
                    age=int(input("Enter updated age: "))
                    mobile=input("Enter  updated mobile number: ")
                    modify_cust(id,name,age,mobile)
                    break
                # print("Customer details is modify Successfully")

                else:
                    print("Invalid choice")
                print("Customer details is modify Successfully")

            else:
                print("Id is not present ,try again")
    # """for display all customer of list"""
    elif ch=="5":
        flag=0
        for i in range(len(id_list)):
            show_cust(i)
            flag=1
        else:
            if flag==0:
                print("Id_list is empty")
    # """for exit Infinite loop"""
    elif ch=="6":
        print("Thanks for using CMS ")
        break
    # """If user gives invalid choice"""
    else:
        print("You Entered Wrong Choice")
    # """wanna to continue infinite loop"""
    chYN=input("Do you want to continue(Y/N): ")
    if chYN=="n" or chYN=="N":
        print("Thanks for using our calculator")
        break
    # End of CMS Thankyou :)

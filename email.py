#Prompts user to input the name of the recruiter along with the email domain
def userInput():

    first_name = input("Enter the recruiter's first name: ")
    last_name = input("Enter the recruiter's last name: ")
    email_domain = input("Enter the email domain: ")
    return first_name, last_name, email_domain


#Creates email based on four different formats
def createEmail(first, last, domain, email_list):

    format1 = str(first) + str(last) + "@" + str(domain)
    print(format1)
    format2 = str(first) + "." + str(last) + "@" + str(domain)
    print(format2)
    format3 = str(first) + "_" + str(last) + "@" + str(domain)
    print(format3)
    format4 = str(first) + "-" + str(last) + "@" + str(domain)
    print(format4)

    email_list.extend([format1,format2,format3,format4])
    return email_list
    



#Creates a list of the emails that are fenerated from the email function
def main_function():
    info = userInput()
    email_list = []

    first = info[0]
    first_int = first[0]
    last = info[1]
    last_int = last[0]
    domain = info[2]
    
    email_list = createEmail(first,last,domain, email_list)
    email_list = createEmail(first_int,last,domain, email_list)
    email_list = createEmail(first,last_int,domain, email_list)
    print(email_list)

main_function()

#The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including your own.
#Use your knowledge of working with Python files to retrieve, manipulate, obscure, and create data in your quest for justice. Work with CSV files and other text files in this exploration of the strength of Python file programming.
import csv
compromised_users = []
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])

#print(compromised_users)

compromised_userss = 'jean49' 'haydenashley' 'michaelastephens' 'denisephillips' 'andrew24' 'kaylaabbott' 'tmartinez' 'mholden' 'randygilbert' 'watsonlouis' 'mdavis' 'patrickprice' 'kgriffith' 'hannasarah' 'xaviermartin' 'hrodriguez' 'erodriguez' 'danielleclark' 'timothy26' 'elizabeth19'

with open('compromised_users.txt','w') as compromised_user_file:
  for compromised_user in compromised_users:
   compromised_user_file.write(compromised_userss) 


import json
with open('boss_message.json','w') as boss_message:
  boss_message_dict = {'key':'The Boss','message':'Mission Success'}
  boss_message = json.dump(boss_message_dict,boss_message)
  

with open('new_passwords.csv','w') as new_passwords_obj:
  slash_null_sig = """"
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
  
  """

  new_passwords_obj.write(slash_null_sig)





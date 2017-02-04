import os
hostname = "google.com" #example
response = os.system("ping " + hostname)

if response==0:
    print ("Server is Alive")
else:
    print ("Server is Down")
print response

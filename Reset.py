''' removes encrypted files and populates victims folder with victim files for testing '''

import os

for anything in os.scandir('/home/cse/Lab3/Q6files/victims'):
  os.remove(anything.path)

with open('/home/cse/Lab3/Q6files/victims/flora.txt', 'w') as f:
  f.write('puppy cat')
  
with open('/home/cse/Lab3/Q6files/victims/stella.txt', 'w') as f:
  f.write('We bear Bears')
  
with open('/home/cse/Lab3/Q6files/victims/techna.txt', 'w') as f:
  f.write('aint that just the way')
  
with open('/home/cse/Lab3/Q6files/victims/coffee.txt', 'w') as f:
  f.write('karinas coffee addiction')
  
with open('/home/cse/Lab3/Q6files/victims/drama.txt', 'w') as f:
  f.write('xinyi and faiyhaa drama addiciton')

try:
  os.remove('/home/cse/Lab3/Q6files/EncryptedSharedKey.txt')
except:
  x = 1
  
print('success: directory reset')
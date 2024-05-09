
file = open ("devices.txt","a")
while True:
    newDevice = input ("Enter device name:")
    file.write(newDevice + "\n")
    if newDevice == 'exit':
         break

print("All done")

import socket

TEL_IP = "192.168.1.18" # PHONE IP
PORT = 54596            # PORT TO USE
PATH = "D:\\Users\\Seb\\Desktop\\my_video.h264" # PATH TO THE SAMPLE

#Open end read file
f = open(PATH, "rb")

b = f.read()

f.close()

#send data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TEL_IP, PORT))


print("Enter negative value to quit")
cursor = 0
while cursor < len(b):
    try:
        i = int(input("how many bit to send ("+str(cursor)+"/"+str(len(b))+") ? "))
        if i < 0:
            break
        cursor += s.send(b[cursor:cursor+i])
        #print("b[", cursor, ":", cursor+i, "] ", b[cursor:cursor+i])
        #cursor += i
    except:
        pass
s.close()
print("end")

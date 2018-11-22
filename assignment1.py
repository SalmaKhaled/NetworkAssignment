def CRC(frame,genterator):
	order = len(genterator)
	result=""
	index=order
	for i in range(order):
	    if i == 0:
	        continue
	    frame = frame + "0"
	    result = result +str(int(frame[i]) ^ int(genterator[i]))
	#print(result)
	for k in range(len(frame))[index:]:
	    result = result + frame[index]
	    resultprev = result
	    #print(index , "-" , result)
	    result = ''
	    for j in range(order):
	        if j == 0:
	            continue
	        if k == len(frame):
	            continue
	        if resultprev[0] == '0':
	            result = result + str(int(resultprev[j]) ^ 0)
	        else:
	            result = result + str(int(resultprev[j]) ^ int(genterator[j]))
	    if len(result) < order:
	        for j in range(order - len(result)-1):
	            result = "0" + result
	    index = index +1
	message = str(int(frame)^int(result))
	#print(frame)
	#print(result)
    #print(message)
    return message

#ALTER FUNCTION
def alter(message):
    index = input("Please enter the index:")
    x = int(index) - 1
    toinvert = message[x]
    # message = message.replace(toinvert,str(int(toinvert)^1))
    message = message[:x] + str(int(toinvert) ^ 1) + message[x + 1:]
    # print(message)
    return message

#MAIN
""" input """
f = open("input.txt", 'r')
f_out = open("out.txt", 'w')
lines = f.readlines()
frame = lines[0].replace('\n', '')
genterator = lines[1].replace('\n', '')

message = CRC(frame, genterator)
f_out.write(message)
f_out.close()
f_out = open("out.txt", 'r')
message2=f_out.read()
verifier(message2, genterator)

message3 = alter(message2)
f_out = open("out_alter.txt", 'w')
f_out.write(message3)
f_out.close()
f_out = open("out_alter.txt", 'r')
msg=f_out.read()
verifier(msg, genterator)

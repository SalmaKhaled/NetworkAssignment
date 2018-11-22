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
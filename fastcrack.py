tocrack = "d0763edaa9d9bd2a9516280e9044d885"

def fastfind(hashtocrack):
	with open('hashtabble.txt', 'r') as f:
		lines = f.readlines()
		for l in lines:
			parts = l.split(':')
			if len(parts) == 2:
				if parts[0] == hashtocrack:
					return parts[1]
	return "not found"

print(fastfind(tocrack))
start_time = raw_input()
duration = 1000
servers = []        #server is next available at start_time + duration (1000ms)

while start_time != "end":
   start_time = int(start_time)
   i = 0 
   while i < len(servers) and servers[i] > start_time:
      i = i + 1
   if i < len(servers):
      servers[i] = start_time + duration
   else:
      servers.append(start_time + duration)
   start_time = raw_input()
print len(servers)
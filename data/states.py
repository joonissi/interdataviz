import csv


input_file = 'userlocation_counts.csv'
states_file = '../docs/statescount.csv'

#with open(input_file) as f:
  #content = f.readlines()
  # skip header
  #content = f.readlines()[1:]
r = csv.reader(open(states_file, 'r'))
reader = csv.reader(open(input_file, 'r'))

d = {}
states = {}

for state in r:
  a, s, c = state
  states[s.upper()] = c

print states

for row in reader:
  k, v, z = row
  if v.isdigit():
    #d[k.upper()] = int(v)
    #print k, v

    for key, value in states.iteritems():
      #state, count = r
      if key.upper() == k.upper():
        #states[s] += int(v)
        print key.upper() + ' is ' + k.upper()
        temp = int(v) + int(value)
        states[key] = int(temp)
        #print 'jee'


        #states[s] += c

   #print a, s, c

#print states
for kk, vv in states.iteritems():
  print kk.title() + ',' + str(vv)

# reader = csv.reader(open(input_file, 'r'))
# d = {}
# for row in reader:
#    k, v, z = row
#    if v.isdigit():
#     d[k.upper()] = int(v)

# print d




#states = {}

#for line in content:
  #line_name = line.split(',')[0].replace('"','').upper()
  #line_count = line.split(',')[1]

  #(key, val) = line.split()
  #states[line_name] = int(line_count)

  #if line_name not in a:
  #  a[]
  #print line_name + ' ' + line_count

#print 'original lines: ' + str(len(content))
#print 'no dublicate lines: ' + str(len(a))

# for x in states:
#     print (x)
#     for y in states[x]:
#         print (y,':',states[x][y])
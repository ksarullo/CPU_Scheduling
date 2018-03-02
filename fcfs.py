#!/user/bin/env python
import random
import sys

process_queue = []
#for i in range(random.randint(2,5)):
for i in range(int(sys.argv[1])):
	process_queue.append(dict(Name="P" + str(i+1), Burst=random.randint(1, 100)))

random.shuffle(process_queue) #randomize arrival time

for index, process in enumerate(process_queue):
	if(index == 0):
		process['Waiting'] = 0
		process['Turnaround'] = process['Burst']
	else:
		process['Waiting'] = process_queue[index-1]['Waiting'] + process_queue[index-1]['Burst']
		process['Turnaround'] = process['Waiting'] + process['Burst']

print("+------------------------------------------+\t\t+--------------------------------+")
print("| Process Name | Arrival Time | Burst Time |\t\t| Waiting Time | Turnaround Time |")
print("+------------------------------------------+\t\t+--------------------------------+")

for index, process in enumerate(process_queue):
	print("\t{}             {}            {}\t\t\t\t{}\t\t{}".format(process['Name'], index, process['Burst'], process['Waiting'], process['Turnaround']))

total_waiting = 0
total_turnaround = 0
for process in process_queue:
	total_waiting += process['Waiting']
	total_turnaround += process['Turnaround']

print("Average Waiting Time: " + str(total_waiting/len(process_queue)))
print("Average Turnaround Time: " + str(total_turnaround/len(process_queue)))

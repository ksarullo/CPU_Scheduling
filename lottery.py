#!/user/bin/env python
import math
import random
import sys

MAX = 25
waiting_counter = 0

process_queue = []
waiting_times = {}
burst_times = {}
for i in range(int(sys.argv[1])):
	process_queue.append(dict(Name="P" + str(i+1), Burst=random.randint(1,MAX), Tickets=[]))
	waiting_times[process_queue[i]['Name']] = []
	burst_times[process_queue[i]['Name']] = process_queue[i]['Burst']

quantum = 8
print("Quantum: {}\n".format(quantum))

while True:
	# Check burst times of each process; if <= 0 it has finished executing so remove from queue
	for process in process_queue:
		if process['Burst'] <= 0:
			process_queue.remove(process)

	# if process_queue is empty all processes have finished executing
	if not process_queue:
		break
	elif len(process_queue) == 1:
		print("+---------------------------+")
		print("| Process Name | Burst Time |")
		print("+---------------------------+")
		print("\t{}           {}".format(process_queue[0]['Name'], process_queue[0]['Burst']))
		print("+---------------------------+")
		print("       One process left      ".format(winning_ticket))
		print("         {} Running          ".format(process_queue[0]['Name']))
		print("+---------------------------+\n\n")

		waiting_times[process_queue[0]['Name']].append(waiting_counter)
		break
	else:

		print("+-------------------------------------+")
		print("| Process Name | Burst Time | Tickets |")
		print("+-------------------------------------+")

		ticket = 0
		total_tickets = 0

		for process in process_queue:
			process['Tickets'] = []
			if(process['Burst'] > 0):
				num_tickets = math.ceil((1 / process['Burst']) * MAX) #Determines # tickets to give process (prioritizes processes with smaller burst times)
				total_tickets += num_tickets

				#Give tickets to process
				for i in range(num_tickets):
					ticket+=1
					process['Tickets'].append(ticket)
			print("\t{}           {}       {}".format(process['Name'], process['Burst'], process['Tickets']))

		#Select winner
		winning_ticket = random.randint(1, total_tickets)
		for process in process_queue:
			if winning_ticket in process['Tickets']:
				if process['Burst'] > quantum:
					if waiting_counter == 0:
						waiting_times[process['Name']].append(0)
					else:
						waiting_times[process['Name']].append(waiting_counter)
					waiting_counter += quantum
				else:
					if waiting_counter == 0:
						waiting_times[process['Name']].append(0)
					else:
						waiting_times[process['Name']].append(waiting_counter)
					waiting_counter += process['Burst']
				process['Burst'] -= quantum
				print("+-------------------------------------+")
				print("         Winning Ticket ::{}::         ".format(winning_ticket))
				print("              {} Running               ".format(process['Name']))
				print("+-------------------------------------+\n\n")

#Calculate average turnaround time
total_turnaround = 0
last_exec = 0
for key in waiting_times:
	if len(waiting_times[key]) == 1:
		total_turnaround += (waiting_times[key][0] + burst_times[key])
	else:
		last_exec = waiting_times[key][len(waiting_times[key]) - 1]
		total_turnaround += (last_exec + (burst_times[key] - ((len(waiting_times[key])-1) * quantum)))


#Calculate average waiting time
total_waiting = 0
times = []
for key in waiting_times:
	times = waiting_times[key]
	waiting = 0
	for index, time in enumerate(times):
		if index == 0:
			waiting = times[0]
		if index != 0:
			if times[index - 1] + quantum != time:
				waiting += (time - (times[index-1] + quantum))
	total_waiting += waiting

print("Average Waiting Time: " + str(total_waiting/len(waiting_times)))
print("Average Turnaround Time: " + str(total_turnaround/len(waiting_times)))

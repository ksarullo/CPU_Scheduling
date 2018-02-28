#include<iostream>
using namespace std;

void roundrobin(int num_procs, int burst_time[], int quantum) {
	int waiting[num_procs], turnaround[num_procs], total_wait = 0, total_turnaround = 0, burst_remain[num_procs];
	int t = 0;

	for (int i = 0 ; i < num_procs; i++) {
		burst_remain[i] = burst_time[i];
	}

	while(true) {
		bool done = true;
		for (int i = 0 ; i < num_procs; i++) {
			if (burst_remain[i] > 0) {
				done = false;
				if (burst_remain[i] > quantum) {
					t += quantum;
					burst_remain[i] -= quantum;
				} else {
					t += burst_remain[i];
					waiting[i] = t - burst_time[i];
					burst_remain[i] = 0;
				}
			}
		}
		if(done) break;
	}

	for (int i = 0; i < num_procs; i++) {
		turnaround[i] = burst_time[i] + waiting[i];
	}

	cout << "Process |" << "  Burst time   |" << "  Waiting time |" << "  Turn-around time\n";

	for (int i=0; i < num_procs; i++) {
		total_wait = total_wait + waiting[i];
		total_turnaround = total_turnaround + turnaround[i];
		cout << "   " << i+1 << "   " << "\t|\t" << burst_time[i] << "\t|\t"<< waiting[i] <<"\t|\t" << turnaround[i] << endl;
	}

	cout << "Average waiting time = " << (float)total_wait/ (float)num_procs << "\n";
	cout << "Average turn-around time = " << (float)total_turnaround / (float)num_procs << "\n";
}

int main() {
	
	printf("Enter number of processes: ");
	int num_procs;
	cin >> num_procs;
	int burst_time[num_procs];

	for(int i = 0; i < num_procs; i++) {
		printf("Enter Process #%d's burst time: ", i+1);
		cin >> burst_time[i];
	}

	int quantum;
	printf("Enter time quantum: ");
	cin >> quantum;

	roundrobin(num_procs, burst_time, quantum);

	return 0;
}


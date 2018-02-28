#include<iostream>
using namespace std;


int sort(int arr[], int size) {
    int smallestIndex = 0;
    for (int index = smallestIndex; index < size; index++) {
        if (arr[smallestIndex] > arr[index]) {
            smallestIndex = index;
        }
    }
    return smallestIndex;
}

void roundrobin(int num_procs, int burst_time[], int periods[]) {
	int waiting[num_procs], turnaround[num_procs], total_wait = 0, total_turnaround = 0;
	int burst_remain[num_procs], period_times[num_procs];	     
	int t = 0;

	for (int i = 0 ; i < num_procs; i++) {
		burst_remain[i] = burst_time[i];
	}

	for (int i = 0 ; i < num_procs; i++) {
		period_times[i] = periods[i];
	}

	while(true) {
		bool done = true;
		for (int i = 0 ; i < num_procs; i++) {
			if (burst_remain[i] > 0) {
				done = false;
				if (burst_remain[i] < period_time[i]) {
					t += burst_remain[i];
				} else {
					t += burst_remain[i];
					waiting[i] = t - burst_time[i];
					burst_remain[i] = 0;
				}
			}
		}
		if(done) break;
	}
}

int main() {
	
	printf("Enter number of processes: ");
	int num_procs;
	cin >> num_procs;
	int burst_time[num_procs];
	int periods[num_procs];

	for(int i = 0; i < num_procs; i++) {
		printf("Enter Process #%d's burst time: ", i+1);
		cin >> burst_time[i];
		printf("Enter Process #%d's period time: ", i+1);
		cin >> periods[i];
	}

	int sorted_burst_times[num_procs];
	int sorted_periods[num_procs];
	int smallest_idx;
	for(int i = 0; i < num_procs; i++) {
		smallest_idx = sort(periods, num_procs);
		sorted_periods[i] = periods[smallest_idx];
		sorted_burst_times[i] = burst_time[smallest_idx];
		periods[smallest_idx] = INT8_MAX;
	}

	roundrobin(num_procs, sorted_burst_times, sorted_periods);

	return 0;
}


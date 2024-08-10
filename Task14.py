nc= int(input("How many Customers: "))

scroll=[]
for i in range(nc):
    arrival_time= int(input(f"Enter Arrival time of Customer {i+1}: "))
    time_required= int(input("Enter Time required to prepare tea: "))
    sublist=[arrival_time,time_required]
    scroll.append(sublist)
    
print(scroll)

start_time= 0
current_time=0

waiting_time= []

for sublist in scroll:

    if current_time>=sublist[0] :
       start_time= current_time
    else:
       start_time=sublist[0]

    current_time= (start_time) + sublist[1]
    wait= current_time- sublist[0]
    waiting_time.append(wait) 

sum_wt= sum(waiting_time)
average_waiting_time= sum_wt/nc

print(f"The Average waiting time is : {average_waiting_time}")


import subprocess

cmd_iperf_server="sudo himage pc2@i3411 iperf -s -y >> dados.csv" #pc2
cmd_iperf_server2="sudo himage pc3@i3411 iperf -s -u" #pc3
cmd_iperf_server3="sudo himage pc4@i3411 iperf -s -u" #pc4

print("0")
subprocess.run(cmd_iperf_server, shell=True,capture_output=True) #pc2
print("1")
subprocess.run(cmd_iperf_server2, shell=True,capture_output=True) #pc3
print("2")
subprocess.run(cmd_iperf_server3, shell=True,capture_output=True) #pc4
print("3")
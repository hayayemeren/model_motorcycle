# communication.py

import network
import socket
import time
import _thread

class WifiServer:
    def __init__(self, ssid, password):
        self.latest_command = "STOP" # Start in a safe state
        self.ip_address = None
        self._connect_to_wifi(ssid, password)

    def _connect_to_wifi(self, ssid, password):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid, password)

        print("Connecting to Wi-Fi...")
        max_wait = 15
        while max_wait > 0:
            if wlan.status() >= 3:
                break
            max_wait -= 1
            print(".")
            time.sleep(1)

        if wlan.status() != 3:
            raise RuntimeError('Network connection failed')
        else:
            status = wlan.ifconfig()
            self.ip_address = status[0]
            print(f'Connected! Pico IP address: {self.ip_address}')

    def _server_thread(self):
        # This is the core server logic that runs in the background
        addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        s = socket.socket()
        s.bind(addr)
        s.listen(1)
        print("Server is listening on port 80...")

        while True:
            try:
                conn, addr = s.accept()
                # A single client is expected to connect and send commands
                print(f'Client connected from: {addr}')
                
                # Loop to handle commands from this one client
                while True:
                    data = conn.recv(1024)
                    if not data: # If connection is closed by client
                        break
                    command = data.decode('utf-8')
                    self.latest_command = command
                    # Optional: Print received command for debugging
                    # print(f"Received command: {self.latest_command}")

                conn.close()
                print("Client disconnected.")

            except OSError as e:
                print(f"Server Error: {e}")
                if 'conn' in locals():
                    conn.close()

    def start_server(self):
        # Start the server in a separate thread so it doesn't block the main loop
        _thread.start_new_thread(self._server_thread, ())
        print("Server thread started.")

    def get_latest_command(self):
        # This is how the main.py loop will get the command
        return self.latest_command
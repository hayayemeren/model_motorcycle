# pc_client.py

import socket
import pygame

# --- Configuration ---
PICO_IP = "192.168.68.54"  # IMPORTANT: Change to your Pico W's IP address
PICO_PORT = 80
WIDTH, HEIGHT = 300, 200 # Size of the control window

# --- Network Setup ---
client_socket = None

def send_command(command):
    global client_socket
    try:
        if client_socket is None:
            print(f"Connecting to {PICO_IP}...")
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((PICO_IP, PICO_PORT))
            print("Connected!")
        client_socket.sendall(command.encode())
    except (socket.error, BrokenPipeError) as e:
        print(f"Connection error: {e}. Will try to reconnect.")
        client_socket = None

# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Motorcycle Controller")
font = pygame.font.Font(None, 36)
print("Pygame client running. Use arrow keys in the Pygame window to control.")

# --- Main Loop ---
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # --- Key Press Events ---
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                send_command("UP")
            elif event.key == pygame.K_DOWN:
                send_command("DOWN")
            elif event.key == pygame.K_LEFT:
                send_command("LEFT")
            elif event.key == pygame.K_RIGHT:
                send_command("RIGHT")

        # --- Key Release Events ---
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                send_command("STOP")
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                send_command("CENTER")

    # Drawing the UI (optional but helpful)
    screen.fill((40, 40, 40)) # Dark grey background
    text = font.render("Use Arrow Keys", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()
if client_socket:
    client_socket.close()
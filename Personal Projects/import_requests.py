import requests
import pygame
import keyboard
import os
def download_from_google_drive(file_id, save_path):
    URL = "https://drive.google.com/uc?export=download"
    session = requests.Session()

    response = session.get(URL, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, save_path)
    print(f'File successfully downloaded and saved as {save_path}')
def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None
def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
def play(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
def handle_KEY_DOWN(event):
    if event.event_type == keyboard.KEY_DOWN:
        play(sound_file) # Download the .wav file from Google Drive
file_id = '1SHIJaScpI9SPM5qYTrhaLn6s0mwgn2L8' # Save the file to the same directory as the script
script_directory = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_directory, 'duck_sound.wav')
download_from_google_drive(file_id, save_path) # Set the sound file path to the downloaded file
sound_file = os.path.join(script_directory, 'duck_sound.wav') # Start listening to key presses
keyboard.hook(handle_KEY_DOWN)
keyboard.wait('esc')
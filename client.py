#Standard Libraries
import socket
import pyaudio

def Main():
    try:
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 35000
        CHUNK = 1024*30
        RECORD_SECONDS = 1
        audio = pyaudio.PyAudio()
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
        #IP adress of host and port number
        host = '192.168.10.8' #Host IP similiar to server IP
        port = 8081           #Port Number similiar to server IP
        s = socket.socket()   #Connection
        s.connect((host, port))
        print ("recording...")
        while True:
           #Sending Data frames per seconds
           for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
               data = stream.read(CHUNK)
               s.send(data)
        #Closing the stream   
        stream.stop_stream()
        stream.close()
        audio.terminate() 
        s.close()
    except:
        print("Plugin Handsfree")

if __name__ == '__main__':
    Main()

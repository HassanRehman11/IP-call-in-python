import socket
import pyaudio

def Main():
    #Host IP
    host = '192.168.10.8'
    #Port Number
    port = 8081
    FORMAT = pyaudio.paInt16
    CHANNELS=2
    RATE=35000
    CHUNK=1024*50
    RECORD_SECONDS=1
    audio = pyaudio.PyAudio()
    stream = audio.open(format =FORMAT,channels=CHANNELS,
                        rate = RATE, output=True)
    #TCP connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    #Can Accept 5 users
    s.listen(5)
    c, addr = s.accept()
    print ("Connection from: "+ str(addr))
    try:
        while True:
            #Recieve Data
            data = c.recv(1024*30)
            stream.write(data)
        stream.stop_stream()
        stream.close()
        audio.teminate
        c.close()
    except:
        pass

if __name__ == '__main__':
    Main()


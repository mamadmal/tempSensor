import serial
import serial.tools.list_ports
import mariadb
import sys
#digital temputure sensor: DS18B20

#get  the port list and put in a list
ports = serial.tools.list_ports.comports()
portsList = [] 

#change the port list to a string
for onePort in ports: 
    portsList.append(str(onePort))
    print(str(onePort))

#check if there's a port, try to connect a database.
if bool(portsList):
    try: 
        conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="temp")
        print("coonected to database.")
        cur = conn.cursor()
    except mariadb.Error as e:
        print("ohhh, NO!")
        print(e)
        sys.exit(1)
else:

    print("Thereisn't any port found.")
    sys.exit(1)

# choose the serial port.
ser = serial.Serial(input("Enter the COM: ")) 
print(ser.name)

#read the lines and send data to database.
s = ser.readline()
while True:
     packet = ser.readline()
     packetFlo = packet.decode().rstrip("b'\n'")
     packetFlo = float(packetFlo)
     packetCel = (packetFlo - 32.00) * 5.00 / 9.00
     print("%.2f"%packetCel)

     tempDatabase = [(packetCel)]
     cur.execute("INSERT INTO sdata (flData) VALUES (%s)",tempDatabase)
     conn.commit()
     print(f"Data added to DB, Last Inserted ID: {cur.lastrowid}") 

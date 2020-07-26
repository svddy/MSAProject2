import random
import time

# Implementing Azure connectivity.
from azure.iot.device import IoTHubDeviceClient, Message

# Azure Device Authentication.
CONNECTION_STRING = "HostName=SpeedCameraHub.azure-devices.net;DeviceId=SpeedCameraDevice;SharedAccessKey=FT90biAeszHN/m5nGB3KcCW1S/M3SqdIWEor9uKmybg="

# Output Message Formatting.
SPEED = 100
MSG_TXT = '{{"speed": {speed}}}'

# Establish client connection with IoT Hub.
def iothub_client_connect():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

# Define data transferral to IoT Hub.
def iothub_client_transfer():

    try:
        client = iothub_client_connect()
        print ( "Connection established with IoT Hub. Vehicle speeds are now being monitored." )

        while True:

            # Speed simulation in effect.
            speed = SPEED + (random.uniform(-20,20))
            msg_txt_formatted = MSG_TXT.format(speed=speed)
            message = Message(msg_txt_formatted)

            # Identify detected speeding.
            if speed > 108:
              message.custom_properties["speedAlert"] = "true"
            else:
              message.custom_properties["speedAlert"] = "false"

            print( "Speed Detected: {}".format(message) )
            client.send_message(message)
            if speed > 108:
              print ( "ALERT: Speeding!" )
            # Random interval to simulate realistic gap between camera readings.
            time.sleep(random.uniform(0.2, 12.0))

    except KeyboardInterrupt:
        print ( "Communication halted with IoT Hub. (User Input)" )

if __name__ == '__main__':
    print ( "Speed Camera #1 Simulation" )
    iothub_client_transfer()
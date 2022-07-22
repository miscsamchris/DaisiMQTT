import paho.mqtt.client as mqtt 
import time

class MQTTBROKER():
    def __init__(self,broker_url="broker.hivemq.com",port_no=1883):        
        self.broker_url = broker_url
        self.port_no=port_no
        self.clients=dict()

    def publish(self,client_id,topic, data):
        '''
        
        Parameters
        ----------
        client_id : str
            Client ID of the client created.
            eg. TestClient, Server etc.
        topic : str
            The Topic of the Message to be published.
        data : str
            The Message Payload to be published.

        Returns
        -------
        None.

        '''
        if client_id in self.clients.keys():
            client=self.clients[client_id]
        else:
            client = mqtt.Client(client_id)
            client.connect(self.broker_url,self.port_no) 
            self.clients[client_id]=client
        client.publish(topic,data)
       
    def subscribe(self,client_id,topic,callback):
        '''
        
        Parameters
        ----------
        client_id : str
            Client ID of the client created.
            eg. TestClient, Server etc.
        topic : str
            The Topic of the Message to be published.
        callback : function
            The Callback function that deals with the received data for the client.
            Parameters for the callback:
                client 
                userdata
                message
                eg. def callback(client,userdata, message):
                        print("received message: " ,str(message.payload.decode("utf-8")))
        Returns
        -------
        None.

        '''
        if client_id in self.clients.keys():
            client=self.clients[client_id]
        else:
            client = mqtt.Client(client_id)
            client.connect(self.broker_url,self.port_no) 
            self.clients[client_id]=client
        client.loop_start()
        client.subscribe(topic)
        client.on_message=callback


def initialize(broker_url="broker.hivemq.com",port_no=1883):
    '''

    Parameters
    ----------
    broker_url : str, optional
        Hostname of the MQTT Broker. The default is "broker.hivemq.com".
    port_no : int, optional
        Port of the MQTT Broker. The default is 1883.

    Returns
    -------
    a new MQTTBROKER object

    '''
    
    mqt=MQTTBROKER(broker_url,port_no)
    return mqt
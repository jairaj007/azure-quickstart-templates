from azure.servicebus import ServiceBusService, Message, Queue
from azure.servicebus import Message
from bottle import run, route


bus_service = ServiceBusService(
    service_namespace='jairaj007',
    shared_access_key_name='RootManageSharedAccessKey',
    shared_access_key_value='lGSHGfaf8RBQ9lHbso85PCvGD2BCBVzpMKHHXLwluhg=')
	

	
@route('/')
def root():
	msg = bus_service.receive_queue_message('myqueue', peek_lock=True)
	return(msg.body)
	msg.delete()
	

run()

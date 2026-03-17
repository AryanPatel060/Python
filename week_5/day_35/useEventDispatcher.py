from eventDispatcher import EventDispatcher, DBLog, MailSender, Plugin

class FileLog(Plugin):

    @property
    def plugin_name(self):
        return "File_logger"
    
    def service(self, payload):
        print(f"log has updated for orderId {payload['orderId']} and for username {payload['username']}")        

dispatcher = EventDispatcher()

dispatcher.register(DBLog())
dispatcher.register(MailSender())
dispatcher.register(FileLog())

order = {
    'orderId' : "ord123",
    'username' : 'Aryan Patel'
}

dispatcher.dispatch(order)
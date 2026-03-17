from abc import ABC , abstractmethod

class Plugin(ABC):

    @property
    @abstractmethod
    def plugin_name(self):
        pass

    @abstractmethod
    def service(self):
        pass

class DBLog(Plugin):
    @property
    def plugin_name(self):
        return "Database_logger"
    
    def service(self,payload):
        print(f"order saved in DB with order id {payload['orderId']}")
        return 
    
class MailSender(Plugin):
    @property
    def plugin_name(self):
        return "Mail_sender"
    
    def service(self,payload):
        print(f"Mail send to user {payload['username']}")
        return 

class EventDispatcher:
    
    def __init__(self):
        self._plugin = {}

    def register(self,plugin):
        self._plugin[plugin.plugin_name] = plugin
        print(f"{plugin.plugin_name} registered")

    def dispatch(self, payload):
        for plugin_name , plugin in self._plugin.items():
            plugin.service(payload)



    
import uuid
from nameko.rpc import rpc
from nameko.events import event_handler
from nameko_redis import Redis


class WorkerSubscriber:
    name = 'trips_service'
    redis = Redis('development')

    @event_handler("airports_service", "aeroporto_cadastrado")
    def handle_event(self, payload):
        print(f"Novo aerporto recebido: {payload}")

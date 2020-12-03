from nameko.rpc import rpc
from nameko.events import event_handler
from nameko_redis import Redis


class WorkerSubscriber:
    name = 'trips_service'
    redis = Redis('development')

    @event_handler("airports_service", "aeroporto_cadastrado")
    def handle_event(self, payload):
        # deixei esse id fixo para ficar fácil de consultar a api e ver se atualizou a trip com o aeroporto recem
        # cadastrado no microserviço airport
        trip_id = "12345"
        self.redis.set(trip_id, payload)

    @rpc
    def get(self, trip_id):
        trip = self.redis.get(trip_id)
        return trip
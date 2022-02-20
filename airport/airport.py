import uuid

from nameko.rpc import rpc
from nameko.events import EventDispatcher
from nameko_redis import Redis


class AirportsService:
    name = "airports_service"
    redis = Redis('development')
    dispatch = EventDispatcher()

    @rpc
    def get_by_id(self, airport_id):
        airport = self.redis.get(airport_id)
        return airport

    @rpc
    def create(self, airport):
        airport_id = uuid.uuid4().hex
        self.redis.set(airport_id, airport)
        self.dispatch("aeroporto_cadastrado", airport_id)
        print(f"Novo aeroporto criado: {airport_id}")
        return airport_id

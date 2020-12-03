Ao cadastrar um novo aeroporto no microserviço airport, seu id é publicado em uma fila que é lida pelo microserviço trip, que irá cadastrar uma nova viagem com base nesse aeroporto.

Este projeto utiliza python 3.8 e docker.

Rodar o projeto:
* docker-compose up

Cadastrar aeroporto:
* $ curl -i -d "{\"airport\": \"airport1\"}" localhost:8000/airport

Verificar se cadastrou nova viagem após cadastro do novo aeroporto:
* $ curl localhost:8000/trip/12345

Ver as filas:
* http://localhost:15672/

Exemplo baseado nos tutoriais:
* https://www.toptal.com/python/introduction-python-microservices-nameko
* https://joelholmes.dev/posts/nameko-quick-microservices/

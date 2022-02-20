Ao cadastrar um novo aeroporto no serviço **airport**, seu id é publicado em uma fila que é lida pelo serviço **trip**.
Atualmente, o serviço trip apenas imprime os dados do novo aerporto. Futuramente deve ser implementada uma funcionalidade
para cadastrar uma nova viagem a partir do novo aeroporto cadastrado.

Rodar o projeto:
* docker-compose build
* docker-compose up

Cadastrar aeroporto:
```
curl -i -d "{\"airport\": \"first_airport\"}" localhost:8000/airport
```

Recuperar um aeropornto:
```
curl localhost:8000/airport/{id}
```

Ver as filas:
* http://localhost:15672/

Exemplo baseado nos tutoriais:
* https://www.toptal.com/python/introduction-python-microservices-nameko
* https://joelholmes.dev/posts/nameko-quick-microservices/

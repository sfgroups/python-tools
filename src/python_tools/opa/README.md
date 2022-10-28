This sample got from this site: https://github.com/open-policy-agent/example-api-authz-python

## Trying the example (local)

Start OPA with the example policy:

```bash
opa run -s example.rego
```
# with docker image

```bash
docker run -it --rm -p 8181:8181 -v $PWD:/app openpolicyagent/opa:latest-rootless run -s /app/example.rego
```

Run the server:

```bash
python server.py
```

As a manager, create a car (this should be allowed):

```bash
curl -H 'Authorization: alice' -H 'Content-Type: application/json' \
    -X PUT localhost:8080/cars/test-car \
    -d '{"model": "Toyota", "vehicle_id": "357192", "owner_id": "4821", "id": "test-car"}'
```

As a car admin, try to delete a car (this should be denied):


```bash
curl -H 'Authorization: kelly' \
    -X DELETE localhost:8080/cars/test-car
```

# this will allow us to delete the car
```bash
curl -H 'Authorization: james'     -X DELETE localhost:8080/cars/test-car
```
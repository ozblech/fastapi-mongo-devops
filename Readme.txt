In order to run mongodb chart:
helm install my-mongodb bitnami/mongodb --set auth.enabled=false
Run app:
helm install fastapi-mongo helm-fastapi-mongo/
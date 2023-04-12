
docker build -t webapp2 .
kubectl apply -f deployment.yaml
kubectl expose deployment deploy-python --type=LoadBalancer --name=my-service
# just in case deployment does not work (kubectl apply -f pod-python.yaml)
kubectl exec -it pod-python -- bash #enter into the pod

# CheckOut:

kubectl get statefulset redis
kubectl get service redis-headless
kubectl get pod
kubectl get service my-service
kubectl get deployment
kubectl get pv
kubectl get pvc
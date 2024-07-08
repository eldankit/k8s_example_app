# k8s_example_app
## backend deployment
  - created a docker image of the app using the dockerfile
  - uploaded the image to dockerhub
  - use the image in kubernetes deployment and service yaml files
  - to check if running and working used kubectl port-forward service/flask-app-service 5000:80 to check the app on localhost:5000

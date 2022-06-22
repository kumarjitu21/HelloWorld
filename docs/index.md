# Welcome to flask based hello-world app

## Docker Build and publish
```
$ docker build -t flask-demo .

$ docker tag flask-demo kumarjitu21/flask-helloworld

$ docker push kumarjitu21/flask-helloworld

```

## Docker run

```$ docker run -p 8080:8080 -d -t flask-demo```
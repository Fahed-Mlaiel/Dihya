# Dihya Logos – Exemples Kubernetes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dihya-logos
spec:
  replicas: 1
  selector:
    matchLabels:
      app: dihya-logos
  template:
    metadata:
      labels:
        app: dihya-logos
    spec:
      containers:
      - name: dihya-logos
        image: dihya-logos:latest
        ports:
        - containerPort: 4001
        volumeMounts:
        - name: logos-volume
          mountPath: /app
      volumes:
      - name: logos-volume
        hostPath:
          path: /workspaces/Dihya/Dihya/assets/logos
          type: Directory
```

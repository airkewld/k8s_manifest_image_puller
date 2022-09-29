# k8s_manifest_image_puller
Script to pull and save images from a k8s manifest to a file.

## Usage
```
image-puller.py -i manifest.(yaml|json) -o file_name
```
> `-i`: Provide path to manifest.

> `-o`(optional): filename of file with images.

- If `-o` is not provided, the default name of the output file is `images-to-scan`.

## Sample
```
helm install monitoring prometheus-community/kube-prometheus-stack --namespace monitoring --dry-run > prom.yaml
python3 image-puller.py -i prom.yaml -o scanMe
cat scanMe

 "bats/bats:v1.4.1"
 k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.1.1
 k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.1.1
 quay.io/prometheus/node-exporter:v1.3.1
 "quay.io/kiwigrid/k8s-sidecar:1.15.6"
 "quay.io/kiwigrid/k8s-sidecar:1.15.6"
 "grafana/grafana:8.4.6"
 "k8s.gcr.io/kube-state-metrics/kube-state-metrics:v2.4.1"
 "quay.io/prometheus-operator/prometheus-operator:v0.56.0"
 "quay.io/prometheus/alertmanager:v0.24.0"
 "quay.io/prometheus/prometheus:v2.35.0"
```

> This list can then be used to scan images.

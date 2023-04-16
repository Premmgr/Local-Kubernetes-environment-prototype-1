#!/usr/bin/env python3
import os
import yaml
import shutil

"""Generates simple kubernetes cluster manifest files, further modification required"""
class KubernetesTemplate:
    def __init__(self, name, image, container_port,container_targetport, container_protocol, replica):
        self.name = name
        self.image = image
        self.container_port = container_port
        self.container_targetport = container_targetport
        self.container_protocol = container_protocol
        self.replica = replica

    """Deployment Kind"""
    def deployment(self):
        try:
            os.mkdir(f'{self.name}')
        except:
             pass
        os.chdir(f'{self.name}')
        deployment_yaml = {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {
                "name": f"{self.name}"
            },
            "spec": {
                "selector": {
                    "matchLabels": {
                        "app": f"{self.name}"
                    }
                },
                "replicas": self.replica,
                "template": {
                    "metadata": {
                        "labels": {
                            "app": f"{self.name}"
                        }
                    },
                    "spec": {
                        "containers": [
                            {
                                "name": f"{self.name}",
                                "image": f"{self.image}",
                                "ports": [
                                    {
                                        "name": "http",
                                        "containerPort": self.container_port
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        }

        # Convert the Python dictionary to YAML
        deployment_template = yaml.dump(deployment_yaml)
        with open('Deployment.yaml', 'w') as deployement:
            deployement.write(deployment_template)
    """Service Kind"""
    def service(self):
            service_yaml = {
                "apiVersion": "v1",
                "kind": "Service",
                "metadata": {
                    "name": f"{self.name}"
                },
                "spec": {
                    "selector": {
                        "app": f"{self.name}"
                    },
                    "ports": [
                        {
                            "name": "http",
                            "port": self.container_port,
                            "targetPort": 80
                        }
                    ],
                    "type": "ClusterIP"
                }
            }       
            service_template = yaml.dump(service_yaml)
            with open('Service.yaml', 'w') as service:
                service.write(service_template)
    

sample_app = KubernetesTemplate(name='sample_app', image='example_image:latest', container_port=3000, container_targetport=80, container_protocol='http', replica=2)
sample_app.deployment()
sample_app.service()



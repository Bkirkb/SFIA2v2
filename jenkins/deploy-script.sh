#!/bin/bash
scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@swarm-mgr:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@swarm-mgr << EOF
    export DATABASE_URI=${DATABASE_URI} app_version=${app_version} replicas=${replicas}
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml fortune-swarm
EOF
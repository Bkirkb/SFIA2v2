pipeline{
    agent any
    environment{
        DATABASE_URI = credentials("DATABASE_URI")
    }
    stages{
        stage("Test Application"){
            steps{
                sh "pip3 install -r service1/requirements.txt"
                sh "python3 -m pytest --cov --cov-report term-missing"
            }
        }
        stage("Build & Push"){
            steps{
                // install docker and docker-compose
                // add jenkins to docker group
                // sudo su - jenkins, docker login
                // docker-compose build and push
                sh "docker-compose build && docker-compose push"
            }
        }
        stage("Config Management (ansible)"){
            steps{
                // write out playbook, inventory
                // with roles
                // ssh keys generated from jenkins machine for jenkins user (ssh-keygen)
                // sudo su - jenkins, install ansible on this machine for jenkins
                // jenkins runs playbook
                sh "cd ansible && /home/jenkins/.local/bin/ansible-playbook -i inventory playbook.yaml"
            }
        }
        stage("Deploy"){
            steps{
                // copy docker-compose.yaml over ssh (scp command)
                // set env variables on swarm manager
                // ssh into swarm manager to deploy the stack
            }
        }
    }
}

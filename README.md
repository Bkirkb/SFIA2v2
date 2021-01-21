# SFIA2
Practical project for QA academy
## Table of Contents
* [Brief](#brief)
  * [Requirements](#requirements)
    * [Scope](#scope)
    * [Platform Specific](#platform-specific-requirements)
* [Ideas](#ideas)
  * [Initial Idea](initial-idea)
  * [Final Idea](#final-idea)
* [Documentation](#documentation)
  * [Architecture](#architecture)
    *  [Database Structure](#database-structure)
    * [CI Pipeline](#ci-pipeline) 
  * [Project Tracking](#project-tracking)
  * [Risk Assessments](#risk-assessment)
  * [Testing](#testing)
  * [Front-End Design](#front-end-design)
  * [Known Issues](#known-issues)
  * [Future Improvements](#future-improvements)
<br><br>

### Brief
 The DevOps Practical project is designed to fully test and showcase my knowledge from the first half of the DevOps course as well as to showcase my ability to operate as a junior/dev-ops engineer. This project focuses more on the CI pipeline than the complexity of the code.
 <br> <br>
 
 #### Requirements
The Minumum Viable Product for this project is a fully complete CI/CD pipeline, integrated into a complete version control system utilising the feature/branch model. The application must be built in a service oriented way, with atleast 4 services being implemented. These are:
 * Service 1: Render templates needed to interact with the application, responsible for communicating with the other 3 services as well as persisting data in an SQL database
 * Service 2+3: Generate a "random" object (Needs 2 implementations)
 * Service 4: Generate an object that is built based on the objects generated previously (Needs 2 implementations)
<br><br>

#### Scope
 * An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
 * An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
 * If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
 * The project must follow the Service-oriented architecture that has been asked for.
 * The project must be deployed using containerisation and an orchestration tool.
 * As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
 * The project must make use of a reverse proxy to make your application accessible to the user.
 <br> <br>

#### Platform Specific
 * Kanban Board: Asana or an equivalent Kanban Board
 * Version Control: Git
 * CI Server: Jenkins
 * Configuration Management: Ansible
 * Cloud server: GCP virtual machines
 * Containerisation: Docker
 * Orchestration Tool: Docker Swarm
 * Reverse Proxy: NGINX
<br> <br>

### Ideas
The brief provided for this project provided several example ideas which could be used. 

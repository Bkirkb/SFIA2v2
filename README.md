# SFIA2
Practical project for QA academy
## Table of Contents
* [Brief](#brief)
  * [Requirements](#requirements)
    * [Scope](#scope)
    * [Platform Specific](#platform-specific-requirements)
* [Ideas](#ideas)
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
 * Fortune telling app - Generate a random fortune from a set of pre-defined random outcomes.
 * RPG style character generating app - Generate a random class and random attributes from a set of pre-defined random outcomes
 * football betting odds calculator app - Generate a random outcome from a game between 2 clubs from a list of clubs, outcome is decided by random outcomes and pre-defined values.
#### Chosen Idea: Fortune telling app
On refreshing the page the user is shown a series of objects that have been generated using various services, with the following structure:
 * Service 1: Jinja two template which takes in the values generated by the other 3 services and displays it to the user, hosted using an NGINX reverse proxy
 * Service 2 Implementation one: Generates a random day within the year (2021) that will be "lucky" for the user. Using conditional statements to ensure the date is logical.
 * Service 2 Implementation two: Generates a random month within the next 12 years that will be "lucky" for the user.
 * Service 3 Implementation one: Generates a luck value from 1-100, with the higher being the more "desirable" outcome
 * Service 3 Implentation two: Generates an outcome based on a simulated double dice roll. If the user rolls two of the same number they are classed as lucky and "true" is returned, if not "false" is returned.
 * Service 4 Implementation one: Checks what the day and luck values are, if the day is in an array of lucky values the luck number is added to, if the day is classed as unlucky the luck value is taken from. This service then generates a fortune message, with the luck number directly influencing how good or bad the fortune is.
 * Service 4 Implemntation two: Checks what the year value is and also if the user was lucky or not. depending on if the year is in the list of lucky or unlucky years their fortune will change, with various combinations existing.

### Planning
As this is a DevOps style oriented project the various project planning tools and methodologies were adhered to. This meant that the MVP was delivered within a single sprint and that the projects various tasks were displayed and taken from a kanban style board, using trello. The benefit of using a kanban style board is the ability to pick and choose which tasks need to be finished, and to order tasks into specific sections depending on the current state of the task. The full trello board for the project can be seen [here](https://trello.com/b/ArpN6Gwl "Project tracking board")

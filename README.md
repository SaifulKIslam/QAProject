# Book Review Application
# Author
## Saiful Islam

## Introduction
<a name="intro"></a>
This repositary contains my CRUD application for my QA devops fundamental project.

## Contents

- [Introduction](#intro)
- [Project Brief](#brief)
- [Application Design](#appdes)
    - [Entity Relationship Diagrams](#erd)
- [CI Pipeline](#ci)
- [Project Planning & User Stories](#use_case)
- [Testing](#test_)
- [Deployment](#depl)
- [Technologies used](#tech)
- [Risk Assessment](#risks)
    - [Explanation](#risk-exp)
- [Front end Design](#FE)
    - [Page: Home](#home)
    - [Page: Add Series name](#addSN)
    - [Page: Review Series](#revS)
    - [Page: View Review](#virev)
- [Future Improvements](#improve)

<a name="brief"></a>
## Breif
My project is to build an application where users can review books that they have read. 
Users will be able to:
*Create and add new books
*Delete exiting books
*Add reviews for books
*Update existing book titles
*Update existing reviews

<a name="appdes"></a>
### Application Design
The reviws and books data will be stored on an SQL server hosted on Google Cloud Platform (GCP).
Users will be able to Create, Read, Update and Delete from the database via the application interface accordingly.

<a name="erd"></a>
    #### Entity Relationship Diagram
    There will be two databases with a one-to-many realtionship.
    * A Books database
    * A Reviews database
    The ERD below shows the relationship between the databases

<a name="erd"></a>
    ### Entity Relationship Diagrams (ERD)
    <img src="/Documentation/ERD-db.png" alt="ERD" width="100%" height="100%"/>
    #### Plan

The inital plan for the ERD was consistent throughout the projects lifecycle and the project was delievered with the ERD shown below. No 
changes were needed to be made to the database as all functionalty requirements were met. 

<a name="ci"></a>
## CI Pipeline

A CI pipeline was involved in the development and deployment of the project, a mock-up of this can be seen below.

<img src="/Documentation/CI Pipeline.png" alt="CI" width="100%" height="100%"/>

<a name="use_case"></a>
### Project Planning & User Stories 

For the project a tool called Trello is being used as a planning tool to keep track of tasks and update what needed to be done or has been completed.
Trello is a free and easy to use platform that creates Kanban boards. Below is a screenshot of the Trello board and a link to the Trello board:

[Trello Board](https://trello.com/b/siBc2gmV/fundamental-qa-project)

<img src="/Documentation/Trello Board.png" alt="Trello" width="100%" height="100%"/>

### Use Case Overview

<img src="/Documentation/Use case Overview.png" alt="Usecase" width="100%" height="100%"/>

### Use Stories Overview
Below are entailed a series of user stories according to the planned uses for the application and their level of requirement according to a MoSCoW (Must, Shoud, Could, Would) scale

|  | User Stories and their MoSCoW |
| ------ | ------ |
| MUST | As a user, I want to be able to access the app online |
| MUST | As a user, I want to be able to create reviews on the app |
| SHOULD | As a user, I want to be able to read reviews on the app |
| SHOULD | As a user I want to be able to update my reviews on the app |
| SHOULD | As a user I want to delete my reviews on the app |
| COULD | As a user, I want to access the web on a mobile devices|
| Won't Have | As a user, I want to be able to rate other reviews on the app|


<a name="test_"></a>
## Testing (Unit Testing)
Testing of my web app has been done by using Pytest. When running pytest --cov term-missing on the applications directory the test coverage report of was 79%. The tests conducted on my app were to ensure that the user can access or view any of the apps pages. I also tested the functions for adding a series name, adding a review, updating and deleting series. With Pytest I was able to test most functions of my web app and understand what parts of my app that were not tested. 
<img src="/Documentation/Pytest-Cov.png" alt="ERD" width="100%" height="100%"/>
 

<a name="depl"></a>
## Deployment
The deployment and test stage for the web app were automated using Jenkins, a Continous integration server. Jenkins was installed into the GCP instance by firstly adding a port tcp:8080 to the firewall rules control, creating a deployment server. I then installed Jenkins on the GCP instance terminal as a user, with enhanced User admissions to run sudo commands enabling me to deploy and test my app on the deployment server. Jenkins 
<img src="/Documentation/Jenkins.png" alt="CI" width="100%" height="100%"/>

I also deployed my web application in a production server using Gunicorn by running the below command. 
<img src="/Documentation/Gunicorn.png" alt="CI" width="100%" height="100%"/>

<a name=risks></a>
## Risk Assessment

I have thought of a number of risks that my project may face and have categorised them below to analyse the risk, its impact, likelihood and the appropriate response to that risk. The risks can be seen as a combination of technical risks associate with the development side of the project and general risks that will directly or indirectly impact the project

[Excel version](https://docs.google.com/spreadsheets/d/1PkbGO7We7VWNwiyrE6rUQE0_KDZOs-1CUOdsQAjmLcc/edit#gid=0)
<img src="/Documentation/Risk Table.png" alt="CI" width="100%" height="100%"/>


<a name="tech"></a>
### Technologies Used
* Database: GCP SQL Server
* Programming language: Python
* Framework: Flask
* Deployment: Gunicorn
* CI Server: Jenkins
* Test Reporting: Pytest
* VCS: [Git](https://github.com/aaboungab)
* Project Tracking: [Trello](https://trello.com/b/siBc2gmV/fundamental-qa-project)
* Live Environment: GCP


<a name="FE"></a>
## Front End Design

<a name="home"></a>
### Home Page
Clear home page consists of an Add series button and home button to redirect back to the homepage. 
<img src="/Documentation/Home.png" alt="" width="100%" height="100%"/>


<a name="addSN"></a>
### Add Series Name Page
Clicking on the Add a Series button you will be redirect to the Add series page. 
<img src="/Documentation/AddSeries.png" alt="" width="100%" height="100%"/>

#### Home page after Adding series name
<img src="/Documentation/AddSeriesHome.png" alt="" width="100%" height="100%"/>


<a name="revS"></a>
### Review Series Page
#### Add review
Add a review by clicking on the Add review button on the home page. That will then redirect you to the add review page:

<img src="/Documentation/AddReview.png" alt="" width="100%" height="100%"/>

After adding your review you will be automatically redirected to the Review page where you can view your review and other reviews on the specific series:

<img src="/Documentation/ReviewPage.png" alt="" width="100%" height="100%"/>


<a name="virev"></a>
### View Review Page
You can veiw reviews of each series by clicing  the view review button on the homepage:

<img src="/Documentation/viewreviewbutton.png" alt="" width="100%" height="100%"/>


<a name="improve"></a>
## Improvements for the Future
Future improvements for the project would mostly be focused on the development stage. As the source code grew for my application it became more difficult to navigate around and due to my lack of knowledge and experince it was hard to keep up. In the future I can: 

- Seperate my routes.py file. Each route can be subdivided in their own category where Add review can be in its own file
- The current state of the app is fairly simple, in the future I would hope to add more functionalities or more complex services to the ones already in place. I would also improve general layout/design of the .html pages by using CSS or Bootstrap
- Use of integrated testing in the future as some of the services cannot currently be tested or must be tested when run as a Flask app (without Docker/Jenkins) as this would make the app more stable.
- Make my web app Mobile friendly, since most websites today are accessed over mobile
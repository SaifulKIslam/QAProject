# Book Review Application

<a name="intro"></a>
## Introduction
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
- [User Interface Design](#UID)
    - [Page: Home](#home)
    - [Page: Add Series name](#addSN)
    - [Page: Review Series](#revS)
    - [Page: View Review](#virev)
- [Potential Improvements](#improve)

<a name="brief"></a>
## Project Brief
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

The ERD below shows the relationship between the databases.
    <img src="/Documentation/ERD.png" alt="ERD" width="100%" height="100%"/>
    
    
<a name="ci"></a>
## CI Pipeline

A CI pipeline was involved in the development and deployment of the project, a mock-up of this can be seen below.

<img src="/Documentation/CI Pipeline.png" alt="CI" width="100%" height="100%"/>

<a name="use_case"></a>
### Project Planning & User Stories 

For the project planning tool i used Jira to keep track of tasks and update what needed to be done or has been completed.
Below is a screenshot of the Jira board.

[Trello Board](https://trello.com/b/siBc2gmV/fundamental-qa-project)

<img src="/Documentation/Trello Board.png" alt="Trello" width="100%" height="100%"/>

### User Case Overview

<img src="/Documentation/Use case Overview.png" alt="Usecase" width="100%" height="100%"/>

### Use Stories Overview
Below are the user stories according to the planned uses for the application and their  requirement according to  MoSCoW (Must, Shoud, Could, Would) scale

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
Testing was an essential part of development to ensure that the planned uses were delivered and working. Pytest was used to test my application. The test coverage report for my application was 79%. Tests fot individual core functions such as adding a book title, adding a review, updating and deleting books were also carried out with Pytest. As per the coverage report most of the application was tested succefully and i was also able to understand where issues occurred.

<img src="/Documentation/Pytest-Cov.png" alt="ERD" width="100%" height="100%"/>
 

<a name="depl"></a>
## Deployment
Jenkins (a continuouse integration server) was used for the The deployment and also testing for the application. To do this i installed henkins into my GCP instance. I created a firewall rule to add port 8080 to the instance to create a deployment server.  I then installed Jenkins on the GCP instance terminal as a user, with enhanced User admissions to run sudo commands enabling me to deploy and test my app on the deployment server. Jenkins 
<img src="/Documentation/Jenkins.png" alt="CI" width="100%" height="100%"/>

I also deployed my web application in a production server using Gunicorn by running the below command. 
<img src="/Documentation/Gunicorn.png" alt="CI" width="100%" height="100%"/>

<a name=risks></a>
## Risk Assessment

I carried out a risk assessment in the planning stage to plan for issues that may have occurred. I included various risks that my project may come accross and have categorised them below to according to a high,medium, low risk rating, its impact, likelihood, likelihood rating and a suitable response. The risks can be seen as a combination of technical risks with the development of the project and general risks that will directly or indirectly impact the project.

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
* VSC: 
* Project Tracking: Jira
* Live Environment: GCP


<a name="UID"></a>
## User Interface Design

<a name="home"></a>
### Home Page
Home page consists of a home button

<img src="/Documentation/Home.png" alt="" width="100%" height="100%"/>


<a name="addSN"></a>
### Add a book Page
Clicking on the Add a book button you will direct you to the to the Add books page. 
<img src="/Documentation/AddSeries.png" alt="" width="100%" height="100%"/>

#### Home page after Adding books name
<img src="/Documentation/AddSeriesHome.png" alt="" width="100%" height="100%"/>
Once you add a book it will be displayed on the homepage.

<a name="revS"></a>
### Review book Page
#### Add review
To Add a review simply click the Add review button on the home page. That will then direct you to the add review page:

<img src="/Documentation/AddReview.png" alt="" width="100%" height="100%"/>

After adding your review you will be automatically directed to the Review page where you can view your reviews and other reviews on the book:

<img src="/Documentation/ReviewPage.png" alt="" width="100%" height="100%"/>


<a name="virev"></a>
### View Review Page
You can view reviews of each book by clicking the view review button under the specific book on the homepage:

<img src="/Documentation/viewreviewbutton.png" alt="" width="100%" height="100%"/>


<a name="improve"></a>
## Potential Improvements 

There are various development improvements that can be made. The application is fairly simple and my focus was on delivering a finctional app rather than delivering on further ideas which i coudl have included.

- I would improve the interface fir users; making it more user freindly by formatting. such as text font, colour size, background etc.

- I would also add further functionalties such as. Being able to delete individual reviews.

- Would create a seperate homepage and a seperate page for viewing all reviews; as currently my hompeage changes when reviews are added. 

- I would also remove the homepage button from my homepage.

- Use of integrated testing in the future as some of the services cannot currently be tested or must be tested when run as a Flask app (without Docker/Jenkins) as this would make the app more stable.

- Make my web app Mobile friendly, since most websites today are accessed over mobile
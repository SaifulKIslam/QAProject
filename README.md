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
    - [Page: Add Series name](#addbook)
    - [Page: Review Series](#reviewbook)
    - [Page: View Review](#viewrev)
- [Potential Improvements](#improve)

<a name="brief"></a>
## Project Brief
My project is to build an application where users can review books that they have read. 
Users will be able to:
* Create and add new books
* Delete exiting books
* Add reviews for books
* Update existing book titles
* Update existing reviews

<a name="appdes"></a>
### Application Design
The reviews and books data will be stored on an SQLlite database as it is a small file. This can be deployed on a SQL hosted databse via GCP if more memory is required.
Users will be able to Create, Read, Update and Delete from the database via the application interface accordingly.

<a name="erd"></a>
#### Entity Relationship Diagram
There will be two databases with a one-to-many realtionship.
* A Books database
* A Reviews database

The ERD below shows the relationship between the databases.
    <img src="/images/ERD.png"/>
    
    
<a name="ci"></a>
## CI Pipeline

A CI pipeline was involved in the development and deployment of the project, this can be seen below.

<img src="/images/Pipeline.png" alt="CI" width="100%" height="100%"/>

<a name="use_case"></a>
### Project Planning & User Stories 

For the project planning tool i used Jira to keep track of tasks and update what needed to be done or has been completed.
Below is a screenshot of the Jira board.

<img src="/images/Jira.png" alt="Trello" width="100%" height="100%"/>

### User Stories Overview
Below are the user stories according to the intended uses for the application and their MoSCoW (Must, Shoud, Could, Would) prioisting scale

|  | User Stories and their MoSCoW |
| ------ | ------ |
| MUST | As a user, I want to be able to access the app online |
| MUST | As a user, I want to be able to create reviews on the app |
| SHOULD | As a user, I want to be able to read reviews on the app |
| SHOULD | As a user I want to be able to update my reviews on the app |
| SHOULD | As a user I want to delete reviews on the app |
| COULD | As a user, I want to access the web on a mobile devices|
| Won't Have | As a user, I want to be able to create two of the same books tabs on the reviews on the app|


<a name="test_"></a>
## Testing (Unit Testing)
Testing was an essential part of development to ensure that the planned uses were delivered and working. I wrote my tests early on in the development stage to esnure my application functioned to its intended purpose. Pytest was used to test my application. The tests i raised passed 11 out of 11. The test coverage report for my application was 79%. Tests fot individual core functions such as adding a book title, adding a review, updating and deleting books were also carried out with Pytest. As per the coverage report most of the application was tested succefully and i was also able to understand where issues occurred.

<img src="/images/testing.png" alt="ERD" width="100%" height="100%"/>
 

<a name="depl"></a>
## Deployment
Jenkins (a continuouse integration server) was used for the The deployment of the application and can also be used for testing. To do this i installed Jenkins into my GCP instance. I created a firewall rule to add port 8080 to the instance to create a deployment server.  I then installed Jenkins on the GCP instance terminal as a user, with enhanced User admissions to run sudo commands enabling me to deploy and test my app on the deployment server. Jenkins. I included the web hook option to trigger a build of the job.
<img src="/images/Jenkins.png" alt="CI" width="100%" height="100%"/>

I also deployed my web application in a production server using Gunicorn using the below command. 
<img src="/images/Gunicorn.png" alt="CI" width="100%" height="100%"/>

<a name=risks></a>
## Risk Assessment

I carried out a risk assessment in the planning stage to plan for issues that may have occurred. I included various risks that my project may come accross and have categorised them below to according to a high,medium, low risk rating, its impact, likelihood, likelihood rating and a suitable response. The risks can be seen as a combination of technical risks with the development of the project and general risks that will directly or indirectly impact the project.

<img src="/images/RiskAssessment.png" alt="CI" width="100%" height="100%"/>


<a name="tech"></a>
### Technologies Used
* Database: GCP SQL Server/SQL lite
* Programming language: Python
* Framework: Flask
* Deployment: Gunicorn
* CI Server: Jenkins
* Test Reporting: Pytest
* VCS: Github
* Project Tracking: Jira
* Live Environment: GCP


<a name="UID"></a>
## User Interface Design

<a name="home"></a>
### Home Page
Home page consists of a home button and add book button:

<img src="/images/Homepage.png" alt="" width="100%" height="100%"/>


<a name="addbook"></a>
### Add a book Page
Clicking on the Add a book button you will be directed to the to the Add books page. 
<img src="/images/Addbookpage.png" alt="" width="100%" height="100%"/>

#### Home page after Adding books name
<img src="/images/Booksreviewpage.png" alt="" width="100%" height="100%"/>
Once you add a book it will be displayed on the homepage.

<a name="reviewbook"></a>
### Review book Page
#### Add review
To Add a review simply click the Add review button on the home page under teh specific book. That will then direct you to the add review page:

<img src="/images/Addreviewpage.png" alt="" width="100%" height="100%"/>

After adding your review you will be automatically directed to the Review page where you can view your reviews and other reviews on the book:

<img src="/images/Reviewspage.png" alt="" width="100%" height="100%"/>


<a name="viewrev"></a>
### View Review Page
You can view reviews of each book by clicking the view review button under the specific book on the homepage:

<img src="/images/Multiplereviews.png" alt="" width="100%" height="100%"/>


<a name="improve"></a>
## Potential Improvements 

There are various development improvements that can be made. The application is fairly simple and my focus was on delivering a finctional app rather than delivering on further ideas which i coudl have included.

- I would improve the interface fir users; making it more user freindly by formatting. such as text font, colour size, background etc.

- I would also add further functionalties such as. Being able to delete individual reviews.

- Would create a seperate homepage and a seperate page for viewing all reviews; as currently my hompeage changes when reviews are added. 

- I would also remove the homepage button from my homepage.

- Use of integrated testing in the future as some of the services cannot currently be tested or must be tested when run as a Flask app (without Docker/Jenkins) as this would make the app more stable.

- Make my web app Mobile friendly, since most websites today are accessed over mobile
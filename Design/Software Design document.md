# Software Design Description
## For <project name> Home Loan Monitor</project>


<Institute> Easter Institute of Technology NZ Bachelor of Computing Systems  </Institute>
<course> ITPR7.508 Business Application Programming </course> <br>
<author>  Katherine Mulder & Alex Borawski </author> <br>
<date>  20/03/2024 </date>

Table of Contents
=================
- [Software Design Description](#software-design-description)
  - [For  Home Loan Monitor](#for--home-loan-monitor)
- [Table of Contents](#table-of-contents)
  - [Revision History](#revision-history)
  - [1. Introduction](#1-introduction)
    - [1.1 Document Purpose](#11-document-purpose)
    - [1.2 Subject Scope](#12-subject-scope)
    - [1.3 Definitions, Acronyms and Abbreviations](#13-definitions-acronyms-and-abbreviations)
      - [Data Design Diagrams](#data-design-diagrams)
    - [1.4 Software Development](#14-software-development)
  - [2. Analysis/ Reflection of Business Issues](#2-analysis-reflection-of-business-issues)
  - [3. Key areas of software application issues](#3-key-areas-of-software-application-issues)
    - [3.1 Reliability](#31-reliability)
    - [3.2 Scalability](#32-scalability)
    - [3.3 Performance](#33-performance)
    - [3.4 Maintainability](#34-maintainability)
    - [3.5 Security](#35-security)
    - [3.6 Usability](#36-usability)
    - [3.7 Compatibility](#37-compatibility)
  - [4. Analysis \& Reflection of the Program Specifications](#4-analysis--reflection-of-the-program-specifications)
    - [4.1 Graphical User Interface](#41-graphical-user-interface)
    - [4.2 Identification / Authorization](#42-identification--authorization)
    - [3.3 User Accounts](#33-user-accounts)
    - [3.4 Client Relation Features](#34-client-relation-features)
  - [5. System Overview](#5-system-overview)
  - [6. Data Design](#6-data-design)
    - [6.1 Entity Relationship Diagram](#61-entity-relationship-diagram)
    - [6.2 Data Flow Diagram](#62-data-flow-diagram)
  - [7. System Design](#7-system-design)
    - [7.1 User Case Diagram](#71-user-case-diagram)
    - [7.2 Sequence Diagram](#72-sequence-diagram)
    - [7.3 Activity Diagram](#73-activity-diagram)
    - [7.4 Class Diagram](#74-class-diagram)
  - [8. Interface Design](#8-interface-design)
    - [8.1 Wireframes](#81-wireframes)
  - [9. Test Framework](#9-test-framework)
  - [10. Conclusion](#10-conclusion)
- [Software Design Description](#software-design-description)
  - [For  Home Loan Monitor](#for--home-loan-monitor)
- [Table of Contents](#table-of-contents)
  - [Revision History](#revision-history)
  - [1. Introduction](#1-introduction)
    - [1.1 Document Purpose](#11-document-purpose)
    - [1.2 Subject Scope](#12-subject-scope)
    - [1.3 Definitions, Acronyms and Abbreviations](#13-definitions-acronyms-and-abbreviations)
      - [Data Design Diagrams](#data-design-diagrams)
      - [Software Development](#software-development)
  - [2. Analysis/ Reflection of Business Issues](#2-analysis-reflection-of-business-issues)
  - [3. Key areas of software application issues](#3-key-areas-of-software-application-issues)
    - [3.1 Reliability](#31-reliability)
    - [3.2 Scalability](#32-scalability)
    - [3.3 Performance](#33-performance)
    - [3.4 Maintainability](#34-maintainability)
    - [3.5 Security](#35-security)
    - [3.6 Usability](#36-usability)
    - [3.7 Compatibility](#37-compatibility)
  - [4. Analysis \& Reflection of the Program Specifications](#4-analysis--reflection-of-the-program-specifications)
    - [4.1 Graphical User Interface](#41-graphical-user-interface)
    - [4.2 Identification / Authorization](#42-identification--authorization)
    - [3.3 User Accounts](#33-user-accounts)
    - [3.4 Client Relation Features](#34-client-relation-features)
  - [5. System Overview](#5-system-overview)
  - [6. Data Design](#6-data-design)
    - [6.1 Entity Relationship Diagram](#61-entity-relationship-diagram)
    - [6.2 Data Flow Diagram](#62-data-flow-diagram)
  - [7. System Design](#7-system-design)
    - [7.1 User Case Diagram](#71-user-case-diagram)
    - [7.2 Sequence Diagram](#72-sequence-diagram)
    - [7.3 Activity Diagram](#73-activity-diagram)
    - [7.4 Class Diagram](#74-class-diagram)
  - [8. Interface Design](#8-interface-design)
    - [8.1 Wireframes](#81-wireframes)
  - [9. Test Framework](#9-test-framework)
  - [10. Conclusion](#10-conclusion)

## Revision History
| Name | Date    | Reason For Changes  | Version   |
| ---- | ------- | ------------------- | --------- |
|      |         |                     |           |
|      |         |                     |           |
|      |         |                     |           |

## 1. Introduction 
> The following Software Design Description document outlines the design and architecture of a proposed Home Loan Monitor Tool. This tool aims to simplify mortgage management processes for individuals by offering a user-friendly interface and comprehensive features. It's important to note that this proposal is intended for personal use only and is not designed for financial advisers or professional consultation. <br><br>
The SDD serves as a detailed guide for developers, stakeholders, and users, providing insights into the software's functionality, structure, and behavior. This including data design, system design, interface design, and testing framework. <br>
>

### 1.1 Document Purpose
The reason we're writing this document is to explain how the Home Loan Monitor Tool will work and how it's built. We want to make it easy for everyone involved to understand how the software will function and what it will look like.
We have also conducted a user required specifications document defines what users expect from this project.
* Users/ Project manager: This document serves as a guide for both project managers and users of the mortgage management tool. It provides the software's functionality, design rationale, usability aspects, and system behavior. By understanding these details, users and project manager can make informed decisions about the project, while users can utilize the software to meet their needs.
* Developers: This guide helps developers understand how the software is designed, the important decisions made about its structure, and how it's built. It's like a roadmap for them to turn requirements into a working program.

### 1.2 Subject Scope

**Scope Summary:**
- **Project Includes:**
> The home loan monitor will contain the following key functionalities:

The home loan monitor will contain the following key functionalities:
1.	Initial set up
2.	Update mortgage
3.	Transaction reporting
4.	Mortgage editing
5.	Authentication
6.	Visualization chart

  
**Project Excludes:**
1.	Complex mortgage type
2.	Deployment
3.	SEO services
4.	Maintenance and updates
5.	Advanced financial analysis
6.	Legal advice
7.	Tax advice
8.	Integration with external systems

_Note: Please read URS for more information_

### 1.3 Definitions, Acronyms and Abbreviations
#### Data Design Diagrams 
1. **ERD**:
   - Definition: Entity-Relationship Diagram.
   - Description: A visual representation of the entities and relationships within a database. It illustrates how entities relate to each other within a database model.

2. **DFD**:
   - Definition: Data Flow Diagram.
   - Description: A graphical representation that shows the flow of data within a system. It visualizes the processes, data stores, and data flows involved in a system or business process.

### 1.4  Software Development  
1. Python:
Backend logic and data processing.
2. Flask (Web Framework):
Handling HTTP requests and responses.
Routing URLs to appropriate functions.
Serving HTML templates.
3. HTML, CSS, Bootstrap (Frontend):
Structuring and styling the user interface.
Using Bootstrap for responsive design and pre-styled components.
4. JavaScript:
Implementing client-side interactivity (optional).
Validating user inputs.
5. Pytest (Testing Framework):
Writing and running unit tests to ensure code quality and functionality.
6. Postgres:
Storing mortgage data.
Managing transactions and updates.

## 2. Analysis/ Reflection of Business Issues
1. Business Objectives:  Our main goal is to develop a user-friendly mortgage calculator for individuals. This tool will help them accurately estimate their mortgage payments based on factors like loan amount, interest rate, and loan term.
2. Business Processes: Our software will simplify the process of estimating mortgage payments. Users will be able to input their loan details, and the software will automatically calculate and present the results clearly.
3. Regulatory and Compliance Requirements: Since the software is for individual use, it doesn't fall under specific financial regulations.
4. Risk Analysis: There are some technical risks due to our team's limited experience, but we can manage these with guidance from our lecture. Limited resources and time pose business risks, so we need to make sure to meet the declines.
5. Reflection on Business Issues: Our project aligns well with our team's abilities. Guidance from our instructor will help us overcome challenges. We're focusing on creating value for individual users without unnecessary complexity.
6. Recommendations: Prioritize simplicity and usability. Maintain regular communication with our lecture for guidance. Break the project into manageable tasks with realistic milestones for tracking progress.

_Note: Please read URS for more information_
## 3. Key areas of software application issues

### 3.1 Reliability 
### 3.2 Scalability
### 3.3 Performance
### 3.4 Maintainability
### 3.5 Security
### 3.6 Usability 
### 3.7 Compatibility


## 4. Analysis & Reflection of the Program Specifications

### 4.1 Graphical User Interface
### 4.2 Identification / Authorization
### 3.3 User Accounts 
### 3.4 Client Relation Features 

## 5. System Overview 
> A guide to understanding a system. It tells you what the system does, who uses it, and how it works. 
> It also mentions things like its parts, how it connects to other systems, what technology it uses, and how it's kept secure and working well. 
> It's like a map that helps you get the big picture before diving into the details.
> In the system overview selection here will provide datat design, system design and interface design.

## 6. Data Design
### 6.1 Entity Relationship Diagram
> The purpose of the Entity-Relationship Diagram(ERD) is to visually represent the structure of the database for the mortgage calculator,
By mapping out entities like "User," "mortgage," "transaction, along with their attributes and relationships.
The ERD will provide a clear understanding of how data is organized within the system. 


> ![ERD](ERD.png)
### 6.2 Data Flow Diagram
> The Data Flow Diagram (DFD) serves to illustrate the flow of data within the system, showing how data is input, processed, and output. It helps to understand the flow of information and the interactions between different components within the software. <br>

> ![DFD](DFD.png)

## 7. System Design 
### 7.1 User Case Diagram
> The use case diagram outlines the interactions between users and the system, including the primary functions such as calculating mortgage payments, viewing amortization schedules, adjusting parameters, and accessing mortgage features.<br>
> ![ user case diagram](usercase.png)

### 7.2 Component Diagram
> The component diagram shows the overview of how the components of our software will be designed and comunicate with each other. As shown in the diagram below, the software will need to communicate externally with Postgres to store the data, which is then handled by the Data Models, ran through the analysis, amortization and graphing components to then produce the interface. <br>
> ![component diagram](component_diagram.png)

### 7.3 Activity Diagram
>The activity diagram is the sequence of actions involved in performing tasks such as inputting data, calculating mortgage payments, viewing amortization schedules, adjusting parameters, and so on. Each activity is connected through transitions, showing the flow of control within the system.<br>
> 1. User login activity diagram
> ![activity_diagram_add_mortgage](activity_diagram_add_mortgage.png) 
> 2. User update mortgage activity diagram
> ![activity_diagram_edit_transaction](activity_diagram_edit_transaction.png)
> 3. User viewing mortgage activity diagram
> ![activity_diagram_transaction_analysis](activity_diagram_transaction_analysis.png)
> 4. User viewing mortgage activity diagram
> ![activity_diagram_user_login](activity_diagram_user_login.png)
### 7.4 Class Diagram
> The class diagram shows the structures of the various classes used throughout the application as well as the methods that are inherent to those classes. This helps drive our ovject orientated programming to work smoothly.
> ![class diagram](Class_Diagram.png)


## 8. Interface Design
### 8.1 Wireframes
A skeletal outline of the webpage, those wireframes shows the structure and placement of elements. 
<br><br>**User login page** 
when users open up the webpage. This log in page will display before entry the calculator.
This page gives users options for log-in and sign-up an account also try it out.
> ![login page](wireframe_user_login.png)

<br><br>**Sign up page**: 
In this page will grab user's username and password details. Alternately, User can still log in if they remember their login details after enter this page, or they can try the calculator without an account.
> ![signup page](wireframe_sign_up.png)

<br><br>**Index page**: User will be able to view their transaction reports on this page. Where users can edit payment date, delete transaction, add new mortgage and update mortgage.
![wireframe_index](wireframe_index.png) 

<br><br>**Add mortgage page**: After the user logs in or clicks the 'Try it out' button, the adding new mortgage page will be displayed.
This page allows users to input new mortgage information.
> ![wireframe_add_mortgage](wireframe_add_mortgage.png)

<br><br>**update mortgage page**: After a new mortgage is established, user will be able to edit mortgage on this page.
This page will display current mortgage details and allow users to update the information. 
Users can analysis override payment and add extra costs if there is any. A comment textarea for comment on the costs.  
> ![wireframe_update_mortgage](wireframe_update_mortgage.png)

<br><br>**Deleting Data Page**: If users wish to delete existing transactions or mortgages, they can access this page through the removing data button on the index page.
They will see a table of both mortgages and transactions with identifying information so that they can remove exactly what they want to remove.
 > ![wireframe_delete_data](wireframe_removing_data.png)

<br><br>**User account settings**: 
The username will display as default and user can change password.
> ![wireframe_user_settings](wireframe_user_settings.png)

<br><br>**User account icon**:
When user clicks the user icon on the top right page then a pop up window will appear for user to update their account information.
> ![wireframe_user_popup_window](wireframe_user_popup_window.png)


## 9. Test Framework
_Unit Testing_
<br> The main objective is to isolate written code and determine if it works as it should, so we can detect early flaws in code.
We will focus on creating unit test cases before developing the actual code by using automated unit testing for validating the functionality.




## 10. Conclusion

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
<<<<<<< Updated upstream:Design/Software Design document.md
    - [1.5 Overview of documentation](#15-overview-of-documentation)
  - [2. Analysis/ Reflection of Business Issues](#2-analysis-reflection-of-business-issues)
=======
  - [2. Analysis/ Reflection of Business Issues (katherine)take what we did in the propsal and take it deeper](#2-analysis-reflection-of-business-issues-katherinetake-what-we-did-in-the-propsal-and-take-it-deeper)
>>>>>>> Stashed changes:Design/SDD.md
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

<<<<<<< Updated upstream:Design/Software Design document.md
## 1. Introduction
> This section should provide an overview of the entire document
=======
## 1. Introduction 
> The following Software Design Description document outlines the design and architecture of a proposed Home Loan Management Tool. This tool aims to simplify mortgage management processes for individuals by offering a user-friendly interface and comprehensive features. It's important to note that this proposal is intended for personal use only and is not designed for financial advisers or professional consultation. <br><br>
The SDD serves as a detailed guide for developers, stakeholders, and users, providing insights into the software's functionality, structure, and behavior. This including data design, system design, interface design, and testing framework. <br>
>
>>>>>>> Stashed changes:Design/SDD.md

### 1.1 Document Purpose
The reason we're writing this document is to explain how the Home Loan Management Tool will work and how it's built. We want to make it easy for everyone involved to understand how the software will function and what it will look like.

* Users/ Project manager: This document serves as a guide for both project managers and users of the home loan management tool. It provides the software's functionality, design rationale, usability aspects, and system behavior. By understanding these details, users and project manager can make informed decisions about the project, while users can utilize the software to meet their needs.
* Developers: This guide helps developers understand how the software is designed, the important decisions made about its structure, and how it's built. It's like a roadmap for them to turn requirements into a working program.

### 1.2 Subject Scope

**Scope Summary:**
- **Project Includes:**
1. Development of a mortgage calculator module enabling users to calculate monthly or fortnightly payments based on loan amount, interest rate, and loan term.
2. Incorporation of the ability to compare multiple loans and interest rates.
3. Enablement of users to input variable interest rates over specific periods and automatically update mortgage calculations accordingly.
4. Inclusion of a feature to view historical mortgage data.
5. Support for managing multiple mortgages, allowing users to handle multiple properties simultaneously.
6. Addition of a chart to display mortgage data.
7. Provision of user-friendly interface webpages.
8. Inclusion of thorough testing procedures to ensure the software functions as expected and meets quality standards.
9. Implementation of authentication features for multi-user access.
10. Provision of comprehensive documentation covering usage instructions.
11. Design of the software with scalability and performance in mind to handle a growing user base and large datasets.
12. Analysis & Reflection of Business Issues.
  
- **Project Excludes:**
1. The actual deployment of the website onto designated servers.
2. Extensive SEO services such as keyword research, on-page optimization, or link building.
3. Custom graphic design services beyond the scope of interface design and layout.
4. The necessary maintenance and updates for the software post-project completion.
5. Advanced financial analysis beyond basic mortgage calculations, such as investment analysis, risk assessment, or portfolio management.
6. Legal advice related to mortgages, including contract terms, legal obligations, or regulatory compliance. Users would need to consult legal professionals for such matters.
7. Property valuation services, including home appraisals or estimates of property values.
8. Tax advice or calculations of property taxes. Users would need to consult with tax professionals or refer to relevant tax regulations.
9. While homeowners’ insurance and mortgage insurance are integral to homeownership, the software will not calculate insurance premiums.
10. Integration with banking systems, financial institutions, or real estate databases.
11. Detailed analytics or reporting features beyond basic mortgage calculations will be excluded.
12. Complex mortgage types, such as adjustable-rate mortgages (ARMs) with various index rates and margins, will be excluded for simplicity.

### 1.3 Definitions, Acronyms and Abbreviations

1. **ERD**:
   - Definition: Entity-Relationship Diagram.
   - Description: A visual representation of the entities and relationships within a database. It illustrates how entities relate to each other within a database model.

2. **DFD**:
   - Definition: Data Flow Diagram.
   - Description: A graphical representation that shows the flow of data within a system. It visualizes the processes, data stores, and data flows involved in a system or business process.

3. **Python**:
   - Definition: Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

4. **Flask Framework**:
   - Definition: Flask is a micro web framework written in Python.
   - Description: Flask provides tools, libraries, and technologies for building web applications. It is lightweight and modular, allowing developers to add only the components they need. Flask is known for its simplicity and flexibility.

5. **Postgres**:
   - Definition: PostgreSQL.
   - Description: PostgreSQL is an open-source relational database management system (RDBMS) known for its reliability, robustness, and advanced features. It supports SQL and is highly extensible, allowing users to define custom data types, functions, and more.

6. **Pytest**:
   - Definition: Pytest is a testing framework for Python.
   - Description: Pytest is a popular testing framework used for writing simple and scalable test cases in Python. It supports fixtures, parameterized testing, and assertions, making it suitable for testing various types of applications and libraries.



## 2. Analysis/ Reflection of Business Issues

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
>

## 6. Data Design
### 6.1 Entity Relationship Diagram
### 6.2 Data Flow Diagram

## 7. System Design 
### 7.1 User Case Diagram
### 7.2 Sequence Diagram
### 7.3 Activity Diagram


## 8. Interface Design
### 8.1 Wireframes

## 9. Test Framework


## 10. Conclusion
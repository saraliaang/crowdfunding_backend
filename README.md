# crowdfunding_backend
SheCodes Python django project

# Crowdfunding Back End
Sara Liang 

## Planning:
### 🕰 The PastPort Project
**What if you can witness the building of the Great Pyrimid with your own eyes?** 
What if you can say good bye to a loved one that you never got a chance to? Or walk in the streets in Paris when it was a movable feast, alongside with Hemingway and Fitzgerald?

Fundraiser Purpose: Users pledge money to gain access to the time machine for a personal trip to the past 

### Intended Audience

- **History Enthusiasts** – who want to witness key moments in history firsthand, from the signing of the Declaration of Independence to the invention of sliced bread.  
- **Regret Fixers** – individuals seeking to right past wrongs, make different choices, or prevent themselves from sending that one embarrassing text.  
- **Investors in Science & Adventure** – people who believe in pushing humanity beyond the limits of physics (and who also enjoy bragging about funding “faster-than-light” travel).  
- **Thrill Seekers** – daredevils eager to experience warp-speed nausea and the risk of minor to severe temporal paradoxes.  
- **Celebrity Time-Tourists** – *"I just want to take a selfie from 1923 and post it on intagram"*



### ✨ Front-end and Features  

#### 1. Home Page
- **Animated Landing Section** – Spaceship animation to welcome users, showcasing front-end animation skills.  
- **Featured Fundraisers (Kickstarter Style)** – Display the top open fundraiser (highese pledge).  
  - **Call-to-Action** – Prominent “Back This Project” button &rarr; route to *Pledge Page*.

- **Time Machine Recommendation / Review** - Playful endorsements to make the the page engaging.

- **Fund Your Trip** - Button to allow users to pledge or create their own campaign &rarr; route to *Creat New Fundraiser Page*.


#### 2. Create New Fundraiser Page
- **Form with Fundraiser Details** – Users can create a new fundraising campaign by entering:
  - **Title** - name of the trip
  - **Owner** - a user who created the project
  - **Description** - What the user hopes to experience 
  - **Time_Created** - Auto generated time stamp
  - **Destination year** - The year the user wants to travel  to(numeric)
  - **Image URL** - Image of the destination
  - **Submit Button**

- **Automatic Goal Calculation** - The funding goal is derived from the destination year:
  - Example: 300 years ago &rarr; 1.3c &rarr; $100,000,000
  - Longer trip requires higher speed &rarr; higher pledges
  
- **Form Validation & Error Pages** – Friendly error messages if fields are missing, invalid, or incorrected formatted.

- **Status** - Users can open/close their fundraisers; the time machine will be marked ready automatically when pledges reach the goal.

#### 3. Pledge Page

- Users can pledge money toward the fundraiser.  
- **Live Progress Bar Animation** – Fills according to total pledges vs goal, visualizing “how close we are to time departure.”  
- **Pledge Animation** - After pledging, will show a speeding up of progress animation &rarr; *“Current speed, 0.76c -- we're almost fast enough to reach 1856!”*

#### 4. REST API Backend
- Built with **Django REST Framework** to handle fundraisers, pledges, and progress calculations.  

#### 5. React Front-End
- Interactive UI with dynamic updates for pledges and progress.  
- Smooth animations for landing page and progress bar.  

#### 6. Error Handling & UX
- Custom error pages for invalid routes or failed actions (e.g., failed pledge submission).  
- Friendly messages and animations to keep the experience engaging.  

#### Optional Extra Features
- Display backer count and pledge amounts similar to Kickstarter.  
- Fun “time travel milestones” as users hit funding thresholds (small animations or icons along the progress bar).



### API Spec


| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- | ------------ | --------------------- | ---------------------------- |
| /fundraisers | GET | Fetch all fundraisers | N/A | 200 | None |
| /fundraisers/<:id> | GET | Fetch a fundraiser | N/A | 200 | None |
| /fundraisers | POST | Create a new fundraiser| JSON Payload | 201 | Any logged in user |
| /fundraisers/<:id> | DELETE | Delete a fundraiser| JSON Payload | 204 | Creator of the fundraiser |
| /fundraisers/<:id>| PUT | update the description and image | JSON Payload | 200 | Creator of the fundraiser |
| /user | POST | Create a user account | N/A | 200 | None |
| /pledges | POST | Create a pledge | N/A | 200 | None |



### DB Schema
![]( database.drawio.svg)


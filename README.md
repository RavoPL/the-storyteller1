![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# The Storyteller
Developed by **Dorian Wolarz**, a Code Institute Student

*The Storyteller is a Full Stack website which works as a mini blog. Users can create personal accounts and afterwards they can create, share and comment on each other's short stories. In a general sense it will be a very primitive version of WordPress or WattPad.*

[LINK TO HEROKU VERSION](https://the-storyteller1-c9b741a61416.herokuapp.com/)

![The Storyteller on a PC](N/A)

## Contents
1. [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Stories](#user-stories)
       - [Admin Stories](#admin-stories)
       - [User Stories](#user-stories)
3. [Design](#design)
    - [Design Choices](#design-choices)
    - [Colour and Fonts](#colour-and-fonts)
    - [Structure](#structure)
    - [Wireframes](#wireframes)
4. [Features](#features)
    - [Story Submission](#story-submission)
5. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Tools and Websites](#tools-and-websites)
6. [Testing and Validation](#testing-and-validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [Python Validation](#python-validation)
    - [Accessibility and Performance](#accessibility-and-performance)
    - [Manual Testing of Admin and User Stories](#manual-testing-of-admin-and-user-stories)
       - [Admin Stories Testing](#admin-stories-testing)
       - [User Stories Testing](#user-stories-testing)
7. [Known Bugs](#known-bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)
    - [Code and Assets](#code-and-assets)
    - [Media](#media)

## Project Goals

### User Goals

* Easily navigate across a clean user interface.
* Read highly engaging short stories.
* Like existing stories.
* Comment on existing stories.
* Submit a Short Story for review.

### Site Owner Goals

* Facilitate the existence of a creative environment where authors can share stories with readers.
* Promote user engagement by allowing users to like and comment on stories.
* Promote creativity by reaching out to up and coming writers of various genres.
* Acquire new talent and content by reviewing submitted stories.

## User Experience

### Target Audience

* Authors of short stories and fanfictions wanting to publish their work and have it received by readers.
* Readers who want to read short stories and engage with the material by liking and commenting.

### User Requirements and Expectations

* A well structured, user-friendly and efficient webpage.
* Simple and intuitive navigation system.
* A glitchless experience with features that work properly.
* An interactive environment where users can rate short stories and leave comments.
* A level of accessibility for students and new users with disabilities.

### User Stories

For the purpose of this project I have created a list of fitting user and admin stories to serve as a design guide in creating this webpage. *The Storyteller* is a mini blog webpage for sharing short stories and, as such, I based it on the Code Institute project of *I Think Therefore I Blog* given the similar theme. I've come up with the following user and admin stories thus far:

#### Admin Stories

* As a **site admin** I can **create, read, update and delete posts** so that **I can manage the content of the entire website**.
* As a **site admin** I can **create drafts** so that **I can finish creating the content at a later stage**.
* As a **site admin** I can **approve or deny user comments** so that **I can filter out objectionable comments**.
* As a **site admin** I can **approve or deny a short story** so that **I can filter aspiring writers according to their skill and creativity**.


#### User Stories

* As a **site user** I can **register for a new account** so that **I can use the website's full functionality**.
* As a **site user** I can **log in to my account**.
* As a **site user** I can **log out of my account**.
* As a **site user** I can **click on a post** so that **I can read the full text**.
* As a **site user** I can **like or unlike** a post so that **I can interact with the content other users have created**.
* As a **site user** I can **view the comments under a post** so that **I can read the feedback other users have shared**.
* As a **site user** I can **comment under a post** so that **I can share my own feedback under other users' content**.
* As a **site user** I can **view a paginated list of blog posts** so that **I can easily select a post I want to view**.
* As a **site user** I can **view a list of blog posts** so that **I can view a post**.
* As a **site user** I can **view the number of likes on each post** so that **I can see which short stories people enjoy the most**.
* As a **site user** I can **submit a short story for review** so that **I can contribute to the website's content**.

## Design

### Design Choices

The webpage was designed with the concept of a writer's blog in mind, hence I decided to call it *"The Storyteller"* in order to elicit a certain image of a cozy campfire and an elderly, wise gentleman with a smoking pipe. The website is meant to facilitate the posting of stories from different authors by the Admin, which are then published on the home page and can be interacted with by readers. The chosen artistic direction is meant to be clean, organized and easily navigable. The content of the webpage is neatly divided between collapsible buttons in the case of mobile view and interactive buttons in the case of widescreen view.

### Colour and Fonts

![Image of Coolors Color Wheel](static/media/others/colourpalette.jpg)

Colour tones associated with classic typewriters were chosen as basis for the colour palette of the webpage. As such, the main colours are the natural and basic contrast of dark grey and white to symbolize black letters upon white parchment. The complimentary colours chosen were neutral greys and a light blue, almost turqouise highlight for mouse hover. My intent was to bring the readers back to a simpler time almost a decade and a half ago now, when the internet was still in its developing stages and was populated mostly by amateur websites, far away from the monopoly of large corporations. This visual style is a nostalgic callback to my time as a child when I would spend evenings typing short stories and post them to my Wordpress. At the same time however I made use of modern UI/UX design solutions in order to provide a visually pleasing, clear and usable webpage.

For the heading and menu fonts I chose *"Lora"* backed up by *"Helvetica Neue"* because they effectively compliment one another and are very clean.
For the main heading fonts I chose *"Open Sans"* backed up by *"Helvetica Neue"* because the fonts are pleasing to the eye, soft and rounded.
*Arial* and *Sans-Serif* were chosen as the emergency backup fonts in case the selected ones refuse to load because they're basic fonts that should display without any issues on all devices and software.

### Structure

The website is structured in a user friendly way that makes navigation of its contents extremely easy and makes it pleasing to the eye. The *Home Page* serves as the central hub of the design, allowing for quick access to other sections of the project through fully interactive buttons. More details on the project and its aims are stored in the *About* page. The users can *Register*, *Login* and *Logout*. Each article and short story is stored in a separate page. As such, the website consists of de facto six separate pages:
* **The Home Page**, with its selection of buttons and a collapsible menu for mobile users.
* **About Page**, with its short writeup on the project and its goals.
* **Register Page**, with its easy-to-use registration system for new users.
* **Login Page**, with its username and password login options for existing users.
* **Logout Page**, with its easy-to-use logout option for logged in, existing users.
* **Article Page**, which displays each article and short story in a separate view.

### Wireframes

<details>
  <summary>Personal Computer View</summary>
  <img src="static/media/others/pchomepage.jpg" alt="Wireframe of PC Home Page" title="PC Home Page Wireframe">
</details>

<details>
  <summary>Mobile View</summary>
  <img src="static/media/others/mobilehomepage.jpg" alt="Wireframe of Mobile Home Page" title="Mobile Home Page Wireframe">
</details>

<details>
  <summary>User Stories Flow Chart</summary>
  <img src="static/media/others/userstoriesplan.jpeg" alt="Flow Chart of User Stories" title="User Stories Flow Chart">
</details>

## Features

### Story Submission

Custom *Story Submission* model - **FINISHED**

Corresponding to **User Story - Approve or Reject Short Story**([#18](https://github.com/RavoPL/the-storyteller/issues/18))

![Image of My Story Submission Model](static/media/others/storysubmission.png)

## Technologies Used

### Languages

* HTML 5
* CSS 3
* Python 3

### Tools and Websites

* Git *for version control*
* GitHub *to store code and deploy the website*
* GitPod *as an IDE to build the project and edit the code*
* Django *as framework to develop the project*
* Heroku *to deploy the project and host it*
* Bootstrap *to access HTML design templates*
* Crispy Forms *to access and display premade forms on the website*
* Fontawesome *to access free icons*
* GoogleFonts *to access different font styles*
* Coolors *to generate colour palette for ReadMe*
* Lucidchart *to plan out a diagram of user stories*
* Django Summernote *for visualization of post creation and edits*
* FreeFormatter HTML Checker *to validate HTML*
* W3C CSS Checker *to validate CSS*
* ExtendClass Python Syntax Checker *to validate Python code*

## Testing and Validation

### HTML Validation

<details>
  <summary>Base Validation</summary>
  <img src="static/media/others/html_base_validation.png" alt="Base Validation" title="Base HTML Validation">
</details>

<details>
  <summary>About Us Validation</summary>
  <img src="static/media/others/html_aboutus_validation.png" alt="About Us Validation" title="About Us HTML Validation">
</details>

<details>
  <summary>Index Validation</summary>
  <img src="static/media/others/html_index_validation.png" alt="Index Validation" title="Index HTML Validation">
</details>

<details>
  <summary>Post Detail Validation</summary>
  <img src="static/media/others/html_postdetail_validation.png" alt="Post Detail Validation" title="Post Detail HTML Validation">
</details>

### CSS Validation

<details>
  <summary>CSS Validation</summary>
  <img src="static/media/others/css_validation.png" alt="CSS Validation" title="CSS Validation">
</details>

### Python Validation

<details>
  <summary>admin.py Validation</summary>
  <img src="static/media/others/python_admin_validation.png" alt="Admin Validation" title="Admin Python Validation">
</details>

<details>
  <summary>forms.py Validation</summary>
  <img src="static/media/others/python_forms_validation.png" alt="Forms Validation" title="Forms Python Validation">
</details>

<details>
  <summary>models.py Validation</summary>
  <img src="static/media/others/python_models_validation.png" alt="Models Validation" title="Models Python Validation">
</details>

<details>
  <summary>urls.py Validation</summary>
  <img src="static/media/others/python_urls_validation.png" alt="Urls Validation" title="Urls Python Validation">
</details>

<details>
  <summary>views.py Validation</summary>
  <img src="static/media/others/python_view_validation.png" alt="Views Validation" title="Views Python Validation">
</details>

### Accessibility and Performance

<details>
  <summary>Main Page</summary>
  <img src="static/media/others/main_accperf.png" alt="Main Page Acc and Perf" title="Main Accessibility and Performance">
</details>

<details>
  <summary>About Us</summary>
  <img src="static/media/others/aboutus_accperf.png" alt="About Us Acc and Perf" title="About Us Accessibility and Performance">
</details>

### Manual Testing of Admin and User Stories

#### Admin Stories Testing

<br>

1. *As a site admin I can create, read, update and delete posts so that I can manage the content of the entire website.*

| **Feature**  | **Expected Result** | **Action Taken** | **Result** |
| ------------- | ------------- | ------------- | ------------- |
| Create Posts | A post can be created from admin view | Entered admin view and created a post | Works as Intended |
| Read Posts | A post can be read from admin view | Clicked an existing post in admin view and read its contents | Works as Intended |
| Update Posts | A post can be updated from admin view | Clicked an existing post in admin view and updated its contents | Works as Intended |
| Delete Posts | A post can be deleted in admin view | An existing test post was deleted in admin view | Works as Intended |

<br>

<br>

2. *As a site admin I can create drafts so that I can finish creating the content at a later stage.*

| **Feature**  | **Expected Result** | **Action Taken** | **Result** |
| ------------- | ------------- | ------------- | ------------- |
| Create Drafts | A draft can be created for a post | A test post was set to 'Draft' instead of 'Published' | Works as Intended |

<br>

<br>

3. *As a site admin I can approve or deny user comments so that I can filter out objectionable comments.*

| **Feature**  | **Expected Result** | **Action Taken** | **Result** |
| ------------- | ------------- | ------------- | ------------- |
| Approve and Deny Comments | Comment approved or denied | Approved test comment and denied test comment | Works as Intended |

<br>

<br>

4. *As a site admin I can approve or deny a short story so that I can filter aspiring writers according to their skill and creativity.*

| **Feature**  | **Expected Result** | **Action Taken** | **Result** |
| ------------- | ------------- | ------------- | ------------- |
| Approve and Deny Stories | Story approved or denied | Approved short story and denied short story | Works as Intended |

<br>

#### User Stories Testing

<br>

1. *As a site user I can register for a new account so that I can use the website's full functionality*.

| **Feature**  | **Expected Result** | **Action Taken** | **Result** |
| ------------- | ------------- | ------------- | ------------- |
| Registration | User Registrates an Account | Clicked on 'Register' and filled out the form | Works as Intended |

<br>

<br>

2. *As a site user I can log in to my account.*

| **Feature**  | **Expected Result** | **Action Taken** | **Result** |
| ------------- | ------------- | ------------- | ------------- |
| Log In | User Logs into an existing account | Clicked on 'Login' and filled out the form | Works as Intended |

<br>

<br>

3. *As a site user I can log out of my account.*

| **Feature**  | **Expected Result** | **Action Taken** | **Result** |
| ------------- | ------------- | ------------- | ------------- |
| Log Out | User Logs out of an existing account and returns to home page | Clicked on 'Logout' | Works as Intended |

<br>

<br>

4. *As a site user I can click on a post so that I can read the full text.*

| **Feature**  | **Expected Result** | **Action Taken** | **Result** |
| ------------- | ------------- | ------------- | ------------- |
| Read Post | User can access any post | Clicked on a short story | Works as Intended |

<br>

<br>

5. *As a site user I can like or unlike a post so that I can interact with the content other users have created.*

| **Feature**  | **Expected Result** | **Action Taken** | **Result** |
| ------------- | ------------- | ------------- | ------------- |
| Like and Unlike Post | User can like and unlike a post | Clicked the Heart symbol under a post | Works as Intended |

<br>

<br>

6. *As a site user I can view the comments under a post so that I can read the feedback other users have shared.*

| **Feature**  | **Expected Result** | **Action Taken** | **Result** |
| ------------- | ------------- | ------------- | ------------- |
| View Comments | User can read approved comments under a post | Clicked on a short story | Works as Intended |

<br>

<br>

7. *As a site user I can comment under a post so that I can share my own feedback under other users' content.*

| **Feature**  | **Expected Result** | **Action Taken** | **Result** |
| ------------- | ------------- | ------------- | ------------- |
| Comment | User can submit a comment under a post | Filled out the comment box and pressed 'Submit' | Works as Intended |

<br>

<br>

8. *As a site user I can view a paginated list of blog posts so that I can easily select a post I want to view.*

| **Feature**  | **Expected Result** | **Action Taken** | **Result** |
| ------------- | ------------- | ------------- | ------------- |
| Paginated Posts | User can view all the posts currently on the site | Entered Home Page | Works as Intended |

<br>

<br>

9. *As a site user I can view a list of blog posts so that I can view a post.*

| **Feature**  | **Expected Result** | **Action Taken** | **Result** |
| ------------- | ------------- | ------------- | ------------- |
| Posts | User can view all the posts currently on the site | Entered Home Page | Works as Intended |

<br>

<br>

10. *As a site user I can view the number of likes on each post so that I can see which short stories people enjoy the most.*

| **Feature**  | **Expected Result** | **Action Taken** | **Result** |
| ------------- | ------------- | ------------- | ------------- |
| Number of Likes | User can view current like number on the main page and each article page | Checked Home Page and Article Page | Works as Intended |

<br>

<br>

11. *As a site user I can submit a short story for review so that I can contribute to the website's content.*

| **Feature**  | **Expected Result** | **Action Taken** | **Result** |
| ------------- | ------------- | ------------- | ------------- |
| Submit Short Story | User can submit a short story from a form above the footer | Filled out the form and pressed 'Submit' | Works as Intended |

<br>

## Known Bugs

N/A

## Deployment

### GitHub

This project was deployed using *Code Institute's Python Template* on GitHub.

You can *deploy the repository* on GitHub by following these steps:

1. In your GitHub repository navigate to the *Settings* tab
2. In the menu on the left hand side select *Pages*
3. For the source of your repo select *branch: main*
4. After the webpage refreshes, you will see a ribbon on the top saying: *"Your site is published at https://ravopl.github.io/the-storyteller/"*

You can *fork the repository* by following these steps:

1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner

You can *clone the repository* by following these steps:

1. Go to the GitHub repository
2. Locate the Code button above the list of files and click on it
3. Select if you prefer to clone using HTTPS, SSH or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open GitBash
5. Change the current directory to the one you previously cloned
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press 'Enter' to create your local clone

### Heroku

This project was deployed using *Code Institute's Python Terminal* on Heroku.

After the repository is forked, you can deploy it by following these steps:

1. Create an account on Heroku or log into your existing one
2. Go to the *Dashboard*
3. Create a new app, add its name and your geographical region
4. Click on *Create App*
5. Go to your *Settings* tab
6. Under *Config Vars*, add **PORT** for key and **8000** for value
7. Click *Add*
8. Click *Add Buildpack*
9. Add **python** from the list and press *Save Changes*
10. Add **nodejs** from the list and press *Save Changes*
11. Ensure that python is placed **above** nodejs
12. Scroll up and click *Deploy*
13. Navigate to *Deployment Method* and click on *GitHub*
14. Confirm that you want to *Connect to GitHub* and link your account
15. Search for the GitHub repository you had previously forked
16. Click *Connect*
17. Scroll down and click on *Deploy Branch*

## Credits

### Code and Assets

* *Code Institute* for the CI Full template on GitHub
* *Code Institute* for the deployment terminal on Heroku
* *Code Institute* for *I Think Therefore I Blog*
* *Help with some code issues by my brother in faith Hassan Ali*
* [Basic Bootstrap Template (EDITED BY ME): *Clean Blog* by Start Bootstrap](https://startbootstrap.com/theme/clean-blog)
* [About Us Bootstrap Template (EDITED BY ME): *Bootstrap 5 About Us Page Section* by Bootstrap Brain](https://bootstrapbrain.com/component/bootstrap-about-us-page-section/)
* [TUTORIAL: *Django Recipes Full Stack App* by Dom Vacchiano](https://www.youtube.com/watch?v=w7EJu9Gd5Ns&list=PLQbt1tI_yQHg5HYpdUqit1wkc4BOPTkpx)

### Media

* [Typewriter Image by *American Farmhouse Style*](https://americanfarmhousestyle.com/wp-content/uploads/2021/10/IMG_1252.jpg)
* [Typewriter Logo Background by *BoostMeUp*](https://boostmeup.com/blog/get-typewriter-text-effect-on-instagram-stories/)
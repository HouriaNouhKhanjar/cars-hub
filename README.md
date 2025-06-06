# Cars Hub

Welcome to Cars Hub – Your Trusted Car Enthusiast Platform

![Cars Hub Hompage Header](documentation/images/homepage-header.png)

Visit the deployed site: [Cars Hub](https://cars-enthusiast-platform-967e10cbb827.herokuapp.com/)

![GitHub last commit](https://img.shields.io/github/last-commit/HouriaNouhKhanjar/cars-hub) ![GitHub language count](https://img.shields.io/github/languages/count/HouriaNouhKhanjar/cars-hub) ![GitHub top language](https://img.shields.io/github/languages/top/HouriaNouhKhanjar/cars-hub)

---

## CONTENTS

- [Project Description](#project-description)
- [User Experience](#user-experience-ux)
  - [Bussiness Goal](#bussiness-goal)
  - [User Goal](#user-goal)
  - [Scope Plan](#scope-plan)
  - [User Stories](#user-stories)
- [Database Schema](#database-schema)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Wireframes](#wireframes)
  - [Features](#features)
  - [Accessibility](#accessibility)
- [Technologies Used](#technologies-used)
   - [Languages Used](#languages-used)
   - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Testing](#testing)
- [Deployment & Local Development](#deployment--local-development)
   - [Deployment](#deployment)
   - [Local Development](#local-development)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
- [Credits](#credits)
   - [Code Used](#code-used)
   - [Content](#content)
   - [Media](#media)
   - [Acknowledgments](#acknowledgments)

---

## Project Description

This project is a modern web application designed for car enthusiasts to showcase their personal car collections, engage with other users, and build a community around automotive passion. Each user can create a profile, upload their vehicles, add descriptions and images, while others can like and comment on these posts—similar to a social media platform but focused exclusively on cars.

---

## User Experience

### Bussiness Goal

1. **Build a Niche Car Enthusiast Platform:**  
   Create a unique social space dedicated specifically to car lovers—unlike general-purpose platforms.

2. **Grow a Passionate Community:**  
   Encourage user engagement, car sharing, and meaningful interaction to increase user retention and organic growth.

3. **Monetization Opportunities (Future):**
   - Promote partnerships with car brands, auto parts dealers, detailing services, etc.
   - Offer premium features like profile customization, more upload storage, or verified accounts.

### User Goal

1. **Showcase Personal Cars:**  
   Upload and display cars they own or admire with images, specs, and stories.

2. **Get Recognition and Feedback:**  
   Receive likes and comments from other users—satisfying social interaction and validation.

3. **Discover and Explore Other Cars:**  
   Browse through a variety of vehicles, learn about different models, and get inspired.

---

## Scope Plan

### **Feature Planning**

Below is a table of opportunities for the Cars Hub project, rated on **importance** and **viability** (1–5 scale). Features that score highest are considered part of the **MVP** and were prioritized in this release. Mid-level features are planned for future updates, while lower-priority features are candidates for future enhancement phases.

The system supports **three user roles**:

- **Guest Users**: Can view car listings and categories without an account.
- **Registered Users**: Can create and manage car posts, interact with the platform, and customize their profiles.
- **Admins**: Have full control over the platform's content and management capabilities through a customized admin panel using Jazzmin.

| User Type | Feature | Importance | Viability | MVP/Extra | Delivered |
| --------- | ---------------- | ---------- | ------ | ------- | ----- |
| All | View car listings on homepage | 5 | 5 | MVP | ✅ |
| All | Filter cars by category | 5 | 5 | MVP | ✅ |
| All | Search for cars | 5 | 5 | MVP | ✅ |
| Guest | Register account | 5 | 5 | MVP | ✅ |
| User | Login / Logout | 5 | 5 | MVP | ✅ |
| User | Profile management (update info, manage posted cars, view liked list) | 5 | 5 | MVP | ✅ |
| User | Post new car listings | 5 | 5 | MVP | ✅ |
| User | Like/Dislike car (AJAX) | 4 | 5 | MVP | ✅ |
| User | Comment on car (AJAX) | 4 | 5 | MVP | ✅ |
| User | Edit/Delete own comments/cars | 4 | 5 | MVP | ✅ |
| User | Drag and drop image upload | 4 | 5 | MVP | ✅ |
| User | Description editor with Summernote | 4 | 5 | MVP | ✅ |
| Admin | Manage car categories | 5 | 5 | MVP | ✅ |
| Admin | Approve/reject car posts before publishing | 5 | 5 | MVP | ✅ |
| Admin | Manage users' car listings | 5 | 5 | MVP | ✅ |
| Admin | Manage comments | 4 | 5 | MVP | ✅ |
| Admin | Manage About page content | 3 | 5 | MVP | ✅ |
| Admin | Read and manage user inquiries | 3 | 5 | MVP | ✅ |
| Admin | Access custom dashboard (Jazzmin) | 5 | 5 | MVP | ✅ |
| All | Error pages (400, 403, 404, 500) | 4 | 4 | MVP | ✅ |
| All | Toast Bootstrap notifications for server responses | 4 | 5 | MVP | ✅ |
| User | Loader during AJAX requests | 3 | 4 | MVP | ✅ |
| User | Confirm deletion using Bootstrap modals | 4 | 5 | MVP | ✅ |
| Dev | Manual and automated testing (views, forms) | 5 | 5 | MVP | ✅ |
| Dev | HTML, CSS, JS, Python code validation | 5 | 5 | MVP | ✅ |
| Dev | Lighthouse analysis with strong performance results | 5 | 5 | MVP | ✅ |
| Dev | Version control via GitHub | 5 | 5 | MVP | ✅ |
| Dev | Deployment via Heroku | 5 | 5 | MVP | ✅ |
| Dev | Cloudinary for image storage | 5 | 5 | MVP | ✅ |

#### **Planned for Future Releases**

| User Type | Feature| Importance | Viability | MVP/Extra | Delivered |
| --------- | ------ | ---------- | --------- | --------- | --------- |
| Guest | Sign in using social media (OAuth) | 3 | 4 | Extra | ❌ |
| User | Forgot password / password reset | 4 | 4 | Extra | ❌ |
| Dev | Optimize image upload size before saving | 3 | 4 | Extra | ❌ |
| Dev | Use Cloudflare for performance boost | 4 | 4 | Extra | ❌ |
| All | Integrate with Google Maps API | 3 | 4 | Extra | ❌ |

---

## **User Stories**

| User Story ID  | As a/an | I want to be able to.. | So that can... |
| :------------- | :------ | :--------------------- | :------------- |
| **VIEWING & NAVIGATION** | | | |
| 1 | Guest/User | View a list of available cars on the homepage | Browse car listings and explore what’s available |
| 2  | Guest/User | Filter cars by category (e.g., Van, Luxury, etc.) | Quickly narrow down listings to what suits my interests |
| 3| Guest/User | Search for a car by title, brand, or model  | Find a specific car I'm interested in |
| 4 | Guest/User | Click on a car to view detailed information | Learn more about the car’s features and specifications |
| 5 | Guest/User | View car images in the detail page | Visually assess the condition and style of the car |
| 6 | User | View comments and likes on cars | See what others think about a listing |
| **INTERACTION & ENGAGEMENT** | | | |
| 7 | User | Like or dislike a car (AJAX) | Express interest or feedback on a listing |
| 8 | User | Add a comment on a car (AJAX) | Share thoughts or ask questions directly on the listing |
| 9 | User | Delete or edit my comment | Correct or remove what I have written |
| 10 | User | See a list of cars I’ve liked | Review my favorites later |
| **REGISTRATION & USER ACCOUNTS** | | | |
| 11 | Guest | Register for an account | Post cars and interact with the platform |
| 12 | User | Log in and out | Access and secure my personal account |
| 13 | User | View and edit my profile | Update my information anytime |
| 14 | User | Manage my posted cars | Edit or remove listings I’ve created |
| 15 | Guest | Reset my password(future) | Regain access to my account if I forget my credentials |
| 16 | Guest | Sign in using social media(future) | Quickly register without filling in a full form |
| **ADMIN & SITE MANAGEMENT** | | | |
| 17 | Admin | Approve or reject car posts | Ensure only valid, quality listings are published |
| 18 | Admin | Manage car categories | Keep the list of car types organized and relevant |
| 19 | Admin | Manage all posted cars | Edit, delete, or deactivate inappropriate listings |
| 20 | Admin | Manage comments | Remove harmful or spam comments |
| 21 | Admin | View and manage inquiries from users | Respond to user questions and feedback |
| 22 | Admin | Edit content on the About page | Keep site information up to date |
| 23 | Admin | Access a customized dashboard | Efficiently manage the site from a central panel |
| **UI / UX FEATURES** | | | |
| 24 | All | See toast messages for server feedback | Instantly understand the success or failure of actions  |
| 25 | User | Confirm deletion actions with a modal | Avoid accidentally deleting content |
| 26 | User | See a loader during AJAX operations | Know that a background action is in progress |
| **TECHNICAL & PERFORMANCE** | | | |
| 27 | Developer  | Validate HTML, CSS, JS, and Python code | Ensure quality, readable, and bug-free code |
| 28 | Developer  | Write and run unit tests | Confirm that major functionalities behave as expected |
| 29 | Developer | Analyze site using Lighthouse | Track and improve performance metrics |
| 30 | Developer | Use GitHub for version control | Collaborate and manage code history efficiently |
| 31 | Developer  | Use Heroku for deployment | Host the application and make it publicly accessible |
| 32 | Developer | Use Cloudinary for image handling | Store and retrieve user-uploaded images efficiently |
| 33 | Developer  | Optimize images before saving (future) | Improve site speed and reduce storage usage |
| 34 | Developer | Integrate Google Maps (future) | Show Address locations on an interactive map |

---

## Database Schema

The database for Cars Hub is designed to efficiently manage car listings, user profiles, and interactions. It is implemented using Django's ORM, ensuring seamless integration with the rest of the application.

The following ERD was generated using Graphviz (see the code [ingraphvis.py](documentation/erd/graphvis.py)) and outlines the relationships between the core models in the project:
![Cars Hub ERD](documentation/images/erd.png)


---

## Design

### **Colour Scheme**
The colour theme for Cars Hub is inspired by a modern, minimal aesthetic that strikes a balance between energy perfect for an automotive focused platform. The palette was carefully selected to convey professionalism, enhance the user experience, and maintain visual harmony across the site.

- Primary Colour: Deep Red Brown (#a52727): This bold, attention grabbing color is used for key interface elements like buttons and calls to action, helping guide user focus.

- Secondary Colour: Eastern Blue (#29a5b3): A fresh and cool tone that complements the primary red, adding contrast and balance.

- Background Accent: Link Water (#e0e2f3): A soft blue grey shade used in subtle background areas to add depth without distraction.

- Light Base:  Soapstone (#fffbf8): Applied to headers, footers, and important text areas, this warm off-white ensures strong contrast and readability.

- Dark Base: Raisin Black (#212529): A rich dark tone used for the navigation bar, footer backgrounds, and dark-on-light text, creating a solid visual foundation.

*Text colors throughout the site are primarily black or white, chosen based on background color to maintain high contrast and optimal legibility.*

![Cars Hub Colour Scheme](documentation/images/color-scheme.png)

### **Typography**

All fonts used in the **Cars Hub** project are sourced from [Google Fonts](https://fonts.google.com/), ensuring fast loading and broad compatibility across browsers and devices.

```css
--primary-font: "Montserrat", sans-serif;
--secondary-font: "Overlock", sans-serif;
```

![Cars Hub Fonts](documentation/images/fonts.png)

**Montserrat** is the primary font and is used for body text, meta information, and comments. Its clean, modern design supports clear readability across all content areas.

**Overlock** is used for headings and key UI elements, adding a touch of character and contrast while maintaining overall visual harmony.

Both fonts are web-safe, responsive, and accessible tested for legibility at various sizes and color contrasts to support an inclusive user experience.

### **Imagery**

I used a high quality **hero background image** featuring a sleek red car. The image brings bold energy to the homepage and sets the tone for users as soon as they land on the site.

The image was sourced from [Pexels](https://www.pexels.com), a free and high resolution image library. I specifically chose a red vehicle to complement the site’s **primary red-brown color** and to maintain a cohesive look and feel between the branding and the interface.

![Hero Image](documentation/images/hero.webp)

### **Wireframes**

- Homepage
![Homepage Wireframe](documentation/images/homepage-wireframe.png)

- Car Detail
![Car Detail Wireframe](documentation/images/car-detail-wireframe.png)

- About
![About Wireframe](documentation/images/about-wireframe.png)

- Update Profile
![Update Profile Wireframe](documentation/images/profile-wireframe.png)

- User Cars List
![User Cars List Wireframe](documentation/images/user-cars-list-wireframe.png)

- User Add/Edit Car
![User Add/Edit Car Wireframe](documentation/images/add-edit-car-wireframe.png)

- User Likes List
![User Likes List Wireframe](documentation/images/likes-list-wireframe.png)

- Signup
![Signup Wireframe](documentation/images/signup-wireframe.png)

- Signin
![Signin Wireframe](documentation/images/signin-wireframe.png)

- Signout
![Signout Wireframe](documentation/images/signout-wireframe.png)

- Error Page
![Error Page Wireframe](documentation/images/error-wireframe.png)

### **Features**

The website is contains the following pages:  Homepage, Car detail, Signin, Signup, Signout, Profile, User cars list, User likes list, Admin dashboard.

All Pages on the website are responsive.

#### Base Template

All pages except the Admin dashboard inherit the content from base template, and it contains the follwing sections:

* Favicon - I used [Favicon.io](https://favicon.io/) to create the favicon for the site.

  ![Cars Hub Favicon](documentation/images/favicon.png)

* Logo - I used [Canva(https://www.canva.com/) to create the logo.
  ![Cars Hub Logo](documentation/images/cars-hub-logo.webp)

- **Navbar section:** contains the logo, Home link, About link, and a "Sign In" button that when clicked displays a dropdown with signin or signup choices.
  - On large screen and guest mode:
    
     ![Cars Hub Navbar on large screen and guest mode](documentation/images/navbar-large.png)
   
   - On large screen and authenticated user:
    
     ![Cars Hub Navbar on large screen and authenticated user](documentation/images/navbar-large-user.png)

   - On small screen and guest mode:

     ![Cars Hub Navbar on small screen and guest mode](documentation/images/navbar-mobile.png)
   
   - On small screen and authenticated user:
    
     ![Cars Hub Navbar on small screen and authenticated user](documentation/images/navbar-mobile-user.png)


- **Footer section:** displays the contact information and address on map.

   *In the future: If Cars Hub expands to include in-person services (like inspections, meetups, or a real-world showroom), the address sets the stage*

   - On large screen:
    
     ![Cars Hub Footer on large screen](documentation/images/footer-large.png)

   - On small screen:

     ![Cars Hub Footer on small screen](documentation/images/footer-mobile.png)

#### Homepage
This is the landing page of the website it contains the following sections:

- **Hero section:** contains the welcoming phrase and "Discover" button that when scrolles to cars list. 

  - On large screen:
    
     ![Cars Hub Hero on large screen](documentation/images/hero-large.png)

   - On small screen:

     ![Cars Hub Hero on small screen](documentation/images/hero-mobile.png)

- **Filter and search section:** contains the search area and categories filter. 

  - On large screen:
    
     ![Cars Hub Filter and Search on large screen](documentation/images/filters-large.png)

   - On small screen:

     ![Cars Hub Filter and Search on small screen](documentation/images/filters-mobile.png)

- **Cars list section:** contains the published cars, and below the pagination list. 

  - On large screen:
    
     ![Cars Hub Filter and Search on large screen](documentation/images/cars-list-large.png)

   - On small screen:

     ![Cars Hub Filter and Search on small screen](documentation/images/cars-list-mobile.png)

#### Car Detail
This page contains the following sections:

- **Car content section:** contains the car title, description, owner, created date, images slider and like button.
   - On large screen and guest mode:
    
     ![Cars Hub Car Detail on large screen and unauthenticated user](documentation/images/car-detail-large-guest.png)
   
   - On large screen and authenticated user:
    
     ![Cars Hub Car Detail on large screen and authenticated user](documentation/images/car-detail-large-user.png)

   - On small screen and guest mode:

     ![Cars Hub Car Detail on small screen and unauthenticated user](documentation/images/car-detail-mobile-guest.png)
   
   - On small screen and authenticated user:

     ![Cars Hub Car Detail on small screen and authenticated user](documentation/images/car-detail-mobile-user.png)

- **Comments section:** This area displays a comment box that includes the total number of comments and a list of existing comments on the left, with an "Add Comment" form on the right. If the logged-in user is the author of a comment, edit and delete icons appear next to their name, allowing them to manage their comment. The comments section is only visible to logged-in users, guests will not see it.
   - On large screen and guest mode:
    
     ![Cars Hub Comments on large screen and unauthenticated user](documentation/images/comment-large-guest.png)
   
   - On large screen and authenticated user:
    
     ![Cars Hub Comments on large screen and authenticated user](documentation/images/comment-large-user.png)

   - On small screen and guest mode:

     ![Cars Hub Comments on small screen and unauthenticated user](documentation/images/comment-mobile-guest.png)
   
   - On small screen and authenticated user:

     ![Cars Hub Comments on small screen and authenticated user](documentation/images/comment-mobile-user.png)

#### Profile Base Template
This template extends the Base Template, inheriting the shared navbar and footer. It features a two-column layout on larger screens:

The left section is a navigation panel where users can access their profile settings, their cars, and liked items.

The right section displays content based on the selected option.

On smaller screens (mobile view), the layout switches to a vertical stack. The navigation panel becomes a dropdown menu, ensuring a clean and user-friendly experience across all devices.

- On large screen:
    
   ![Cars Hub Profile Base Template on large screen](documentation/images/profile-base-large.png)

- On small screen:

   ![Cars Hub Profile Base Template on small screen](documentation/images/profile-base-mobile.png)

#### Profile
This page contains the profile update form:

- On large screen:
    
   ![Cars Hub Profile on large screen](documentation/images/profile-large.png)

- On small screen:

   ![Cars Hub Profile on small screen](documentation/images/profile-mobile.png)

#### User Cars List
This page contains the user cars list with the following sections:
- **Add new car section:** includes an "Add New Car" button, which redirects the user to the car creation form when clicked.

  - On large screen:
    
     ![Cars Hub Add New Car on large screen](documentation/images/add-new-car-large.png)

   - On small screen:

     ![Cars Hub Add New Car on small screen](documentation/images/add-new-car-mobile.png)

- **Filter and search section:** contains the search area and categories filter. 

  - On large screen:
    
     ![Cars Hub User Filter and Search on large screen](documentation/images/user-filters-large.png)

   - On small screen:

     ![Cars Hub User Filter and Search on small screen](documentation/images/user-filters-mobile.png)

- **User Cars List section:** displays a table of the user's cars, showing key details such as the title, one of the uploaded images, category, and actions including View, Update, and Delete.

   If a car has not yet been approved by an admin, it will display a message: "Needs Admin Approval" with a semi-transparent overlay on the row to indicate it's pending.
  - On large screen:
    
     ![Cars Hub User Cars List on large screen](documentation/images/user-carslist-large.gif)

   - On small screen:

     ![Cars Hub User Cars List on small screen](documentation/images/user-carslist-mobile.gif)

#### Adding New Car
This page contains the add car form, the user enter car information and cars images.
If the form fields are not filled out correctly, validation messages will appear directly beneath the relevant inputs, guiding the user to correct their entries.
After adding a new car, the user is redirected to the My Cars list page. A toast notification appears confirming the successful submission. The newly added car is displayed in the table but is not yet actived, it shows the message: "Need Admin Approval" with a visual overlay indicating its status.

- On large screen:
    
   ![Cars Hub Add New Car on large screen](documentation/images/add-car-large.png)

- After submiting:

   ![Cars Hub Add New Car after submiting](documentation/images/add-car-after-adding.png)

- On small screen:

   ![Cars Hub Add New Car on small screen](documentation/images/add-car-mobile.gif)


#### Editing a Car
This page contains the Edit Car form, pre-filled with the car's existing information and displaying its current images. The user can update the car details, modify images, and delete any unwanted image.

If any form fields are invalid or left incomplete, validation messages appear directly beneath the relevant inputs to guide the user in making corrections.

After successfully updating the car, the user is redirected to the My Cars list page, where a toast notification confirms the successful update.

- On large screen:
    
   ![Cars Hub Edit  Car on large screen](documentation/images/edit-car-large.gif)

- On small screen:

   ![Cars Hub Edit Car on small screen](documentation/images/edit-car-mobile.gif)

#### Deleting a Car
When the user clicks the Delete button, a confirmation modal appears to prevent accidental deletion. Upon confirming, a loading indicator is shown while the request is being processed. Once the car is successfully deleted:
- It is immediately removed from the table.

- A toast notification appears confirming the successful deletion.

- On large screen:
    
   ![Cars Hub Delete Car on large screen](documentation/images/delete-car-large.gif)

- On small screen:

   ![Cars Hub Delete Car on small screen](documentation/images/delete-car-mobile.png)

#### Likes List
This page displays a list of previously liked cars in a table format. The user can click on a car title to navigate directly to its detail page.

- On large screen:
    
   ![Cars Hub Likes List on large screen](documentation/images/likes-list-large.png)

- On small screen:

   ![Cars Hub Liskes List on small screen](documentation/images/likes-list-mobile.png)

#### About page 
The page contains the following sections:

- **About content**:
The About page displays content managed by the site admin. It provides information about the Cars Hub platform, its purpose, and any other details the admin chooses to share. This content is editable from the admin dashboard, allowing updates without code changes.
   - On large screen:
      
      ![Cars Hub About on large screen](documentation/images/about-large.gif)

   - On small screen:

      ![Cars Hub About on small screen](documentation/images/about-mobile.gif)

- **Inqiry Form**:
The Inquiry Form allows users to get in touch with the platform administrators. It typically includes fields like name, email, subject, and message. Upon submission, the form data is stored or sent via email (depending on implementation), and a toast notification confirms that the inquiry was successfully submitted.
   - On large screen:
      
      ![Cars Hub Inquiry on large screen](documentation/images/inquiry-large.png)

   - On small screen:

      ![Cars Hub Inquiry on small screen](documentation/images/inquiry-mobile.gif)


#### Sign in page 
The Sign In page allows registered users to log into their Cars Hub account. It includes fields for username and password, with form validation to ensure correct input. If the credentials are incorrect, an error message is displayed. After a successful login, the user is redirected to Homepage and the username appears on navbar with a toast notification confirming the action.

- On large screen:
    
   ![Cars Hub Sign in on large screen](documentation/images/signin-large.png)

- On small screen:

   ![Cars Hub Sign in on small screen](documentation/images/signin-mobile.png)

#### Sign up page 
The Sign Up page enables new users to create an account on Cars Hub. The form includes required fields like username, and password, with validation to ensure proper formatting and unique account creation. Once registered, the user is logged in automatically and redirected to Homepage and the username appears on navbar with a toast notification confirming the action.

- On large screen:
    
   ![Cars Hub Sign up on large screen](documentation/images/signup-large.png)

- On small screen:

   ![Cars Hub Sign up on small screen](documentation/images/signup-mobile.png)

#### Sign out page 
The Sign Out function securely logs the user out of their session. After logging out, the user is redirected to the home page with a toast notification confirming the action.

- On large screen:
    
   ![Cars Hub Sign out on large screen](documentation/images/signout-large.png)

- On small screen:

   ![Cars Hub Sign out on small screen](documentation/images/signout-mobile.png)

#### Error page 
The website includes custom error pages to handle and display user-friendly messages for common HTTP errors. These pages help maintain a consistent user experience and guide users when something goes wrong.

404 – Page Not Found:
Displayed when a user tries to access a page that doesn’t exist. It includes a friendly message and a button to return to the homepage.

403 – Forbidden:
Shown when a user tries to access a resource they don’t have permission to view. It includes a friendly message and a button to return to the homepage.

400 – Bad Request:
Triggered when the server cannot process the request due to invalid syntax or corrupted data. It includes a friendly message and a button to return to the homepage.

500 – Internal Server Error:
Appears when the server encounters an unexpected condition. It includes a friendly message and a button to return to the homepage.

- On large screen:
    
   ![Cars Hub Error on large screen](documentation/images/error-large.png)

- On small screen:

   ![Cars Hub Error on small screen](documentation/images/error-mobile.png)

#### Admin Dashboard

The **Admin Dashboard** is the central hub for managing the **Cars Hub** platform. It is built using Django's default admin interface, with extensive customizations powered by the **[Jazzmin](https://django-jazzmin.readthedocs.io/)** library to enhance both the aesthetics and functionality.

- **Customizable Interface:**
  Using **Jazzmin**, the dashboard has been tailored to provide a modern, user friendly experience. It includes a clean layout with easily navigable menus and color schemes that align with the overall design of the website.

- **Improved Navigation:**
  Jazzmin's navigation features offer a collapsible sidebar, helping admins quickly access key sections such as **User Management**, **Car Listings**, **Comments**, and **Inquiries and About Management**.

- **User Friendly Forms & Filters:**
  Admins can easily manage content with advanced search and filter options for **cars** and **users**. The forms are also enhanced with better styling and validation messages to make administrative tasks smoother.

- **Quick Access to Key Actions:**
  Common actions like approving cars, and handling inquiries are made more accessible and visible, reducing the time needed to perform daily tasks.

   - Admin has on Homepage navbar an additional link that take him to the admin panel:

      ![Cars Hub Admin Navbar Links](documentation/images/admin-navbar.png)

   - Admin has on admin panel header link that take him to the Homepage:

      ![Cars Hub Admin Actions](documentation/images/admin-actions.png)
   
   - Admin edits about content:

      ![Cars Hub Admin Edit About Content](documentation/images/admin-dashboard-about.png)
   
   - Admin views inquiries list and changes read field:

      ![Cars Hub Admin Inquiries](documentation/images/admin-dashboard-inquiries.png)
   
   - Admin views cars list and changes the approved field:

      ![Cars Hub Admin Cars](documentation/images/admin-dashboard-cars.png)
   
   - Admin adds/edits car:

      ![Cars Hub Admin Add/Edit Car](documentation/images/admin-edit-car.gif)
   
   - Admin footer contains copyright and a link to go back to the website:

      ![Cars Hub Admin Footer](documentation/images/admin-footer.png)

---

### Accessibility

I have been careful while coding to ensure the website is as user friendly and accessible as possible. This has been accomplished by:

* Using semantic HTML.
* Implementing a hover state on all buttons across the site, I made sure it is clear to the user when they are hovering over a button.
* Making sure there is adequate color contrast throughout the site to enhance readability and accessibility.
* Forms & Validation:
Form fields have clear labels and validation messages, which are read out by screen readers to help users understand and correct their input. Error messages appear clearly to guide the user in case of invalid form submissions.

![action button](documentation/images/accessibility-btn.png)
![navbar link](documentation/images/accessibility-navlinks.png)
![Card Title](documentation/images/accessibility-title.png)
![Signup Form](documentation/images/accessibility-signup-form.png)
![Inquiry Form](documentation/images/accessibility-inquiry-form.png)

- - - 

## Technologies Used

### Languages Used

HTML, CSS, Bootstrap, Javascript, Python

### Frameworks, Libraries & Programs Used

- [Balsamiq](https://balsamiq.com/) - Used to create wireframes.

- [Git](https://git-scm.com/) - For version control.

- [Github](https://github.com/) - To save and store the files for the website.

- [Google Fonts](https://fonts.google.com/) - To import the fonts used on the website.

- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - Version 0.41.0 - Used for authentication, registration & account management.

- [django_crispy_forms](https://pypi.org/project/django-crispy-forms/) - provides a tag and filter that lets you quickly render forms

- [gunicorn](https://pypi.org/project/gunicorn/) - a Python WSGI HTTP Server

- [pillow](https://pypi.org/project/Pillow/) - Python imaging library

- [dj_databsae_url](https://pypi.org/project/dj-database-url/) - allows us to utilise the DATABASE_URL variable

- [psycopg2](https://pypi.org/project/psycopg2/) - a postgres database adapter which allow us to connect with a postgres database

- [Jazzmin](https://django-jazzmin.readthedocs.io/) Custumizing Admin Dashboard

- [Google Developer Tools](https://developers.google.com/web/tools) - To troubleshoot and test features, solve issues with responsiveness and styling.

- [TinyPNG](https://tinypng.com/) To compress images

- [Birme](https://www.birme.net/) To resize images and convert to webp format.
- - -

## Testing

Please refer to [TESTING.md](/documentation/TESTING.md) file for all testing carried out.

- - -

## Deployment & Local Development

### Deployment

The **Cars Hub** project is deployed using **Heroku**. Follow the steps below for a successful deployment:

---
#### Create the Live Database

This project uses a **PostgreSQL** database, provided by [ElephantSQL](https://www.elephantsql.com/) (via Code Institute or you can make one manualy).

---

#### Heroku App Setup

1. Go to the [Heroku Dashboard](https://dashboard.heroku.com/) and click **New → Create new app**.
2. Choose a unique name, select your region, and click **Create app**.
3. In the app's **Settings** tab, add the following config var:

   * `DATABASE_URL` → your Postgres connection string

---

#### Prepare for Deployment (in IDE)

1. Install required packages:

   ```bash
   pip3 install dj_database_url==2.3.0 psycopg2 gunicorn
   ```

2. Add them to your `requirements.txt`:

   ```bash
   pip3 freeze > requirements.txt
   ```

3. Update `settings.py`:

   * Import:

     ```python
     import dj_database_url
     ```

   * Replace `DATABASES` with:

     ```python
     DATABASES = {
         'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
     }
     ```

4. Run migrations:

   ```bash
   python3 manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python3 manage.py createsuperuser
   ```
---

#### Static Files Setup with WhiteNoise

WhiteNoise serves static files in production.

1. Install:

   ```bash
   pip install whitenoise
   ```

2. Add to `MIDDLEWARE` (after SecurityMiddleware):

   ```python
   'whitenoise.middleware.WhiteNoiseMiddleware',
   ```

3. In `settings.py`, add:

   ```python
   STATIC_URL = '/static/'
   STATIC_ROOT = BASE_DIR / 'staticfiles'
   STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
   ```

4. Collect static files:

   ```bash
   python manage.py collectstatic
   ```
---

#### Media Uploads with Cloudinary

Cloudinary handles image/media storage.

1. Install:

   ```bash
   pip install cloudinary django-cloudinary-storage
   ```

2. Add to `INSTALLED_APPS`:

   ```python
   'cloudinary',
   'cloudinary_storage',
   ```

3. Add this Cloudinary config var in **Heroku Settings**:

   * `CLOUDINARY_URL`
---

#### Rich Text Editing with Summernote

**django-summernote** allows rich text fields in admin or forms.

1. Install:

   ```bash
   pip install django-summernote
   ```

2. Add to `INSTALLED_APPS`:

   ```python
   'django_summernote',
   ```

3. Include its URLs in your main `urls.py`:

   ```python
   path('summernote/', include('django_summernote.urls')),
   ```
---

#### Procfile and Runtime

1. Create a `Procfile` in your root directory:

   ```
   web: gunicorn your_project_name.wsgi:application
   ```

2. Create a `runtime.txt` specifying your Python version:

   ```
   python-3.12.8
   ```

---

#### Security Settings

1. Generate a secure secret key using [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/).

2. Add it to Heroku as `SECRET_KEY`.

   In `settings.py`:

   ```python
   SECRET_KEY = os.environ.get("SECRET_KEY")
   ```

3. Set allowed hosts:

   ```python
   ALLOWED_HOSTS = ['your-app-name.herokuapp.com', 'localhost']
   ```

---

#### Final Deployment Steps

1. Push changes to GitHub and go to the **Deploy tab** in Heroku.

2. Click the connect to GitHub button in the deployment method section.

3. Search for the projects repository and then click connect.

4. Click enable automatic deploys or deploy it manualy at the bottom of the page.

---

### Local Development

#### **How to Fork**

To fork the repository:

1. Log in (or sign up) to [GitHub](https://github.com).
2. Navigate to the repository for this project:
   [Cars Hub GitHub Repo](https://github.com/HouriaNouhKhanjar/cars-hub) 
3. Click the **Fork** button in the top-right corner of the page.
   This will create a copy of the repository under your GitHub account.

---

#### **How to Clone**

To clone the repository:

1. Log in to [GitHub](https://github.com).

2.  Go to the repository for this project, [Cars Hub GitHub Repo](https://github.com/HouriaNouhKhanjar/cars-hub).

3. Click the green **Code** button and choose to clone using:

   * **HTTPS**
   * **SSH**
   * **GitHub CLI**
     Then copy the provided URL.

4. Open your terminal or IDE and navigate to the directory where you want to clone the project.

5. Type the following command:

   ```bash
   git clone https://github.com/your-username/cars-hub.git
   ```

   Replace the URL above with your copied link.

6. Navigate into the cloned directory:

   ```bash
   cd cars-hub
   ```

---

#### **Set Up the Environment**

1. It's recommended to use a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

2. Install the required packages:

   ```bash
   pip3 install -r requirements.txt
   ```

3. Apply migrations to set up the database:

   ```bash
   python3 manage.py migrate
   ```

4. Create a superuser (optional for accessing the admin dashboard):

   ```bash
   python3 manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python3 manage.py runserver
   ```

6. Visit `http://127.0.0.1:8000/` in your browser to access the site locally.

---
## Credits

### Code Used

Throughout the development of **Cars Hub**, I referred to various official documentation and tools to implement specific features and improve user experience:

* **Authentication & Permissions**
  Used the [Django `LoginRequiredMixin`](https://docs.djangoproject.com/en/5.2/topics/auth/default/#the-loginrequired-mixin) to restrict access to authenticated users.

* **Many-to-Many Relationships**
  Implemented user likes using Django’s [`ManyToManyField`](https://docs.djangoproject.com/en/5.2/ref/models/fields/#django.db.models.ManyToManyField).

* **CSRF Protection in AJAX**
  Followed the [Django CSRF in AJAX guide](https://docs.djangoproject.com/en/5.2/ref/csrf/#ajax) to secure asynchronous requests.

* **Template Filters**
  Utilized built-in filters like `date` from the [Django template language reference](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/).

* **Custom Error Handling**
  Customized 404, 403, and 500 pages using [Django's error view documentation](https://docs.djangoproject.com/en/5.2/topics/http/views/#customizing-error-views).

* **Django Admin Customizations**

  * Injected custom JavaScript into the admin interface for a better user experience using [this guide](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#adding-custom-javascript).
  * Added an inline image upload form within the car model using [inline model administration](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#working-with-inline-models).

* **JavaScript & Fetch API**

  * Sent and handled AJAX requests via the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).
  * Implemented smooth navigation using [`scrollIntoView`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView).

* **UI Components with Bootstrap**

  * Added toast notifications for feedback using [Bootstrap Toasts](https://getbootstrap.com/docs/5.3/components/toasts/).
  * Implemented confirmation dialogs using [Bootstrap Modals](https://getbootstrap.com/docs/5.3/components/modal/).

* **Admin Dashboard Styling**

  Customized the admin interface with the [**Jazzmin**](https://github.com/farridav/django-jazzmin) template.

* **UI Animations**

  Used [Animate.css](https://animate.style/) for smooth button and text animations.

### Content
- **Car Samples (Text, Images, and Categories)**

   Some car-related content, including sample text, images, and categories, was sourced from [**cars.com**](https://www.cars.com/) for demonstration and testing purposes.

-  **Site Descriptions & Instructions**

   All descriptive content across the site including welcome messages, user guidance, and instructional text was written by me.

### Media

* The main images used on the Start page and About page were sourced from [**Pexels**](https://www.pexels.com), a free stock photo platform.

### Acknowledgments

I would like to sincerely thank the following individuals and organizations for their support throughout the development of this project:

- **My Family** — For their patience, encouragement, and unwavering support during the countless hours spent building this application.

- [**Jubril Akolade**](https://github.com/Jubrillionaire) — My Code Institute mentor, whose guidance and constructive feedback helped me stay focused and improve the quality of my work.

- [**Code Institute**](https://codeinstitute.net/de/) — For providing a comprehensive and well structured curriculum that equipped me with the skills needed to complete this project confidently.

# Djitter

This project **follows** a 4-part tutorial by [Real Python](https://realpython.com/) to build a social network with Django.

## Tutorial Outline

**(Copied from the tutorial as is)**

For this project, you’ll implement the connections between users of your social network following a couple of assumptions that expand on the two cornerstones mentioned above:

- Your users will be able to either follow or not follow another user.
- If they follow someone, they’ll see that user’s content. If they don’t, they won’t.
- Your users can follow a person without being followed back. Relationships in your social network can be asymmetrical, meaning that a user can follow someone and see their content without the reverse being true.
- Your users need to be aware of who exists so that they know whom they can follow.
- Users should also be aware of who follows them.
- In your app’s most basic form, users won’t have many extra features available to them. You won’t implement a way to block people, and there won’t be a way to directly respond to content that someone else posted.

### Part 1 - [Build a Social Network With Django](https://realpython.com/django-social-network-1/)

In the first part of this tutorial series, you’ll learn how to:

- Implement one-to-one and many-to-many relationships between Django models
- Extend the Django user model with a custom Profile model
- Customize the Django admin interface

Project overview:

- Step 1	[Set Up the Base Project](https://realpython.com/django-social-network-1/#step-1-set-up-the-base-project)
- Step 2	[Extend the Django User Model](https://realpython.com/django-social-network-1/#step-2-extend-the-django-user-model)
- Step 3	[Implement a Post-Save Hook](https://realpython.com/django-social-network-1/#step-3-implement-a-post-save-hook)

### Part 2 - [Build a Django Front End With Bulma](https://realpython.com/django-social-front-end-2/)

In the second part of this tutorial series, you’ll learn how to:

- Integrate Bulma CSS and style your app
- Use template inheritance to reduce repetition
- Structure Django templates in a folder hierarchy
- Build routing and view functions
- Interlink pages of your app using dynamic URLs

Project overview:

- Step 4	[Create a Base Template With Bulma](https://realpython.com/django-social-front-end-2/#step-4-create-a-base-template-with-bulma)
- Step 5	[List All User Profiles](https://realpython.com/django-social-front-end-2/#step-5-list-all-user-profiles-on-the-front-end-of-your-django-app)
- Step 6	[Access Individual Profile Pages](https://realpython.com/django-social-front-end-2/#step-6-access-individual-profile-pages)

### Part 3 - [Build and Handle POST Requests in Django](https://realpython.com/django-social-post-3/)

In the third part of this tutorial series, you’ll learn how to:

- Create the front-end interface to let users follow and unfollow profiles
- Submit and handle a POST request in Django using buttons
- Set up the model for your text-based content
- Build styled templates to display content on the front end
- Use intricate model relationships in template code

Project overview:

- Step 7	[Follow and Unfollow Other Profiles](https://realpython.com/django-social-post-3/#step-7-follow-and-unfollow-other-profiles)
- Step 8	[Create the Back-End Logic For Dweets](https://realpython.com/django-social-post-3/#step-8-create-the-back-end-logic-for-dweets)
- Step 9	[Display Dweets on the Front End](https://realpython.com/django-social-post-3/#step-9-display-dweets-on-the-front-end)

### Part 4 - [Build and Submit HTML Forms With Django](https://realpython.com/django-social-forms-4/)

In the fourth part of this tutorial series, you’ll learn how to:

- Create and render Django forms from your Dweet model
- Prevent double submissions and display helpful error messages
- Interlink pages of your app using dynamic URLs
- Refactor a view function
- Use QuerySet field lookups to filter your data on the back end

Project overview:

- Step 10	[Submit Dweets Through a Django Form](https://realpython.com/django-social-forms-4/#step-10-submit-dweets-using-django-forms)
- Step 11	[Prevent Double Submissions and Handle Errors](https://realpython.com/django-social-forms-4/#step-11-prevent-double-submissions-and-handle-errors)
- Step 12	[Improve the Front-End User Experience](https://realpython.com/django-social-forms-4/#step-12-improve-the-front-end-user-experience)

### Next Steps

If you’ve already created a portfolio site, add your project there to [showcase your work](https://realpython.com/get-started-with-django-1/#showcase-your-projects). You can keep improving your Django social network to add functionality and make it even more impressive.

Here are some ideas to take your project to the next level:

- **Implement User Authentication:** Allow new users to sign up through the front end of your web app by following the steps outlined in [Get Started With Django Part 2: Django User Management](https://realpython.com/django-user-management/).
- **Deploy Your Djitter Project:** Put your web app online for the whole world to see by [hosting your Django project on Heroku](https://realpython.com/django-hosting-on-heroku/).
- **Get Social:** Invite your friends to join your Django social network, and start djeeting your thoughts to one another.

# CRUD Simulation for Summer Skilling

Or known as the **Web App Simulation Under One Page | CRUD Session.**

## Introduction

Hello! This is a repository that features ***CRUD functionalities*** in Django. With the process, all done in one page! Means, multiple forms were spawn in modals from which the data has to be filled. With export feature as well. This repository consisting of Class-Based Views and Slight Manipulation on Code. Also, this repository has some parts / components used from the [****SmartClassroomSystem Repository****](https://github.com/CodexLink/SmartClassroomSystem). You could check that if you're interested on what parts I used on that repository.

## So, What's the difference between your work and other works?

I usually can't tell. But I think it is all about implementation that make things different here. But in my case, I used a method that avoids transitioning to another page to do the process. I want to do the processes in the same page. This means, I'm using only one page along with modals that generates form inside on it within different instances. Which then means, different intentions.

## Installation

Just to make things clear, there will be a lot of dependencies here! Not just the python modules but there are some executables needed as well!

### Preparation

1. Do the git clone! Or, you can fork the repository as well!

```text
For Clone: https://github.com/cpe-tipqc-community/django-crud-webapp-CodexLink.git
For Fork: Just press the fork button of the repository...
```

2. Open the Root of the Repository Folder in your favorite IDE.
   - If for instance, your IDE doesn't have an integrated terminal. Open a command prompt or any other CMD that favors you (such as [Cmder](https://cmder.net/)). And change directory towards the root of the repository.

### Dependencies

3. Assuming that you have Django Installed already. You still have to do `pip install -r requirements.txt` from the root of the repository. This installs the following:

```text
- Django (Update If Possible Only To 3.0.4)
- WeasyPrint
- django-extensions
```

Please report any further if I missed some dependencies as `pipreqs` weren't updating all required dependencies.

After installing dependencies, we're going to the much more complicated stuff. But first, we have to install the ***WeasyPrint Dependencies***.

### WeasyPrint Dependencies

Not going any further to complicate stuff. But you have to follow the instructions on their [website](https://weasyprint.readthedocs.io/en/stable/install.html#windows). It would take you for at least 10 minutes minimum or 30 minutes maximum to set things up.

#### "Why would you install something like this?"

It is the only library that could properly render a context with CSS support. And much easy implementation. Both for FBV and CCBV.

After all of that (assuming you have tested targetting their site to generate a PDF at]), we should be going to the ****database**** part.

### Database

The project is currently using `MySQL`. With that, we know that Django doesn't create the tables for you. (That occurs to me...). So you have to create one and name it with `smcrud_db`. Refer to the [settings.py](https://github.com/cpe-tipqc-community/django-crud-webapp-CodexLink/blob/master/CrudSpeedrun/settings.py#L81) for more information about the database settings.

### Preparation Literal

Since you have been able to get this far, it's time to set things the project itself, literally.

1. On the root of the repository, we have apply our models in the database. With that, type `python manage.py makemigrations`.
2. Once done, type `python manage.py migrate` to apply all migrations that the Django did.
3. After that, setup up your superuser! Type `python manage.py createsuperuser` to fill the information needed. (I will talk about how the master should be creating his / her / their account through command line later, see second bullet of FAQ below!)
4. Then, run `python manage.py runserver` and navigate to `localhost:8000/login` to get started~!
5. For additionals, if you want other users to register, navigate to `localhost:8000/register`!
6. ??? Profit... (You're done!)

## Frequently Asked Questions

- **Why are you doing it in Class-Based Views?**
  - Two words. ***Minimal***. ***Configuration***. The thing with class-based views is that, you could do basic work without **repeating** your self. Why create another one when they already provided it to you? Though even with customizations, they're quite possible unless complex conditions has to be done. Basically you have to `Base_____View` to do your intended outcomes with `Mixins` or else get the provided once.

- **Why would the master should register through Command Line instead in the website?**
  - The reason is, I haven't set things up properly. Meaning I haven't implemented the smart `is_user_superuser?` functionality. Since the focus here is the essentiality of the CRUD functionalities. I left that as is. Users who register through the website doesn't have any access to the Django-administration. Which is why, Master person have to start in the command line as he/she/them setup the project.

- **So, what are the expected things that I could learn from this repo?**
  - How you should be well organized from how constructed the content you're trying to generate.
  - How formality(In General) should be one of the priorities when in development. (See Forms File and Django Administration to know what I'm trying to talk about.)
  - How Implementation gives you the ability to debug with ease.
  - How Separating DataSets will help you to do your work by already adapting to DRY principles.
  - I guess there's nothing else. Inspect further for unforeseen learnings.

- **Why you do have so many dependencies?**
  - Module / Library Usage.

- **Why there's no user forgotten password feature!?**
  - Technically, not really part of the objective. I'm quite done going any further as I don't know what would be the next move after this requirement submission. You could implement it if you want. Or I may soon if I get the hands of this repository (forked).

- **Why are you making this README longer?**
  - Not because I have to. I did this because I want to.

- **What CSS Framework are you currently using?**
  - The CSS framework that I'm currently using is [Djibe's Material Design 2](https://github.com/djibe/material) Forked from [Daemonite's Material Design](https://github.com/Daemonite/material) Repository. Please go to [Djibe's Material Design 2](https://github.com/djibe/material) on how to construct CSS and JS files as the repo is in the state of soft-development. Meaning the Releases are not quite as would you expect. You have to do it on your own. (*Spoiler Alert: It requires NPM*)

- **Can I use this for personal / non-profit / profit use?**
  - Sure thing! This repository is under [MIT License](https://github.com/cpe-tipqc-community/django-crud-webapp-CodexLink/blob/master/LICENSE). Please check the file for more information.

## Credits

- [djibe](https://github.com/djibe) for Daemonite's Material Design Component Support
- [Django Class-Based View Inspector](https://ccbv.co.uk/) for inspecting inheritance by acknowledging premade class variables and available functions.
- [Django-Extensions](https://github.com/django-extensions/django-extensions) for expanding the ability to do more by easing process of particular technical tasks.
- To someone that is non-existent who motivates me enough for the cause.

## License

This repository is currently licensed in MIT License. Please see the [LICENSE](https://github.com/cpe-tipqc-community/django-crud-webapp-CodexLink/blob/master/LICENSE) File in the Repository for more information.

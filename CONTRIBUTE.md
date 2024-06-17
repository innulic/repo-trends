# Contributing to Our Python Project

🌟 First off, thank you for considering contributing to our project! 🌟

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer


## We Develop with GitHub

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

Pull requests are the best way to propose changes to the codebase. We actively welcome your pull requests:

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

# Report bugs using Github's [issues](https://github.com/innulic/repo-trends/issues)

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/innulic/repo-trends/issues/new); it's that easy!

## Write bug reports with detail, background, and sample code

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can.
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

People *love* thorough bug reports. I'm not even kidding.

## Required Tools for Development

Before you start contributing to our Python project, you will need a few tools installed on your machine:

### Git

Git is essential for version control and managing changes to the project.
Open Terminal application on your MAC and check is Git installed, but running this command
```bash
git --version
```
 If you don't have Git installed, you can download it from [git-scm.com](https://git-scm.com/). After installation, you can verify its installation by opening a terminal again and running the same command as above. It should display version of git. For example:
 ```bash
git version 2.39.3 (Apple Git-146)
 ```

You can use any IDE (or use notepad :), if you like), but during development we used Visual Studio Code

### Visual Studio Code
Visual Studio Code (VS Code) is a highly recommended Integrated Development Environment (IDE) for this project. It's lightweight, powerful, and supports a wide range of programming languages and file formats out of the box. Additionally, it offers a vast marketplace of extensions to enhance its functionality further, particularly for Python development.

#### Installing VS Code

To install VS Code, visit the [official download page](https://code.visualstudio.com/Download) and choose the version that matches your operating system. Follow the installation instructions provided on the website.

#### Recommended Extensions for Python Development

Once VS Code is installed, we recommend installing the following extensions to aid your Python development:

- **Python** (by Microsoft): This extension provides rich support for the Python language, including features such as IntelliSense, linting, debugging, and code navigation.

  To install, open VS Code, go to the Extensions view by clicking on the square icon on the sidebar or pressing `Cmd+Shift+X`, then search for "Python" and click **Install**.

- **Pylance**: Pylance supercharges your Python IntelliSense experience with fast, feature-rich language support derived from Pyright.

  Install it the same way you installed the Python extension, by searching for "Pylance" in the Extensions view.

- **GitLens**: Although optional, GitLens is an immensely useful extension that enhances the built-in Git capabilities of VS Code. It helps you visualize code authorship at a glance, navigate and explore the history of your project, and much more.

  Install GitLens from the Extensions view by searching for "GitLens" and clicking **Install**.

#### Setting Up Your Workspace

After installing VS Code and the recommended extensions, you can set up your workspace by cloning the project repository. 

1. Download project codebase
Open a terminal and run:

```bash
git clone https://github.com/innulic/repo-trends.git
```

2. Create new branch to start working on new task

```bash
git checkout -b user/{YOUR_NICK_NAME}/{SOME_MEANINGFULL_NAME_OF_THE_ISSUE}
```
Replace {YOUR_NICK_NAME} and {SOME_MEANINGFULL_NAME_OF_THE_ISSUE} with your values.

3. Try to run script that should setup your PC and run the app locally:
```bash
./run/local-run.sh
```
At the end you should see smth like this output to make sure that everything was setup successfully
```bash
[notice] A new release of pip is available: 23.0.1 -> 24.0
[notice] To update, run: pip install --upgrade pip
 * Serving Flask app 'index'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
You can also open this adress in your browser `http://127.0.0.1:5000`and should be able to see the website locally
![Local Setup ScreenShot](images/Screenshot%202024-06-17%20at%2019.33.41.png)
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/navchetna/composable-ui">
    <img src="public/github.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Composable UI</h3>

  <p align="center">
    This project aims to simplify the process of creating a frontend. Using the components in this repository, you can quickly create a frontend that is modular and customisable.
    <br />
    <a href="https://github.com/navchetna/composable-ui"><strong>Explore the docs »</strong></a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li>
          <a href="#prerequisites">Prerequisites</a>
        </li>
        <ul>
        <li>
          <a href="#prerequisites">WSL</a>
        </li>
        <li>
          <a href="#prerequisites">nvm and Node.js</a>
        </li>
        <li>
          <a href="#prerequisites">Python</a>
        </li>
        <li>
          <a href="#prerequisites">Git</a>
        </li>
        </ul>
        <li><a href="#cloning-the-project">Cloning the Project</a></li>
        <li><a href="#running-the-project">Running the Project</a></li>
        <ul>
        <li><a href="#cloning-the-project">a. Running via Docker Compose (Recommended)</a></li>
        <li><a href="#cloning-the-project">b. Running the backend</a></li>
        <li><a href="#cloning-the-project">c. Running the frontend</a></li>
        </ul>
        </ul>
      </ul>
      </ul>
    </li>
    <li>
    <a href="#component-usage">Component Usage</a>
    <ul>
        <li><a href="#navbar">Navbar</a></li>
        <ul>
            <li><a href="#navbar-props">Navbar Props</a></li>
        </ul>
        <li><a href="#sidebar">Sidebar</a>
        <ul>
            <li><a href="#sidebar-props">Sidebar Props</a></li>
        </ul>
        </li>
        <li><a href="#forms">Forms</a>
        </li>
        <li><a href="#videoplayer">VideoPlayer</a>
        <ul>
            <li><a href="#videoplayer-props">VideoPlayer Props</a></li>
        </ul>
        </li>
        <li><a href="#tables">Tables (Under development)</a>
        <ul>
            <li><a href="#videoplayer-props">VideoPlayer Props</a></li>
        </ul>
        </li>
        <li><a href="#layouts">Layouts</a></li>
      </ul>
    </li>
    <li><a href="#fastapi-server">FastAPI Server</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

### Built With

- [![React][React.js]][React-url]
- [![MySQL][MySQL]][MySQL-url]
- [![Prisma][Prisma]][Prisma-url]
- [![FastAPI][FastAPI]][FastAPI-url]
- [![Ant Design][Ant Design]][AntDesign-url]
- [![TailwindCSS][TailwindCSS]][TailwindCSS-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

Here are some steps to get started with this project

### Prerequisites

1. Install WSL on Windows machine

   - Open PowerShell or Windows Command Prompt in administrator mode by right-clicking and selecting "Run as administrator" and then enter
     ```
     wsl --install
     ```
   - Then restart your machine
   - Open PowerShell again and enter
     ```
     wsl
     ```
     This will open wsl on your terminal. It is recommended that all your code must be written within wsl.

1. Node.js 20.13.1+ (Long Term Support version) + npm (installed along with Node.js)
   - Install Node Version Manager (nvm)
     ```bash
     curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
     ```
   - Install Node.js (Long Term Support Version) using nvm
     ```bash
     nvm install --lts
     ```
   - Check Node.js version
     ```
     node -v
     ```
     Should display `v20.11.1` or greater
1. Python 3.9+ (Installed by default in wsl)
1. Git (Installed by default in wsl)

   NOTE: If you are new to Git, create an access token and use it when prompted for password

### Cloning the Project

1. Clone the repo
   ```bash
   git clone https://github.com/navchetna/composable-ui.git
   ```
2. Move into project directory
   ```bash
   cd composable-ui
   ```

### Running the project

#### a. Running via Docker Compose (Recommended)

1. Build the image (Approx 5 min)
   ```bash
   docker compose build
   ```
2. Bring up the containers (Approx 5 min)
   ```bash
   docker compose up
   ```

By default

- frontend is accessible at `http://localhost:3000`
- backend is accessible at `http://localhost:3010`
- SwaggerUI is accessible at `http://localhost:3010/docs`

#### b. Running backend locally

1. Navigate to `/server`
   ```
   cd server
   ```
2. Install python libraries packages

   ```bash
   pip install fastapi uvicorn
   ```

   Installs both FastAPI and Uvicorn

3. Bring up the server
   ```bash
   uvicorn main:app --reload
   ```

- by default, backend is accessible at `http://localhost:3010` and SwaggerUI is accessible at `http://localhost:3010/docs`
- `main` corresponds to the name of the file `main.py`

- `app` corresponds to the name of the variable used to initialise FastAPI `app = FastAPI()`.

- `--reload` is used to watch for changes in the `main.py` file, upon which the server automatically restarts, thus incorporating the new changes

  <!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

#### c. Running frontend locally

1. in the root directory, i.e, `/composable-ui`, install required dependecies

   ```bash
   npm install
   ```

   Installs all dependencies for the project like Ant Design Library, Icon packs, etc.

2. Run the project
   ```
   npm run dev
   ```
   By default, frontend is accessible at `http://localhost:3000`

<!-- USAGE EXAMPLES -->

## Component Usage

In this section, you will understand how to use each of the components in the `src/components` folder. This example shows how to add all components into the `App.jsx` file in the `src` folder.

If you wish to use it in different files, adjust the imports accordingly

### Navbar

Add this to the top of your file:

```js
import Navbar from "./components/Navbar";
```

Use the Navbar Component as below:

```js
return (
  <>
    <Navbar
      navigationItems={NavItemsConfig.navigationItems}
      menuItems={NavItemsConfig.menuItems}
      logoPath={NavItemsConfig.logoPath}
    />
  </>
);
```

#### Navbar Props

Props are short for properties and these are the parameters you pass into the child component (Navbar.jsx) in the parent component (App.jsx)

All these props can be configured in a seperate config file present in `/src/config/NavItemsCOnfig.jsx`

The props for these include:

- `navigationItems` - Define the Tabs present in the Navbar
- `menuItems` - Define the dropdown items that appear when the Menu Bar (by default Cog Icon) is clicked.
- `logoPath` - Define the Url or Path of the image to be used as logo

### Sidebar

Add this to the top of your file:

```js
import Sidebar from "./components/Sidebar";
```

Use the Sidebar Component as below:

```js
return (
  <>
    <Sidebar sidebarItems={SidebarItemsConfig.sidebarItems} />
  </>
);
```

#### Sidebar Props

Props are short for properties and these are the parameters you pass into the child component (Sidebar.jsx) in the parent component (App.jsx)

All these props can be configured in a seperate config file present in `/src/config/SidebarItemsConfig.jsx`

The props for these include:

- `sidebarItems` - Define the Elements present in the Sidebar along with links to their respective pages

### Forms

Add this to the top of your file:

```js
import FormLayout from "./components/Forms/FormLayout";
```

Use the Form Component as below:

```js
return (
  <>
    <FormLayout />
  </>
);
```

NOTE: `<FormLayout/>` component houses many such child components like Radio Buttons, Dropdowns, Input Boxes etc. To see examples of their usage, check out `/src/components/Forms/FormLayout.jsx`

### VideoPlayer

Add this to the top of your file:

```js
import VideoPlayer from "./components/VideoPlayer";
```

Use the VideoPlayer Component as below:

```js
return (
  <>
    <VideoPlayer videoURL={"https://www.youtube.com/watch?v=Tk5bqlb5F4M"} />
  </>
);
```

#### VideoPlayer Props

Props are short for properties and these are the parameters you pass into the child component (VideoPlayer.jsx) in the parent component (App.jsx)

For this component, since there is only one prop that contains the link to the video, it can be directly passed as shown in the example above

The prop is:

- `videoUrl` - Pass the URL of the video that you want to be displayed

### Tables

(Under developement)

Add this to the top of your file:

```js
import TableBasic from "./components/Tables/TableBasic";
```

Use the TableBasic Component as below:

```js
return (
  <>
    <TableBasic />
  </>
);
```

### Layouts

Layouts are example configurations made using a combination of all the components listed above. They are designed in such a way that you can just place then in your main file (by default App.jsx) and start using them.

To use an example layout, import that layout in your main file as such:

```js
import Layout1 from "./layouts/Layout1";
```

Then use it as below:

```js
return (
  <>
    <Layout1 />
  </>
);
```

All the props for the child components of the layout can be managed inside the layout component.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- #### Sidebar Props

Props are short for properties and these are the parameters you pass into the child component (VideoPlayer.jsx) in the parent component (App.jsx)

For this component, since there is only one prop that contains the link to the video, it can be directly passed as shown in the example above

The prop is:

- `videoUrl` - Pass the URL of the video that you want to be displayed -->

<!-- ROADMAP -->

<!-- ## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
  - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- CONTRIBUTING -->
<!--
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

<!-- ## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

CONTACT -->

<!-- ## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- ACKNOWLEDGMENTS -->

<!-- ## Acknowledgments

- []()
- []()
- []()

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/navchetna/composable-ui/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[FastAPI]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Prisma]: https://img.shields.io/badge/Prisma-3982CE?style=for-the-badge&logo=Prisma&logoColor=white
[Prisma-url]: https://prisma.io/
[MySQL]: https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white
[MySQL-url]: https://mysql.com/
[Ant Design]: https://img.shields.io/badge/-AntDesign-%230170FE?style=for-the-badge&logo=ant-design&logoColor=white
[AntDesign-url]: https://ant.design/
[TailwindCSS]: https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white
[TailwindCSS-url]: https://tailwindcss.com/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com

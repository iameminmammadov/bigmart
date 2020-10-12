<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Bigmart Project</h3>
</p>

## Table of Contents

* [About the Project](#about-the-project)
  * [Built using](#built-using)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project

This project has been created as part of my contract work with Lighthouse Labs: Canada's 
Leading Coding Bootcamp. As the instructor and mentor for the data science bootcamp, I 
was tasked with developing a project that will combine several concepts taught. This project
includes:
* Analysis of the [BigMart sales data] (https://www.kaggle.com/brijbhushannanda1979/bigmart-sales-data)
* Writing a production-ready pipeline with the focus on object-oriented programming
* Developing an API using Flask-RESTful
* Writing tests for both the pipeline and API
* Configuring S3 and using it for storage of dataset and trained models
* Engineering CI/CD pipeline using CircleCI and writing shell scripts to automate the steps

This project includes two branches:
* `analysis` shows the initial analysis of the dataset
* `main` shows the engineering work. Please note, that while this branch is based on the `analysis`, I
added the parameters hypertuning for several models as part of the pipeline.


### Built With
Here the tools that you will learn (I will teach you) in order to understand how this project works:
* [Python](https://www.python.org/downloads/)
* [CircleCI](https://circleci.com/)
* [AWS](https://aws.amazon.com/)
* [Tox](https://tox.readthedocs.io/en/latest/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Gemfury] (https://gemfury.com/)



<!-- GETTING STARTED -->
## Getting Started

While all of the things are (or will be) discussed during the lectures, here are couple of things
you need to do to be able to run this project:
* Create a clean virtual environment and install packages that are in requirements.txt
* Create a profile at AWS and configure the Access Keys
* Add Access Keys to your environmental variables in CircleCI
* Do the same with Kaggle Key and Kaggle Username
* Do the same with Gemfury upload URL

### Prerequisites

Once you get everything installed, fork this project and run
```sh
python setup.py install --force
```
from the folder of `datacube_bigmart`.

After that, the point of this project is for you to play/test it and see how things that we have
learnt fit in together.

<!-- CONTRIBUTING -->
## Contributing

While this project has been created with the certain goal in mind, anyone from LightHouse Labs or anyone else can cantribute. Any contributions you make are **greatly appreciated** and will be **reviewed**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/Innovation`)
3. Commit your Changes (`git commit -m 'Add some Innovating feature that Emin didn't do'`)
4. Push to the Branch (`git push origin feature/Innovation`)
5. Open a Pull Request

After that, I will review it and either merge, or comment back. 

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Your Name - [@LinkedIn](https://www.linkedin.com/in/emin-mammadov/) - emin.e.mammadov@gmail.com

Project Link: [https://github.com/iameminmammadov/bigmart](https://github.com/iameminmammadov/bigmart)
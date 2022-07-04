<div id="top"></div>

<h3 align="center">Fund View</h3>

  <p align="center">
    <a href="https://github.com/samlangley1/Fund-View/issues">Report Bug</a>
    ·
    <a href="https://github.com/samlangley1/Fund-View/issues">Request Feature</a>
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About Fund View

Fund View was designed to make it easier to track stocks against the most important metrics for investment. It's an incredibly simple fetch and display application that can be up and running in seconds.

![Fund View](https://imgur.com/JJjCWJA)



### Built With

* [Python]

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

Simple:

- Clone the repository to your local machine
- Open backend/params.py and enter your yahoo finance API key
- From the root directory, run 'python main.py' (python command may differ depending on version)
- See results!



Docker:

- Clone the repository to a local directory
- Open backend/params.py and enter your yahoo finance API key
- From the root directory, run the command 'sudo docker build -t fund-view .'
- Run the command 'sudo docker run fund-view'

### Prerequisites

## Installs
- Python >=3
- docker

## General
- A Yahoo finance API key

### Installation

1. Get a free API Key at [https://www.yahoofinanceapi.com/](https://www.yahoofinanceapi.com/)
2. Clone the repo
   ```sh
   git clone https://github.com/samlangley1/Fund-View.git
   ```
3. Enter your API key in `params.py`
   ```Python
   api_key = 'ENTER YOUR API KEY'
   ```
4. Run 'python main.py'
5. Profit!

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- DATA-->
## DATA

To request custom stocks, simply add a symbol to the list in /data/syock_symbols.py 

<!-- ROADMAP -->
## Roadmap

- [Request Limits] API request limits are coming in the near future
- [Frontend] A frontend is planned in the future, but not currently in progress
- [Custom conditions] I am adding the ability to create custom conditions to be alerted on (e.g below a specified EPS)

See the [open issues](https://github.com/samlangley1/Fund-View) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

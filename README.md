# BiciMAD and BiciPARK Stations <-> Religious temples of Madrid

<p align="left"><img src="https://i.postimg.cc/ydd0SSPF/8-h-ZMK5i-M1wf-Jo9-Vc.png"></p>

## **Status:**

Ironhack Madrid - Data Analytics Part Time - Sep 2023 - Project Module 1

## **My Project:**

In this project we need to generate 2 CSV file with the nearest BiciMAD Station and BiciPark Station to a Place of interest of Madrid. In __my project__, I need to show the nearest BiciMAD or BiciPark Station to some temples located in Madrid.

If inputed by the user, the programm must show the nearest Bicipark and Bicimad Station to the requested temple

## **DDBB:**

- **CSV Files.** The datasets contains information from the BiciMAD stations including their location (i.e.: latitude / longitude). You may find the `.csv` files in the __data__ folder.

- bicipark_stations.csv
- bicimad_stations.csv

- **API REST.** We will use the API REST from the [Portal de datos abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json#/), where you can find the data:

- base_url = "https://datos.madrid.es/egob"
- body = "/catalogo/209434-0-templos-otros.json"
- response = re.get(base_url + body)

## **Technology stack:**

- pandas as pd
- Requests
- json
- argpars
- geopy

- Language: pyhon3
- Tools: Jupyter Notebook and Visual Studio Code

## **Folder Structure**

└── __h_datamadpt0923_project_m1__

    ├──  data
    │   ├── bicimad_stations.csv
    │   └── bicipark_stations.csv
    ├── modules
    │   └──  bicimad.py
    |   └──  bicipark.py
    ├── notebooks
    │   ├── ipynb_checkpoints
    │   └── bicimad.ipynb 
    |   └── dev_notebook_ipynb
    ├── resultados
    │   ├── resultados_bicimad.csv
    |   ├── resultados_bicimad.csv
    ├── .gitignore
    ├── LICENSE
    ├── main.py
    ├── README
    ├── __trash__

**Fulfilled Requirements:**

- It must be contained in a GitHub repository which includes a README file that explains the aim and content of your code. You may follow the structure suggested [here](https://github.com/potacho/data-project-template).

- __It must create, at least, a `.csv` file including the requested table (i.e. Main Challenge).__ Alternatively, you may create an image, pdf, plot or any other output format that you may find convenient. You may also send your output by e-mail, upload it to a cloud repository, etc. 

- It must provide, at least, two options for the final user to select when executing using `argparse`: **(1)** To get the table for every 'Place of interest' included in the dataset (or a set of them), **(2)** To get the table for a specific 'Place of interest' imputed by the user.
# grafapp
## Instalation 

### python app

``` mkdir graf ``` <br />
``` git clone https://github.com/andrenv/grafapp.git ```<br />
``` pip install -r requirements.txt ``` <br />

### Docker

into .devcontainer dir run <br /><br />
``` docker-compose up``` <br />

## Content

The purpose of the test is to build a complete data engeneer tool, capable of dealing with huge data, show valuable information and be scallable.
With that in mind I chose to build a system with four different applications to deal with different parts of ETL and data management

### Grafana

Grafana is the dashboard application I chose to run the plots panel, its a powerfull BI tool capable of dealing with massive ammounts of data easely.
Its one of the three applications running on the docker image. If you are running local you can access that through through port 3000:

```localhost:3000 ```

on my AWS you can access on 

```URL HERE```

### Adiminer

Adiminer is the second docker image running, and its a simple but powerfull database manager, I chose to include that as a tool to manage the MYSQL database
because its scallable and easy to include and manage test data (user: ```admin``` pass: ```admin```

```localhost:8080 ```

on my AWS you can access on 

```URL HERE```

user: ```root``` password: ```example``` (default) database: ```mydatabase``` 

to demonstrate how to use and why use Adminer, after loging into the application, go to run query page and create the table necessary to our application:

```
CREATE TABLE trips (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
region VARCHAR(80),
origin_coord VARCHAR(80),
destination_coord VARCHAR(80),
datetime DATETIME,
datasource VARCHAR(80)
)

```

### MySQL DB

Third docker image but the most important obviously is the database. Also to provide scallability I made a docker image.
it is running on the default port: ```3306``` of your localhost and my AWS.




### Import app

Its the only application not dockerized, because its simply a data insertion tool.
Assuming you already installed the requirements simply run:

```python3 app.py``` in your terminal and access your 

```localhost:8050 ```

on my AWS you can access on 

```URL HERE```

This application provides a portal to insert CSV data (has to be the same format as the example) and also a view on the insertion progress.

Access my AWS Grafana page to find a dashboard with some data analytics for this project.


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
 (user: ```admin``` pass: ```admin```)

```localhost:3000 ```

on my AWS you can access on 

```ec2-18-230-165-116.sa-east-1.compute.amazonaws.com:3000/```

![image](https://user-images.githubusercontent.com/11556513/142773263-0679fb21-f36e-4bf2-aa28-f0ee7a563d9a.png)


### Adiminer

Adiminer is the second docker image running, and its a simple but powerfull database manager, I chose to include that as a tool to manage the MYSQL database
because its scallable and easy to include and manage test data

```localhost:8080 ```

on my AWS you can access on 

```ec2-18-230-165-116.sa-east-1.compute.amazonaws.com:8080/```

user: ```root``` password: ```example``` (default) database: ```mydatabase``` 

![image](https://user-images.githubusercontent.com/11556513/142877099-aaa56f1b-85d9-410d-8095-21a6af7ab7d4.png)



to demonstrate how to use and why use Adminer, after loging into the application, go to run query page and create the table necessary to our application:

![image](https://user-images.githubusercontent.com/11556513/142876967-9429008e-be6a-4b18-8eaa-f034cf511396.png)


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

```localhost:8050/upload ```

on my AWS you can access on 

```ec2-18-230-165-116.sa-east-1.compute.amazonaws.com:8050/upload```

This application provides a portal to insert CSV data (has to be the same format as the example) and also a view on the insertion progress.

![image](https://user-images.githubusercontent.com/11556513/142877225-6bc66b10-7340-488d-ac27-837f8d5c093c.png)
![image](https://user-images.githubusercontent.com/11556513/142877301-fd9b3363-ffa7-45e9-8eed-dd2e7d93a2c8.png)


Access my AWS Grafana page to find a dashboard with some data analytics for this project.


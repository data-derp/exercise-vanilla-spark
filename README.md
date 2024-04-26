# Exercise Vanilla Spark
This project is a simple spark project to demonstrate the spark capabilities. This project contains below spark jobs

The examples in `src/` can be run locally using [docker container](#running-locally-using-docker) or on your 
[local machine using PyCharm](#setting-up-pyspark-locally). The examples are written in Python and can be run using 
PySpark.

# Running locally using docker
The docker build use below tech-stack:
- Spark 3.4.3
- Python 3.11
- OpenJDK 11

1. Setup docker on your local machine using colima or docker desktop.
2. Run below command to run using docker
   ```shell
   docker-compose build
   docker-compose up -d
   ``` 

3. Above command will setup below services
   - Spark Master - This is a spark master service, where all the spark jobs will be submitted
   - Spark Worker - This will setup spark executor nodes, which will connect with spark master
   - Spark History Server [Optional] - This will setup spark history server, keep track of spark jobs

   If Spark History Server is not required, you can comment out the service in `docker-compose.yml` file or can run below command
   ```shell
    docker-compose up -d spark-worker
    ```
   Since worker is dependent on master, it will start the master service as well.

4. You can run the spark job using below command
   ```shell
    docker-compose exec spark-master spark-submit ./src/<file-name>
    ```
5. Once the services are up and running, you can access the spark master UI using below URL
   ```shell
    http://localhost:9090
    ```
6. You can access the spark history server using below URL
   ```shell
    http://localhost:18080
    ```

# Setting up PySpark locally

## Install JDK 11
The Java version that is used for the examples demonstrated on the Spark Shell is Java 11. Please download and install 
the correct java 11 version most suitable for your machine processor (Intel, Apple Silicon etc.). If you already have 
a java version installed, install Java 118 from the link provided and manage the version using [jenv](https://www.jenv.be) 
(You might have to install brew and jenv as mentioned in the link). Once done, make sure that your java version is showing version 
`1.11.x` if you execute `java -version` command from your terminal.

## Setup Python 3.11
We use Python version 3.11 for this set up. Please install it from this [link](https://formulae.brew.sh/formula/python@3.11). You might 
be having other versions of Python installed on your machine already which should be fine. In the next section, we have provided 
an environment variable which should help your setup point to Python 3.11.

# Setup Apache Spark

**Note 1:** Before you proceed with the Apache Spark local installation here, please note that the exercises in House 9 of 
data-derp don't need this set up. They are instead done on Pycharm Spark installation of the next section of this readMe. So 
if you are facing any challenges in doing this Spark local set up, we request you to proceed towards the Pycharm spark installation 
in the next section and complete the exercises of House 9. You can come back to this set up later on. In case if you have come 
here after going through Vanilla Spark videos, and you would like to practice examples on the spark-shell (and you are facing 
challenges in this local spark set up), we request you to get in touch with your tour guide to help you out.

The Apache Spark version that I used for the examples demonstrated use version 3.4.3. You can set it up on your local 
machine using the following steps

1. Please download the file named `spark-3.4.3-bin-hadoop2.7.tgz` (It should be ~ 200MB) from this [link](https://spark.apache.org/downloads.html) 
at a preferred location on your machine
2. Extract/Untar it to get a folder by the name "spark-3.4.3-bin-hadoop2.7".`tar –xvzf spark-3.4.3-bin-hadoop2.7-hive1.2.tgz`
3. Set up the location of the folder extracted in step 2 as your `SPARK_HOME` in your `.bash_profile` or `.zshrc` file 
   ```shell
   export SPARK_HOME="<YOUR_PREFERRED_LOCATION>/spark-3.4.3-bin-hadoop2.7"`
   ```
4. Add the `bin` folder of SPARK_HOME to the path. `export PATH="$JAVA_HOME/bin:$SPARK_HOME/bin:$PATH"`)
5. You should be good to go now. Echo SPARK_HOME `echo $SPARK_HOME` from your terminal. You should be able to get the path to your spark installation location.
6. Open a new terminal and type `$SPARK_HOME/bin/spark-shell`. The spark shell should start with Spark version 3.4.3. ![Spark Shell .png](./assets/Spark%20Shell.png)
7. Before proceeding, set up `export PYSPARK_PYTHON=python3.11` for your pyspark to point to Python 3.11.
8. The same can be done for pyspark `$SPARK_HOME/bin/pyspark`. Please note that in order for pyspark to work, you
   need to have python installed on your machines as mentioned in the "Python Set up instructions above" above. ![PySpark Shell.png](./assets/PySpark%20Shell.png)

# Repo set up in Pycharm
1. Please ensure that Python 3.11 is installed from the **Python Set up Instructions** above.
2. Please install PyCharm community edition from this [link](https://www.jetbrains.com/pycharm/download/#section=mac).
3. Clone this repo on the location of your choice on your machine and import the Repo in Pycharm.
4. Go to your Pycharm **Settings**, select your project and select the **Python Interpreter** option. ![Pycharm ReadMe Step - 4.png](./assets/Pycharm%20ReadMe%20Step%20-%204.png)
5. Make sure that you select **No Interpreter** from the `Python Interpreter` **dropdown** and click **Add Interpreter** and select **Add Local Interpreter**. ![Pycharm ReadMe Step - 5.png](./assets/Pycharm%20ReadMe%20Step%20-%205.png)
6. A dialog box will Pop up. Select the option of **Virtualenv Environment**. ![Pycharm ReadMe Step - 6.png](./assets/Pycharm%20ReadMe%20Step%20-%206.png)
7. In the options on the right-hand side of the same dialog box, select **Environment** as **New**, **Location** as any suitable location to save python "venv" folder on your local machine, leave the **Base Interpreter** as default and select **Inherit global site packages** checkbox. ![Pycharm ReadMe Step - 7.png](./assets/Pycharm%20ReadMe%20Step%20-%207.png)
8. This should set up your Python Virtual Env for this repo. Double-check your Python Interpreter from **Setting** again and make sure that your newly created Python interpreter is selected for the project. ![Pycharm ReadMe Step - 8.png](./assets/Pycharm%20ReadMe%20Step%20-%208.png)
9. Now if your Python Interpreter is created and selected as per the instructions above, you should get a message like `Package requirements 'pyspark...' etc. are not installed`. Click on the **install requirement** link to install the plug-ins required for this repo. These plug-ins are listed down in the `requirements.txt` of this repo. ![Pycharm ReadMe Step - 9.png](./assets/Pycharm%20ReadMe%20Step%20-%209.png)
10. You are all set now to run your first program of this repo. Open source file `00 - File Reads.py` from the SRC folder of this repo and run it. It should give you the desired output of the dataframe as shown below. ![Pycharm ReadMe Step - 10.png](./assets/Pycharm%20ReadMe%20Step%20-%2010.png)

**PS**: Please note that you don't need a separate Apache Spark installation on your local machine to run the examples of this repo from Pycharm. The PySpark plug-in you have configured above should be sufficient.
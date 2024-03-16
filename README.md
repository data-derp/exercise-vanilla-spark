# Java Standard Edition Set up Instructions

The Java version that is used for the examples demonstrated on the Spark Shell is Java 8. Please download and install the correct java 8 version most suitable for your machine processor (Intel, Apple Silicon etc.) from [here](https://www.oracle.com/in/java/technologies/javase/javase8u211-later-archive-downloads.html). If you already have a java version installed, install Java 8 from the link provided and manage the version using [jenv](https://www.jenv.be) (You might have to install brew and jenv as mentioned in the link). Once done, make sure that your java version is showing version `1.8.x` if you execute `java -version` command from your terminal. 


# Python Set up Instructions
We use Python version 3.9 for this set up. Please install it from this [link](https://formulae.brew.sh/formula/python@3.9). You might be having other versions of Python installed on your machine already which should be fine. In the next section, we have provided an environment variable which should help your setup point to Python 3.9.

# Apache Spark Set up Instructions

**Note 1:** Before you proceed with the Apache Spark local installation here, please note that the exercises in House 9 of data-derp don't need this set up. They are instead done on Pycharm Spark installation of the next section of this readMe. So if you are facing any challenges in doing this Spark local set up, we request you to proceed towards the Pycharm spark installation in the next section and complete the exercises of House 9. You can come back to this set up later on. In case if you have come here after going through Vanilla Spark videos, and you would like to practice examples on the spark-shell (and you are facing challenges in this local spark set up), we request you to get in touch with your tour guide to help you out. 

The Apache Spark version that I used for the examples demonstrated use version 3.0.2. You can set it up on your local machine using the following steps

1. Please download the file named `spark-3.0.2-bin-hadoop2.7.tgz` (It should be ~ 200MB) from this [link](https://archive.apache.org/dist/spark/spark-3.0.2/) at a preferred location on your machine
2. Extract / Un tar it to get a folder by the name "spark-3.0.2-bin-hadoop2.7".`tar –xvzf spark-3.0.2-bin-hadoop2.7-hive1.2.tgz`
3. Set up the location of the folder extracted in step 2 as your `SPARK_HOME` in your `.bash_profile` or `.zshrc` file `export SPARK_HOME="<YOUR_PREFERRED_LOCATION>/spark-3.0.2-bin-hadoop2.7"`
4. Add the `bin` folder of SPARK_HOME to the path. `export PATH="$JAVA_HOME/bin:$SPARK_HOME/bin"`)
5. You should be good to go now. Echo SPARK_HOME `echo $SPARK_HOME` from your terminal. You should be able to get the path to your spark installation location.
6. Open a new terminal and type `$SPARK_HOME/bin/spark-shell`. The spark shell should start with Spark version 3.0.2. ![Spark Shell .png](./assets/Spark%20Shell.png)
7. Before proceeding, set up `export PYSPARK_PYTHON=python3.9` for your pyspark to point to Python 3.9.
8. The same can be done for pyspark `$SPARK_HOME/bin/pyspark`. Please note that in order for pyspark to work, you 
   need to have python installed on your machines as mentioned in the "Python Set up instructions above" above. ![PySpark Shell.png](./assets/PySpark%20Shell.png)

# Repo set up in Pycharm
1. Please ensure that Python 3.9 is installed from the **Python Set up Instructions** above.
2. Please install PyCharm community edition from this [link](https://www.jetbrains.com/pycharm/download/#section=mac).
2. Clone this repo on the location of your choice on your machine.
3. Open the Repo in Pycharm.
4. Go to your Pycharm **Settings**, select your project and select the **Python Interpreter** option. ![Pycharm ReadMe Step - 4.png](./assets/Pycharm%20ReadMe%20Step%20-%204.png)
5. Make sure that you select **No Interpreter** from the `Python Interpreter` **dropdown** and click **Add Interpreter** and select **Add Local Interpreter**. ![Pycharm ReadMe Step - 5.png](./assets/Pycharm%20ReadMe%20Step%20-%205.png)
6. A dialog box will Pop up. Select the option of **Virtualenv Environment**. ![Pycharm ReadMe Step - 6.png](./assets/Pycharm%20ReadMe%20Step%20-%206.png)
7. In the options on the right-hand side of the same dialog box, select **Environment** as **New**, **Location** as any suitable location to save python "venv" folder on your local machine, leave the **Base Interpreter** as default and select **Inherit global site packages** checkbox. ![Pycharm ReadMe Step - 7.png](./assets/Pycharm%20ReadMe%20Step%20-%207.png)
8. This should set up your Python Virtual Env for this repo. Double-check your Python Interpreter from **Setting** again and make sure that your newly created Python interpreter is selected for the project. ![Pycharm ReadMe Step - 8.png](./assets/Pycharm%20ReadMe%20Step%20-%208.png)
9. Now if your Python Interpreter is created and selected as per the instructions above, you should get a message like `Package requirements 'pyspark...' etc. are not installed`. Click on the **install requirement** link to install the plug-ins required for this repo. These plug-ins are listed down in the `requirements.txt` of this repo. ![Pycharm ReadMe Step - 9.png](./assets/Pycharm%20ReadMe%20Step%20-%209.png)
10. You are all set now to run your first program of this repo. Open source file `00 - File Reads.py` from the SRC folder of this repo and run it. It should give you the desired output of the dataframe as shown below. ![Pycharm ReadMe Step - 10.png](./assets/Pycharm%20ReadMe%20Step%20-%2010.png)

**PS**: Please note that you don't need a separate Apache Spark installation on your local machine to run the examples of this repo from Pycharm. The PySpark plug-in you have configured above should be sufficient.


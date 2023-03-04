# Java Standard Edition Set up Instructions

The Java version that I used for the examples demonstrated on the Spark Shell is Java 8 (specifically "adoptopenjdk8" openjdk ). This can be installed on your machines using the below commands :-

- brew tap AdoptOpenJDK/openjdk
- brew install --cask adoptopenjdk8

Please also note that for the above command to work, you should have homebrew package manager installed on your machines. The link to do the same would be as follows :-

- https://brew.sh/

# Python Set up Instructions
TBD

# Apache Spark Set up Instructions

The Apache Spark version that I used for the examples demonstrated use version 3.0.2. You can set it up on your local machine using the following steps :-

1. Please download the file named "spark-3.0.2-bin-hadoop2.7.tgz" (It should be ~ 200MB) from this [link](https://archive.apache.org/dist/spark/spark-3.0.2/) at a preferred location on your machine
2. Extract / Un tar it to get a folder by the name "spark-3.0.2-bin-hadoop2.7". (tar –xvzf spark-3.0.2-bin-hadoop2.7-hive1.2.tgz)
3. Set up the location of the folder extracted in step 2 as your SPARK_HOME your .bash_profile or .zshrc (export SPARK_HOME="<YOUR_PREFERRED_LOCATION>/spark-3.0.2-bin-hadoop2.7")
4. Add the bin folder of SPARK_HOME to the path (export PATH="$JAVA_HOME/bin:$SPARK_HOME/bin")
5. You should be good to go now. Echo SPARK_HOME (echo $SPARK_HOME) from your terminal and you should be able to get the path to your spark installation location.
6. Open a new terminal and type $SPARK_HOME/bin/spark-shell. The spark shell should start with Spark version 3.0.2. 
7. You can do the same for pyspark ($SPARK_HOME/bin/pyspark). Please note that in order for pyspark to work, you need to have python installed on your machines as mentioned above





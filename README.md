Initial setup for frame analysis of twitter data

Pre-requisites: Java 1.8, Python 3.6

1. Clone the original SEMAFOR repository at <https://github.com/Noahs-ARK/semafor>

2. In preprocessing, SEMAFOR uses MaltParser as the syntactic dependency parser. To use MaltParser, download and unpack the model files for MaltParser and SEMAFOR from here: <http://www.ark.cs.cmu.edu/SEMAFOR/semafor_malt_model_20121129.tar.gz> (~140MB).

3. Navigate to semafor/bin directory and perform the following steps

Environment Variables setup
-------------------------------
The file `bin/config.sh` lists a set of variables which should be modified within the file before running
SEMAFOR:

- `SEMAFOR_HOME`: absolute path where the repository has been cloned. (for example: ~/home/<usr-name>/SEMAFOR_DEMO/semafor)

- `MALT_MODEL_DIR`: the absolute path where the Malt models have been decompressed. (for example: ~/home/<usr-name>/SEMAFOR_DEMO/models/semafor_malt_model_20121129)

- `JAVA_HOME_BIN`: the absolute path to the bin directory under which the executables javac and java can be found. (for example: /usr/lib/jvm/java-9-oracle/bin)

4. Install/Update "maven" - It is a project management tool we will be using to package and build the Semafor project.
[Command on linux - pip install maven]

5. Clone current repository:

Contents
========

Underneath the root folder, there are the following files and folders:

<dl>
  <dt>data-cleaning/</dt>
    <dd>
      extract_tweet_text.py: Transforms twitter data into simple text format(one tweet per line). This step is performed to convert twitter data in a format(One text sentence per line) as expected by semafor.</br></br>

      Takes two arguments: </br>
      1. Twitter input data in JSON format </br>
      2. Output file-name where you wish to store the extracted tweets.</br>
      Note: Output file should be a simple (.txt) file.
    </dd>

  <dt>post-processing/</dt>
    <dd>
      print_detected_frames.py: Run this file after semafor successfully retrieves frames related to tweets. The output of semafor is a json file. Running this file will print those extracted frames in a human readable format.

      Takes a single argument: </br>
      1. The name of JSON file which contains the frames extracted by semafor.
    </dd>
</dl>

6. If you wish to run the demo given in step 7, make sure your directory structure is as follows:
SEMAFOR_DEMO/
├── data-cleaning
│   ├── extract_tweet_text.py
│   └── inp_test.json
├── models
│   └── semafor_malt_model_20121129
│       ├── argmodel.dat
│       ├── engmalt.linear-1.7.mco
|       ...
├── post-processing
│   └── print_detected_frames.py
├── README.md
└── semafor
    ├── bin
    │   ├── config.sh
    │   ├── runMalt.sh
    │   ├── runSemafor.sh
    │   └── tokenizeAndPosTag.sh
    ├── dependency-reduced-pom.xml
    ├── dict
    │   ├── adj.dat
    │   ├── adj.exc
    │   ├── adj.idx
    |   ...


7. Steps to run a quick demo with sample datasets already present in the repository:
root:
SEMAFOR_DEMO/
$ cd semafor
$ mvn package

[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 22.307 s
[INFO] Finished at: 2018-02-05T01:14:14-05:00
[INFO] Final Memory: 39M/129M
[INFO] ------------------------------------------------------------------------

$ cd ../data-cleaning
$ python extract_tweet_text.py inp_test.json out_test.txt

Process Complete.
Output written to file:  out_test.txt
# lines written:  50

$ cd ../semafor/bin

# syntax to run semafor: ./runSemafor.sh <absolute-path-to-input-file-with-one-sentence-per-line> <output-file> <number-of-threads>
$ ./runSemafor.sh ../../data-cleaning/out_test.txt ../../post-processing/extracted_frames.json 10

real	0m28.544s
user	1m6.188s
sys	0m2.196s
Finished frame-semantic parsing.
********************************

# if the program errors out saying:
  edu.cmu.cs.lti.ark.util.CommandLineOptions$InvalidOptionsException: Parent directory of the value of 'output-file' option does not exist: ./extracted_frames.json
  	at edu.cmu.cs.lti.ark.util.CommandLineOptions$NewFilePathOption.set(CommandLineOptions.java:127)
  	at edu.cmu.cs.lti.ark.util.CommandLineOptions.init(CommandLineOptions.java:267)
  	at edu.cmu.cs.lti.ark.fn.utils.FNModelOptions.<init>(FNModelOptions.java:40)
  	at edu.cmu.cs.lti.ark.fn.utils.FNModelOptions.<init>(FNModelOptions.java:36)
  	at edu.cmu.cs.lti.ark.fn.Semafor.main(Semafor.java:94)

==> give absolute paths for both(input file and output file)

$ cd ../../post-processing
$ python print_detected_frames.py extracted_frames.json

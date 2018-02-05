import json
import sys
# import tqdm
import re

def main():
    '''
    Semafor expects data is a simple format (1 sentence per line).
    We extract tweet texts in the input file and store it to output file
    input: Expects input file to be in json format
    output: Output is in simple text format
    '''

    if len(sys.argv) == 3:

        dataset = sys.argv[1]   # input file

        out_fname = sys.argv[2]  # output file

        with open(dataset, 'r') as tweets_file, open(out_fname, 'w') as output_file:

            print('Conversion started')
            for i, line in enumerate(tweets_file):

                tweet_json = json.loads(line)

                tweet_text = ''

                if 'tweetText' in tweet_json:
                    tweet_text = tweet_json['tweetText'].lower()

                elif 'text' in tweet_json:
                    tweet_text = tweet_json['text'].lower()

                else:
                    print('Could not find text element in json')


                tweet_text = check_if_valid(tweet_text)
                output_file.write(tweet_text+'\n')

            print('Process Complete.')
            print('Output written to file: ', out_fname)
            print('# lines written: ', i+1)


    else:
        print("Usage: 'python extract_tweet_text.py <inp-dataset-file-name> <out-file-name>' ")

def check_if_valid(text):
    # print('inp text: ' , text)
    text = text.strip()
    text = text.replace('\n','')
   
    return text

main()
# check_if_valid("\"You know, I've got you like a puppet in the palm of my hand\"")

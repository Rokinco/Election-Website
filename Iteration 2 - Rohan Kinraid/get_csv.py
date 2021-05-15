import csv, requests, urllib.request, os


url = 'https://www.electionresults.govt.nz/electionresults_2017/statistics/csv/candidate-votes-by-voting-place-4.csv'

class get_candidates:

    def __init__(self, url):
        self.url = url


    #Get electorate csv from link and download as csv file into dir
    def get_csv(link):
        r = requests.get(link, allow_redirects=True)
        open("csv_test4.csv", 'wb').write(r.content)


    #read csv file and return candidate object as a list
    def generate_candidates():
        loop = 0
        candidate_list = []
        reader = csv.reader(open("csv_test4.csv"), delimiter = '"',quotechar='|')
        for row in reader:
            loop += 1
            if loop == 3:
                for candidate in row:
                    if candidate != ",Total Valid Candidate Votes,Informal Candidate Votes" and candidate != "," and candidate != ",,":
                        candidate_list.append(candidate)
                break
        return candidate_list

##if __name__ == '__main__':
    ##print(get_candidates.generate_candidates())

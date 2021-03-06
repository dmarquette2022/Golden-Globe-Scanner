'''Version 0.35'''

from host import host
from winner import get_winners, get_nominee
from presenter import get_presenter
from AwardNames import findAwardNames
from sentiment import get_sentiments
from NomineeGather import findAllNominees
from redCarpet import red_carpet
from NomineeGather import findAllNominees

import pickle
import json 

OFFICIAL_AWARDS_1315 = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
OFFICIAL_AWARDS_1819 = ['best motion picture - drama', 'best motion picture - musical or comedy', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best performance by an actress in a motion picture - musical or comedy', 'best performance by an actor in a motion picture - musical or comedy', 'best performance by an actress in a supporting role in any motion picture', 'best performance by an actor in a supporting role in any motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best motion picture - animated', 'best motion picture - foreign language', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best television series - musical or comedy', 'best television limited series or motion picture made for television', 'best performance by an actress in a limited series or a motion picture made for television', 'best performance by an actor in a limited series or a motion picture made for television', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best performance by an actress in a television series - musical or comedy', 'best performance by an actor in a television series - musical or comedy', 'best performance by an actress in a supporting role in a series, limited series or motion picture made for television', 'best performance by an actor in a supporting role in a series, limited series or motion picture made for television', 'cecil b. demille award']

def get_hosts(year):
    '''Hosts is a list of one or more strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    hosts = host(year)
    return hosts

def get_awards(year):
    '''Awards is a list of strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    awards = findAwardNames(year)
    return awards

def get_nominees(year):
    '''Nominees is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change
    the name of this function or what it returns.'''

    # Your code here
    return get_nominee(int(year))

def get_winner(year):
    '''Winners is a dictionary with the hard coded award
    names as keys, and each entry containing a single string.
    Do NOT change the name of this function or what it returns'''
    # Your code here
    winners = get_winners(int(year))
    return winners

def get_presenters(year):
    '''Presenters is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change the
    name of this function or what it returns.'''
    # Your code here
    presenters = get_presenter(int(year))
    return presenters

def pre_ceremony():
    '''This function loads/fetches/processes any data your program
    will use, and stores that data in your DB or in a json, csv, or
    plain text file. It is the first thing the TA will run when grading.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    print("Pre-ceremony processing complete.")
    return

def main():
    '''This function calls your program. Typing "python gg_api.py"
    will run this function. Or, in the interpreter, import gg_api
    and then run gg_api.main(). This is the second thing the TA will
    run when grading. Do NOT change the name of this function or
    what it returns.'''
    # Your code here
    finalAnswers = {"hosts": "", "award_data":""}
    awardDict = {}
    years = [2013, 2015]
    for year in years:
        if year <= 2015:
            awards = OFFICIAL_AWARDS_1315
        else:
            awards = OFFICIAL_AWARDS_1819
        winner_dict = get_winner(year)
        nominee_dict = get_nominees(year)
        presenter_dict = get_presenters(year)
        finalAnswers["hosts"] = get_hosts(year)
        for item in awards:
            tempDict = {}
            tempDict["nominees"] = nominee_dict[item]
            tempDict["winner"] = winner_dict[item]
            tempDict["presenters"] = presenter_dict[item]
            awardDict[item] = tempDict
        finalAnswers["award_data"] = awardDict
        finalAnswers["awards"] = awards
        finalAnswers["awards"] = get_awards(year)
        with open("answer{}.json".format(year) , 'w') as f:
            json.dump(finalAnswers, f)

        finalAnswers["sentiments"] = get_sentiments(year, winner_dict, finalAnswers["hosts"])
        finalAnswers["red_carpet"] = red_carpet(year)
        #print(json.dumps(finalAnswers, sort_keys=True, indent=4))
        
        #with open('output{}.txt'.format(year), 'wb') as f: 
        #    pickle.dump(str(finalAnswers), f)

        with open("answer{}.txt".format(year) , 'w', encoding='utf-8') as f:
            f.write('Hosts: {}\n\n'.format(', '.join(finalAnswers['hosts'])))
            for award in finalAnswers['award_data']:
                f.write('Award: {}\n'.format(award))
                f.write('Presenters: {}\n'.format(', '.join(finalAnswers['award_data'][award]['presenters'])))
                f.write('Nominees: {}\n'.format(', '.join(finalAnswers['award_data'][award]['nominees'])))
                f.write('Winner: {}\n\n'.format(finalAnswers['award_data'][award]['winner']))
            f.write('Best Dressed: {}\n'.format(finalAnswers['red_carpet']['best dressed']))
            f.write('Most Controversial: {}\n'.format(finalAnswers['red_carpet']['most controversial']))
            f.write('Worst Dressed: {}\n'.format(finalAnswers['red_carpet']['worst dressed']))
            for person in finalAnswers['sentiments'][0]:
                f.write('Sentiments on {}: {}\n'.format(person, finalAnswers['sentiments'][0][person]))
        
        #print(finalAnswers)


    return

if __name__ == '__main__':
    main()

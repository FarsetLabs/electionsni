import pandas as pd
import json

#Variables
year = 2022
folder_path = 'E:/Personal/Github/electionsni/2022/NI/'

candidates = pd.read_csv(folder_path + 'full-candidates-list.csv',encoding='UTF-8')

cons_candidates = (candidates.groupby(['constituency_name', 'constituency_number'])
                             .apply(lambda x: x[['surname','firstname', 'gender', 'twitter', 'constituency_name', 'constituency_number', 'party_name', 'outgoing_member', 'candidate_id', 'directory', 'party_id', 'email', 'photo_url']].to_dict('records'))
                             .reset_index()
                             .rename(columns={0:'Candidates'})
                             .to_json(orient='records'))

cons_candidates_full = {'Constituencies':json.loads(cons_candidates)}

with open(folder_path + 'all-candidates.json', 'w') as outfile:
    json.dump(cons_candidates_full, outfile)

party_candidates = (candidates.groupby(['party_name', 'party_id'])
                             .apply(lambda x: x[['surname','firstname', 'gender', 'twitter', 'constituency_name', 'constituency_number', 'party_name', 'outgoing_member', 'candidate_id', 'directory', 'party_id', 'email', 'photo_url']].to_dict('records'))
                             .reset_index()
                             .rename(columns={0:'Candidates'})
                             .to_json(orient='records'))

party_candidates_full = {'Parties':json.loads(party_candidates)}

with open(folder_path + 'all-party-candidates.json', 'w') as outfile:
    json.dump(party_candidates_full, outfile)


#print(candidates.to_json())
from parlai.core.teachers import DialogTeacher
import json
import os

def _path(opt):
    # set up path to data (specific to each dataset)
    dt = opt['datatype'].split(':')[0]
    return os.path.join('C:\\Users\\97919\\Desktop\\GUGUAI\\ParlAI-main\\parlai\\tasks\\roleplay', dt + '.json')

class RoleplayTeacher(DialogTeacher):
    def __init__(self, opt, shared=None):
        opt['datafile'] = _path(opt)
        super().__init__(opt, shared)

    def setup_data(self, path):
        print('loading: ' + path)

        with open(path.replace('train.json', 'merged_data.json'), 'r') as data_file:
            for dialogue in json.load(data_file):
                # each dialogue is a list of turns
                # we will create an episode for each dialogue
                for i in range(len(dialogue['dialogue'])):
                    # each turn is a dict containing 'role' and 'content'
                    # we will use 'content' as the text and 'role' as the label
                    yield (dialogue['dialogue'][i]['content'], dialogue['dialogue'][i]['role'], None, None), i == len(dialogue['dialogue']) - 1

DefaultTeacher = RoleplayTeacher

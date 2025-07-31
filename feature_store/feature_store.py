

# Sample Data
'''
{
    'feat 1': 
        [
            ('user 1', 30), 
            ('user 2', 40), 
            ('user 2', 35)
        ]
    'feat 2': 
        [
            ('user 2', 540), 
            ('user 3', 450), 
            ('user 1', 540)
        ]
}
'''



class FeatureStore():

    '''
    
    The goal of this feature store is to save one feature at a time, and retrieve the latest feature
    for the user
    
    '''

    def __init__(self):

        self.data = {}


    def add(self, user_id, feat_name, feat_value):
       
       # Logic for 1 feature addition
        if feat_name not in self.data:
            self.data[feat_name] = [(user_id, feat_value)]

        else:
            self.data[feat_name].append((user_id, feat_value))
        
    
    def fetch(self, feat_name):

        # Checks if the feature exists in the data store, if yes then returns latest value
        # Else returns -1

        if feat_name in self.data:
            return self.data[feat_name][-1](-1)
        else:
            return -1


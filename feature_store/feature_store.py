

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

    def __init__(self, n_features):
        self.data = {}
        self.n_features = n_features

    def add_feature(self, feature):

        if len(self.data) < self.n_features:
            if feature not in self.data:
                self.data[feature] = []
            else:
                print('Feature already exists in the feature store.')
        else:
            print(f'Cannot add {feature}. Maximum number of features reached.')


    def add(self, user_id, feat_name, feat_value):
        '''
        Add one feature at a time

        Args:
            user_id: Unique user ID
            feat_name: Feature name to be added
            feat_value: Feature value to be added
        '''
       
        # Logic for 1 feature addition
        if feat_name not in self.data:

            if len(self.data) < self.n_features:
                self.data[feat_name] = [(user_id, feat_value)]
            else:
                print('Add unsuccesful. Maximum number of features reached.')

        else:
            self.data[feat_name].append((user_id, feat_value))
        
    def fetch(self, feat_name):
        '''
        Fetch one feature (latest value) at a time

        Args:
            feat_name: Feature name to be added

        Returns:
            Any: Value corresponding to the feature name

        '''

        # Checks if the feature exists in the data store, if yes then returns latest value
        # Else returns -1

        if feat_name in self.data:
            return self.data[feat_name][-1](-1)
        else:
            return -1


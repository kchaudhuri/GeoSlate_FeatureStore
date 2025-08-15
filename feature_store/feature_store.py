

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

        self.registered_users = {}
        self.user_log = []
        self.data = {} # Datastore
        self.n_features = n_features # Number of features to be stored

    def register_user(self, user_id, user_name):
        '''
        Register user for interaction with the feature store.

        Args:
            user_id: Unique user identifier
            user_name: User name
        '''

        self.registered_users[user_id] = user_name
        print('User registered successfully')
        print(f'{user_id} : {user_name}')

    def add_feature(self, user_id, feature):
        '''
        Function to add a new feature to the feature store.

        Args:
            feature: Feature name to be added
        '''
        # Check for valid user
        if user_id in self.registered_users:

            # Track userid interaction
            self.user_log.append((user_id, 'add_feature'))

            # If the total number features greater than number of features limit then add feature
            if len(self.data) < self.n_features:

                # Check for duplicate feature
                if feature not in self.data:
                    self.data[feature] = []
                else:
                    print(f"Feature '{feature}' already exists in the feature store.")
            else:
                print(f"Cannot add '{feature}'. Maximum number of features reached.")

        else:
            print('Please register before working with the Feature store.')

    def add_data(self, user_id, feat_sets):
        '''
        Function to add feature data (row-wise) by the user.

        Args:
            user_id: User Id of the user interacting with the feature store
            feat_sets: Data to be added (List of dictionaries), each element in the list represents
                    a data sample.
        '''

        # Check for valid user
        if user_id in self.registered_users:

            # Track userid interaction
            self.user_log.append((user_id, 'add_data'))

            # Iterate through all samples
            for feat_set in feat_sets:

                # Validate if all keys are already present in the feature store
                # if yes then proceed or else quit

                # Iterate through each feature key:value pairs
                for feat_key in feat_set.keys():

                    value = feat_set[feat_key]

                    # Add the feature value to the feature store
                    self.data[feat_key].append(value)
        
        else:
            print('Please register before working with the Feature store.')

        
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

    def snapshot(self):
        # Returns the entire feature store data

        return self.data

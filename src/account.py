class Account:

    def __init__(self, first_name, last_name, email_address, profiles):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.profiles = profiles

    def add_profile(self, profile):
        self.profiles.append(profile)

    def remove_profile(self, profiles):
        self.profiles.remove(profiles)

    def get_profiles(self):
        return self.profiles
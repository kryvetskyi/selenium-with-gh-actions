from faker import Faker

# Create an instance of the Faker class
fake = Faker()


# Generate a fake username and password
def generate():
    fake_username = fake.user_name()
    fake_password = fake.lexify(text='????????')
    return fake_username, fake_password

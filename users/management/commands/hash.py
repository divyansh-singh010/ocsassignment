# import hashlib
# from django.core.management.base import BaseCommand
# from users.models import User


# class Command(BaseCommand):

#     def handle(self, *args, **kwargs):
#         for user in users:
#             user['password_hash'] = hashlib.md5(
#                 user['password'].encode('utf-8')).hexdigest()
#             User.objects.create(
#                 userid=user['userid'], password_hash=user['password_hash'], role=user['role'])
#             print(user['userid'] + " created" + " " +
#                   user['role'] + " " + user['password_hash'])
#         self.stdout.write(self.style.SUCCESS('Successfully created users'))


# users = [{'userid': 'admin_test', 'password': 'password', 'role': 'admin'}, {'userid': 'user1', 'password': 'passwordabc', 'role': 'basic'}, {'userid': 'user2',
#                                                                                                                                               'password': 'password', 'role': 'basic'}, {'userid': 'lakshya', 'password': 'password', 'role': 'basic'}, {'userid': 'basic_test_user', 'password': 'password123', 'role': 'basic'}]

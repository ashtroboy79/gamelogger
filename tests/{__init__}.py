# from flask_testing import TestCase
# from application import app, db
# from application.models import Gamer

# class TestBase(TestCase):
#     def create_app(self):
#         app.config.update(
#             SQLALCHEMY_DATABASE_URI='sqlite:///',
#             DEBUG=True,
#             WTF_CSRF_ENABLED=False
#         )
#         return app

#     def setUp(self):
#         db.create_all()
#         bob = Gamer(name='Bob The Builder')
#         joe = Gamer(name='Joe Bloogs')
#         db.session.add_all([bob,joe])
#         db.session.commit()
    
#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()

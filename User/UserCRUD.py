from User.Labor import Labor
from User.User import User
from db import Session


def add_user(user):
    # create a new session
    session = Session()
    # add the user to the session
    session.add(user)
    # commit the changes to the database
    session.commit()
    session.close()


def get_user(user_id):
    # create a new session
    session = Session()
    # retrieve the user from the database
    user = session.query(User).filter_by(id=user_id).first()
    session.close()
    return user


def update_user(user):
    # create a new session
    session = Session()
    # retrieve the user from the database
    db_user = session.query(User).filter_by(id=user.id).first()
    # update the user's properties
    db_user.name = user.name
    db_user.username = user.username
    db_user.jobTitle = user.jobTitle
    if isinstance(user, Labor):
        db_user.houseNu = user.houseNu
        db_user.farmName = user.farmName
    # commit the changes to the database
    session.commit()
    session.close()


def delete_user(user):
    # create a new session
    session = Session()
    # delete the user from the database
    session.delete(user)
    # commit the changes to the database
    session.commit()
    session.close()

from model import Users, db, Labor


def db_create_user(name, username, jobTitle):
    new_user = Users(name=name, username=username, jobTitle=jobTitle)
    db.session.add(new_user)
    db.session.commit()


def db_create_labor(name, username, farmName, barnNumber):
    new_user = Users(name=name, username=username, jobTitle="Labor")
    db.session.add(new_user)
    db.session.commit()
    new_labor = Labor(user_id=new_user.user_id, houseNu=barnNumber, farmName=farmName)
    # print(new_user.user_id)
    db.session.add(new_labor)
    db.session.commit()

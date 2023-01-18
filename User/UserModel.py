from model import Users, db, Labor, user_schema, labor_schema


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


def get_user_info(user_id):
    user = Users.query.filter_by(user_id=user_id).first()
    if not user:
        return None
    user_info = user_schema.dump(user)
    if user.jobTitle == 'Labor':
        labor = Labor.query.filter_by(user_id=user_id).first()
        labor_info = labor_schema.dump(labor)
        user_info.update(labor_info)
    return user_info

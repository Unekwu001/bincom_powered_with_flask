import datetime
from pkg import db
 
class Announced_pu_results(db.Model): 
    result_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    polling_unit_uniqueid = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer(), nullable=False)
    entered_by_user = db.Column(db.String(100), nullable=False)
    date_entered = db.Column(db.DateTime(), nullable=False )
    user_ip_address = db.Column(db.String(50), nullable=False)

class Announced_ward_results(db.Model): 
    result_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    ward_name = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer(), nullable=False)
    entered_by_user = db.Column(db.String(100), nullable=False)
    date_entered = db.Column(db.DateTime(), nullable=False)
    user_ip_address = db.Column(db.String(50), nullable=False)


class Announced_lga_results(db.Model): 
    result_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    lga_name = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer(), nullable=False)
    entered_by_user =db.Column(db.String(20), nullable=False)
    date_entered = db.Column(db.DateTime(), nullable=False)
    user_ip_address = db.Column(db.String(50), nullable=False)

class Announced_state_results(db.Model): 
    result_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    state_name = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer(), nullable=False)
    entered_by_user = db.Column(db.String(20), nullable=False)
    date_entered = db.Column(db.DateTime(), nullable=False)
    user_ip_address = db.Column(db.String(50), nullable=False)


class Party(db.Model):
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    partyid = db.Column(db.String(11), nullable=False)
    partyname = db.Column(db.String(11), nullable=False)



class States(db.Model):
    state_id = db.Column(db.Integer(), primary_key=True)
    state_name = db.Column(db.String(50), nullable=False)

class Lga(db.Model):
    uniqueid = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    lga_id = db.Column(db.Integer(), nullable=False)
    lga_name = db.Column(db.String(50), nullable=False)
    state_id = db.Column(db.Integer(), nullable=False)
    lga_description = db.Column(db.String(100), nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime(), nullable=False)
    user_ip_address = db.Column(db.String(50), nullable=False)

class Ward(db.Model):
    uniqueid = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    ward_id = db.Column(db.Integer(), nullable=False)
    ward_name = db.Column(db.String(50), nullable=False)
    lga_id = db.Column(db.Integer(), nullable=False)
    ward_description = db.Column(db.String(100), nullable=True)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime(), nullable=False)
    user_ip_address = db.Column(db.String(50), nullable=False)

class Polling_unit(db.Model):
    uniqueid = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    polling_unit_id = db.Column(db.Integer(), nullable=False)
    ward_id = db.Column(db.Integer(), nullable=False)
    lga_id = db.Column(db.Integer(), nullable=False)
    uniquewardid = db.Column(db.Integer(), nullable=True)
    polling_unit_number = db.Column(db.String(50),nullable=True)
    polling_unit_name = db.Column(db.String(50),nullable=True)
    polling_unit_description = db.Column(db.String(200),nullable=True)
    lat = db.Column(db.String(50),nullable=True)
    long = db.Column(db.String(50),nullable=True)
    entered_by_user = db.Column(db.String(50), nullable=True)
    date_entered = db.Column(db.DateTime(), nullable=True)
    user_ip_address = db.Column(db.String(50), nullable=True)

 
class Agentname(db.Model):
    name_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    firstname = db.Column(db.String(50), nullable=True) 
    lastname = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.String(50), nullable=True)
    pollingunit_uniqueid = db.Column(db.Integer(), nullable=True)
 
 
 
 

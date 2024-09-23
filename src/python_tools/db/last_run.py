from datetime import datetime

from python_tools.db.app_model import LastRun
from python_tools.db.last_run_curd import DBLastRun


def main():
    db = DBLastRun()
    # Instantiate the LastRun object
    new_run = LastRun(name="Job1", fullname="Job Fullname 1", nickname="JobNick1", start_date=datetime.now(),
        last_date=None, status="running", created_at=datetime.now(), updated_at=datetime.now())

    # Create or update the LastRun entry using the object
    created_run = db.create_lastrun(new_run)

    # Update the object fields and call the update function
    new_run.status = "completed"
    updated_run = db.update_lastrun(new_run)

    new_run = LastRun(name="Job1", fullname="Job Fullname 2", nickname="Anudy", start_date=datetime.now(),
        last_date=None, status="running", created_at=datetime.now(), updated_at=datetime.now())

    # Create or update the LastRun entry using the object
    created_run = db.create_lastrun(new_run)

    all_rec = db.get_all_lastruns()
    print(all_rec)
    for rec in all_rec:
        print(rec)



if __name__ == "__main__":
    main()

# INSERT INTO user (name, fullname, nickname, date, status, created_at, updated_at) VALUES ('John', 'John Doe', 'Johnny', '2024-09-21 19:09:51.484769', 'active', '2024-09-21 19:09:51.490379', '2024-09-21 19:09:51.490400')

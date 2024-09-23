from python_tools.db.app_model import LastRun
from python_tools.db.db_connection import get_db


class DBLastRun:
    def __init__(self):
        self.db = get_db()

    def create_lastrun(self, lastrun_obj: LastRun):
        existing_run = self.db.query(LastRun).filter(LastRun.name == lastrun_obj.name).first()

        if existing_run:
            return self.update_lastrun(lastrun_obj)  # If the run exists, update it

        self.db.add(lastrun_obj)
        self.db.commit()
        self.db.refresh(lastrun_obj)
        return lastrun_obj

    def update_lastrun(self, lastrun_obj: LastRun):
        run = self.db.query(LastRun).filter(LastRun.name == lastrun_obj.name).first()

        if run:
            run.fullname = lastrun_obj.fullname
            run.nickname = lastrun_obj.nickname
            run.start_date = lastrun_obj.start_date
            run.last_date = lastrun_obj.last_date
            run.status = lastrun_obj.status
            run.updated_at = lastrun_obj.updated_at  # Will auto-update due to onupdate

            self.db.commit()
            self.db.refresh(run)
            return run

        return None  # Return None if the run does not exist

    def delete_lastrun(self, name: str):
        run = self.db.query(LastRun).filter(LastRun.name == name).first()
        if run:
            self.db.delete(run)
            self.db.commit()

    def get_lastrun_by_name(self, name: str):
        return self.db.query(LastRun).filter(LastRun.name == name).first()

    def get_all_lastruns(self):
        return self.db.query(LastRun).all()

from abc import ABC, abstractmethod

# Abstract class
class JobRunner(ABC):

    @abstractmethod
    def run(self):
        """This method must be implemented by the inheriting class"""
        pass

    def execute(self):
        """Encapsulate the full workflow: setup -> run -> cleanup"""
        self.setup()
        self.run()
        self.cleanup()

    def setup(self):
        """This method should be called at the start of run"""
        print("Setting up before the job...")

    def cleanup(self):
        """This method should be called at the end of run"""
        print("Performing cleanup after the job...")

# Inheriting class
class MyJob(JobRunner):

    def run(self):
        # Job execution logic here
        print("Running the job...")

# Example usage
if __name__ == "__main__":
    job = MyJob()
    job.execute()  # Now it automatically handles setup, run, and cleanup

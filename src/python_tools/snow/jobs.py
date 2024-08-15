from abc import ABC, abstractmethod

#write a python program to run  5 jobs in sequence, even one job fails other jobs should continue and get the finished status of the each job, send out the job status in nice html e-mail format
class Job(ABC):
    @abstractmethod
    def run(self):
        """
        This method should be implemented by all subclasses.
        It contains the logic that should be executed for the job.
        """
        pass

    def get_status(self):
        """
        This method should return the status of the job.
        """
        try:
            result = self.run()
            return "Success" if result else "Failed"
        except Exception as e:
            return f"Failed: {str(e)}"

import time

class Job1(Job):
    def run(self):
        time.sleep(1)
        print("Job 1 completed.")
        return True

class Job2(Job):
    def run(self):
        time.sleep(1)
        print("Job 2 completed.")
        return True

class Job3(Job):
    def run(self):
        time.sleep(1)
        print("Job 3 failed.")
        raise Exception("Job 3 failed.")

class Job4(Job):
    def run(self):
        time.sleep(1)
        print("Job 4 completed.")
        return True

class Job5(Job):
    def run(self):
        time.sleep(1)
        print("Job 5 completed.")
        return True

def run_jobs():
    jobs = [Job1(), Job2(), Job3(), Job4(), Job5()]
    job_status = {}

    for i, job in enumerate(jobs, start=1):
        status = job.get_status()
        job_status[f"Job {i}"] = status

    return job_status

def send_email(job_status):
    # Define email sender and receiver
    sender_email = "your_email@example.com"
    receiver_email = "receiver@example.com"
    password = "your_password"  # Use a secure method to handle this

    # Create the HTML body for the email
    html = f"""
    <html>
    <body>
        <h2>Job Status Report</h2>
        <table border="1" cellpadding="10">
            <tr>
                <th>Job</th>
                <th>Status</th>
            </tr>
    """

    for job, status in job_status.items():
        html += f"<tr><td>{job}</td><td>{status}</td></tr>"

    html += """
        </table>
    </body>
    </html>
    """

    # Set up the MIME
    message = MIMEMultipart("alternative")
    message["Subject"] = "Job Status Report"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Attach the HTML content to the email
    part = MIMEText(html, "html")
    message.attach(part)

    # Send the email
    with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully.")

def main():
    job_status = run_jobs()
    send_email(job_status)

if __name__ == "__main__":
    main()

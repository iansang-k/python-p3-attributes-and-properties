#!/usr/bin/env python3
class Person:
    APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]


    def __init__(self, name="Unknown", job="Sales"):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Unknown"

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in Person.APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
            self._job = "Sales"

#!/usr/bin/env python3

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

class Person:
    def __init__(self):
        self._name = None
        self._job = "Programmer"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 0 < len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be a string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in the list of approved jobs.")


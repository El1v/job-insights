from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    dict = []
    with open(path) as file:
        list = csv.DictReader(file)
        for line in list:
            dict.append(line)

        return dict


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    job_types = {job["job_type"] for job in jobs}
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = [job for job in jobs if job["job_type"] == job_type]

    return filtered_jobs

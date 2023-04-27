from typing import Union, List, Dict

from src.insights.jobs import read

# from jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    salaries = [
        int(job["max_salary"]) for job in jobs if job["max_salary"].isdigit()
    ]

    return max(salaries)


def get_min_salary(path: str) -> int:
    jobs = read(path)
    salaries = [
        int(job["min_salary"]) for job in jobs if job["min_salary"].isdigit()
    ]

    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary_f = float(job["min_salary"])
        max_salary_f = float(job["max_salary"])
        salary_f = float(salary)
    except (TypeError, ValueError, KeyError):
        raise ValueError("Invalid salary")

    if min_salary_f > max_salary_f:
        raise ValueError("Min_salary must be greater than max_salary")

    return min_salary_f <= salary_f <= max_salary_f


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except (ValueError, TypeError):
            pass

    return filtered_jobs

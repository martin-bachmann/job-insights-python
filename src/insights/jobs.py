from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    try:
        with open(path, encoding="utf-8") as file:
            data = csv.DictReader(file)
            jobs = [*data]
            return jobs
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo não encontrado: " + path)


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    unique_jobs_types = []
    for job in jobs:
        if job["job_type"] not in unique_jobs_types:
            unique_jobs_types.append(job["job_type"])
    return unique_jobs_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError

# -------------------------
# Do not change the below Code
# -------------------------
def helper_fun1_(arr, i):
    while i > 0:
        parent = (i - 1) // 2
        if arr[i] < arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent
        else:
            break

    return arr

def helper_fun2_(arr, i):
    n = len(arr)

    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            i = smallest
        else:
            break
    return arr

# ------------------------------------------------------------
# Q1 — schedule_next_job
# ------------------------------------------------------------
# A cloud system maintains a job list where each job has a
# priority score (smaller value = higher priority).
#
# The system must always be able to quickly access (O(1)) the job
# with the highest priority (smallest score).
#
# You are given the current job list (arr) and a new job
# (priority_score).
#
# Write a function to add a new job into the system
# and and reorganize the list so that the priority rule is maintained.

# IMPORTANT:
# - You may use the provided helper functions to adjust the structure.
# - Do NOT implement any additional helper functions.
# ------------------------------------------------------------

def schedule_next_job(jobs, new_job):
    jobs.append(new_job)
    updated_jobs = helper_fun1_(jobs, len(jobs) - 1)
    return updated_jobs   


# ------------------------------------------------------------
# Q2 — process_next_job
# ------------------------------------------------------------
# A system processes jobs based on priority score
# (smaller value = higher priority).
#
# The job with the highest priority is always processed first.
#
# Given the current job list (arr), remove and return the
# next job to process.
#
# After removal, reorganize the list to maintain the
# priority rule.
#
# IMPORTANT:
# - You may use the provided helper functions to adjust the structure.
# - Do NOT implement any additional helper functions.
#
# ------------------------------------------------------------

def process_next_job(arr):
    if len(arr) == 0:
        return None
    highest_priority_job = arr[0]
    last_item = arr.pop()

    if len(arr) > 0:
        arr[0] = last_item
        helper_fun2_(arr,0)
        return highest_priority_job, arr

# ------------------------------------------------------------
# Q3 — personal priority reflection
# ------------------------------------------------------------
# This question is about reflecting on your personal priorities.
#
# You are given a structure where each item is:
#     (weight, category)
#
# Smaller weight = higher priority.
#
# Instructions:
# 1. Change the weights (numbers) based on YOUR priorities.
# 2. Do NOT change the category names.
# 3. Insert a new category ("security") with your chosen weight.
# 4. Maintain the structure using the provided helper function.
#
# NOTE:
# - There is NO single correct answer.
# - Focus on meaningful weights based on your perspective.
# - Do NOT create additional helper functions.
# ------------------------------------------------------------

def personal_priority_q():
    priorty_q = [
        (4, "education"),
        (3, "family"),
        (1, "health"),
        (5, "friends"),
        (2, "money")
    ]
    new_item = (2, "security")

    priorty_q.append(new_item)

    for i in range(1, len(priorty_q)):
        helper_fun1_(priorty_q, i)

    return priorty_q
